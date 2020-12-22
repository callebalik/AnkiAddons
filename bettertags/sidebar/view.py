# -*- coding: utf-8 -*-

# BetterTags Add-on for Anki
#
# Copyright (C) 2017-2020  Aristotelis P. <https//glutanimate.com/>
# Copyright (C) 2006-2020  Ankitects Pty Ltd and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the accompanied license file.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License which
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from typing import List, Optional

from PyQt5.QtCore import QModelIndex, QPoint, Qt
from PyQt5.QtGui import QDropEvent, QKeySequence
from PyQt5.QtWidgets import QAbstractItemView, QColorDialog, QMenu, QShortcut

try:
    from PyQt5 import sip
except ImportError:
    import sip  # type: ignore

from anki.hooks import runHook
from anki.lang import ngettext
from aqt.browser import Browser
from aqt.utils import askUser, getText

from ..config import config, user_data
from ..helpers import browserEditorSaveThen, resetBrowser
from ..mediator import TagReplacementMediator
from .const import PIN_STATE_BOTTOM, PIN_STATE_TOP, SIDEBAR_ITEM_TYPE_TAG
from .item import SidebarItem
from .model import SidebarModel

SEPARATOR = config["local"]["hierarchicalTagsSeparator"]


class SidebarTreeView(Browser.SidebarTreeView):

    model: SidebarModel

    def __init__(self):
        super().__init__()
        self.browser: Browser = None
        # FIXME: way too much state in view, refactor using MVC
        self.focused_tags: List[str] = []
        self.undo_tags: List[str] = []
        self.focused_items: List[SidebarItem] = []
        self.noselect_focused = False  # only expand and keyboard-focus, do not select
        self.expanded.connect(self.onExpansion)
        self.collapsed.connect(self.onCollapse)

        # Enable context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)

        # Enable drag-and-drop
        self.setDragEnabled(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.viewport().setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        # UI setup
        self._setupHotkeys()

    # Deferred init

    # This hacky approach is kept for compatibility with other add-ons.
    # Extending __init__ would require adding more init args, which in turn
    # would require overwriting setupSidebar, potentially causing more breakage

    def _deferredInit(self):
        """Put all init steps here require the presence self.browser
        Called after aqt.browser.Browser.setupSidebar
        """
        self._tagReplacer: TagReplacementMediator = TagReplacementMediator(
            self.browser.col
        )

    def setModel(self, model):
        """Put all init steps here that require the presence of self.model
        Called after aqt.browser.Browser.maybeRefreshSidebar"""
        # setModel is called by deferredDisplay, so it can be called after
        # browser has already been closed/deleted
        # FIXME: find proper solution
        if sip.isdeleted(self.browser):  # type: ignore
            return
        super().setModel(model)
        self.model().dataChanged.connect(self._onDataChanged)

    # Interactivity ###################

    def _setupHotkeys(self):
        QShortcut(
            QKeySequence(config["local"]["hotkeyRenameTag"]),
            self,
            activated=lambda: self._actOnSelectedItems("rename"),
        )  # type: ignore
        QShortcut(
            QKeySequence(f"Shift+{config['local']['hotkeyRenameTag']}"),
            self,
            activated=lambda: self._actOnSelectedItems("reorg"),
        )  # type: ignore
        QShortcut(
            QKeySequence(config["local"]["hotkeyDeleteTag"]),
            self,
            activated=lambda: self._actOnSelectedItems("delete"),
        )  # type: ignore

    def onContextMenu(self, pos: QPoint):
        """
        Draw context menu at position

        Arguments:
            pos {QPoint} -- Right-click position
        """

        gpos = self.mapToGlobal(pos)
        item = self.itemAt(pos)

        if not item:
            return

        selected_items = self._filterItems(
            self.selectedItems(), [SIDEBAR_ITEM_TYPE_TAG]
        )

        if not selected_items:
            return
        tag_state = user_data["tagState"].get(item.data, {})

        m = QMenu()

        if len(selected_items) == 1:
            m.addAction(
                f"Rename tag...\t{config['local']['hotkeyRenameTag']}",
                lambda: self._actOnSelectedItems("rename"),
            )
            if self._itemIsHierarchical(item, ignore_root=True):
                m.addAction(
                    "Reorganize hierarchy...\t{}".format(
                        f"Shift+{config['local']['hotkeyRenameTag']}"
                    ),
                    lambda: self._actOnSelectedItems("reorg"),
                )
        m.addAction(
            ngettext("Delete tag", "Delete tags", len(selected_items))
            + "\t{}".format(config["local"]["hotkeyDeleteTag"]),
            lambda: self._actOnSelectedItems("delete"),
        )

        m.addSeparator()
        pin_top_action = ("Pin to the top", lambda: self._actOnSelectedItems("pinTop"))
        pin_bottom_action = (
            "Pin to the bottom",
            lambda: self._actOnSelectedItems("pinBottom"),
        )
        if tag_state and "pinned" in tag_state:
            m.addAction("Unpin", lambda: self._actOnSelectedItems("unpin"))
            pinned_state = tag_state["pinned"]
            if pinned_state == PIN_STATE_BOTTOM:
                m.addAction(*pin_top_action)
            elif pinned_state == PIN_STATE_TOP:
                m.addAction(*pin_bottom_action)
        else:
            for action in (pin_top_action, pin_bottom_action):
                m.addAction(*action)

        submenu = m.addMenu("Set color")

        if tag_state and "color" in tag_state:
            m.addAction("Reset color", lambda: self._actOnSelectedItems("resetColor"))

        for label, code in (
            ("Green", "#008000"),
            ("Red", "#FF0000"),
            ("Blue", "#0000FF"),
        ):
            submenu.addAction(
                label, lambda code=code: self._actOnSelectedItems("setColor", code)
            )
        submenu.addAction(
            "Custom...", lambda: self._actOnSelectedItems("setColor", "custom")
        )

        m.addSeparator()
        m.addAction("Collapse all", self.collapseAll)
        m.addAction("Expand all", self.expandAll)

        m.addSeparator()
        m.addAction(
            "Filtered deck...", lambda: self._actOnSelectedItems("filteredDeck")
        )

        # Allow other add-on authors to modify the context menu:
        runHook("Browser.tagContextMenuEvent", self, m, item)
        m.exec_(gpos)

    def dropEvent(self, event: QDropEvent):
        """
        Custom QTreeWidget drop event handler

        Arguments:
            event {QDropEvent} -- Qt drop event
        """
        source_items = self.selectedItems()
        dropped_on_item = self.itemAt(event.pos())
        indicator_pos = self.dropIndicatorPosition()

        if (
            not source_items
            or not dropped_on_item
            or not self._filterItems([dropped_on_item], [SIDEBAR_ITEM_TYPE_TAG])
        ):
            event.setDropAction(Qt.IgnoreAction)
            return super().dropEvent(event)

        if indicator_pos == QAbstractItemView.OnItem:
            # released on top of other item
            target_item = dropped_on_item
        else:
            # released between items
            target_item = dropped_on_item.parentItem

        # Filter out invalid operations
        source_items = [i for i in source_items if i.parentItem != target_item]

        if not source_items:
            event.setDropAction(Qt.IgnoreAction)
            return super().dropEvent(event)

        self._repositionItems(source_items, target_item)

        return super().dropEvent(event)

    # QTreeWidget API

    def selectedItems(self) -> List[SidebarItem]:
        items = []
        for index in self.selectedIndexes():
            if not index.isValid():
                continue
            items.append(self.model().itemFromIndex(index))
        return items

    def itemAt(self, point: QPoint) -> Optional[SidebarItem]:
        index = self.indexAt(point)
        if not index.isValid():
            return
        return self.model().itemFromIndex(index)

    def itemBelow(self, item: SidebarItem) -> Optional[SidebarItem]:
        index = self.model().indexFromItem(item)
        below = self.indexBelow(index)
        return self.model().itemFromIndex(below)

    def itemAbove(self, item: SidebarItem) -> Optional[SidebarItem]:
        index = self.model().indexFromItem(item)
        below = self.indexAbove(index)
        return self.model().itemFromIndex(below)

    # slots

    def _onDataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex):
        item = self.model().itemFromIndex(topLeft)
        new_name = item.name
        self._renameItem(item, new_name)

    def onTagCollapse(self, expanded: bool, partial_tag: str):
        if config["local"]["hierarchyExpansionBehavior"] != "restore":
            return
        tag_state = user_data["tagState"]
        if partial_tag not in tag_state:
            tag_state[partial_tag] = {}
        tag_state[partial_tag]["expanded"] = expanded

    def onTagClick(self, item: SidebarItem, tag: str):
        """
        Set search filter for tag items depending on
        their level in hierarchy

        Arguments:
            item {SidebarItem} -- Sidebar item clicked on
            tag {str} -- Associated partial tag
        """
        if item.children:  # has children
            self.browser.setFilter(f'("tag:{tag}" or "tag:{tag}{SEPARATOR}*")')
        else:
            self.browser.setFilter("tag", tag)

    # Item helpers

    def _filterItems(self, items: List[SidebarItem], types: List[int]):
        return [item for item in items if getattr(item, "type", None) in types]

    def _itemIsHierarchical(self, item: SidebarItem, ignore_root: bool = False):
        # If item has a parent or children it's part of a hierarchy:
        if ignore_root and not item.parentItem and item.children:
            return False
        elif item.parentItem or item.children:
            return True
        return False

    def _itemNearestNeighbor(self, item: SidebarItem):
        if item.children:
            # TODO: determine next top-level item instead
            item_above = self.itemAbove(item)
            # Workaround: if top-most tag, and item above added by other add-on,
            # select item below
            if hasattr(item_above, "data"):
                return self.itemAbove(item)
            else:
                return self.itemBelow(item)
        else:
            return self.itemBelow(item) or self.itemAbove(item)

    # Called from user interactions ###################

    def _actOnSelectedItems(self, action: str, *args, **kwargs):
        """
        Determine data of currently selected item and perform
        provided action

        Arguments:
            action {str} -- Tag action to perform (rename/reorg/delete)
        """
        selected_items = self._filterItems(
            self.selectedItems(), [SIDEBAR_ITEM_TYPE_TAG]
        )

        if not selected_items:
            return

        if action == "rename":
            # (i.setSelected(False) for i in selected_items[1:])
            self.edit(self.selectedIndexes()[0])
        elif action == "reorg":
            # (i.setSelected(False) for i in selected_items[1:])
            self._reorganizeItem(selected_items[0])
        elif action == "delete":
            self._deleteItems(selected_items)
        elif action == "unpin":
            self._unpinItems(selected_items)
        elif action == "pinTop":
            self._pinItems(selected_items, PIN_STATE_TOP)
        elif action == "pinBottom":
            self._pinItems(selected_items, PIN_STATE_BOTTOM)
        elif action == "filteredDeck":
            self._createFilteredDeckFromItems(selected_items)
        elif action == "setColor":
            self._colorItems(selected_items, *args)
        elif action == "resetColor":
            self._uncolorItems(selected_items)

    # ITEM ACTIONS ###################

    # Called from _actOnSelectedItems ###################

    def _createFilteredDeckFromItems(self, items: List[SidebarItem]):
        subqueries = []
        for item in items:
            tag = item.data
            if item.children:
                subquery = f'("tag:{tag}" or "tag:{tag}{SEPARATOR}*")'
            else:
                subquery = f'"tag:{tag}"'
            subqueries.append(subquery)
        query = " ".join(subqueries)
        self.mw.onCram(query)

    def _pinItems(self, items: List[SidebarItem], mode: int):
        for item in items:
            self._onTagPin(item.data, mode)
        self.browser.maybeRefreshSidebar()

    def _unpinItems(self, items: List[SidebarItem]):
        for item in items:
            self._onTagUnpin(item.data)
        self.browser.maybeRefreshSidebar()

    def _colorItems(self, items: List[SidebarItem], color: str):
        if color == "custom":
            qcolor = QColorDialog.getColor()
            if not qcolor.isValid():
                return
            color = qcolor.name()
        for item in items:
            self._onTagColor(item.data, color)
        self.browser.maybeRefreshSidebar()

    def _uncolorItems(self, items: List[SidebarItem]):
        for item in items:
            self._onTagResetColor(item.data)
        self.browser.maybeRefreshSidebar()

    @browserEditorSaveThen
    def _deleteItems(self, items: List[SidebarItem]):
        tags = [i.name for i in items]

        if config["local"]["confirmItemDeletion"]:
            q = (
                "This will <b>delete</b> the following tags in <b>all of your notes.</b>:"
                f"<br><br><i>{'  '.join(tags)}</i><br><br>"
                "Please note that, in case of hierarchical tags, <b>all subtags</b> "
                "underneath each tag will also be removed for the respective tag tree!"
                "<br><br>Are you sure you want to proceed?"
            )

            if not askUser(q, parent=self.browser, title="Delete tags"):
                return

        neighbor = self._itemNearestNeighbor(items[0])
        # neighbor might have been added by other add-on (e.g. Customize Sidebar),
        # so be extra defensive:
        select_after = "" if not neighbor else getattr(neighbor, "data", "")

        action = "Delete tags"

        with resetBrowser(self.browser, action):
            # TODO: only call findReplaceTags once
            for idx, item in enumerate(items):
                tag = item.data
                is_hierarchy = self._itemIsHierarchical(item)
                self._tagReplacer.delete(tag, is_hierarchy)
                self.undo_tags.append(tag)
                self.browser.mw.progress.update(label=action, value=idx + 1)

            self.focused_tags.append(select_after)

    @browserEditorSaveThen
    def _renameItem(self, item: SidebarItem, text: str):
        query = None
        with resetBrowser(self.browser, "Rename Tag"):
            if self._itemIsHierarchical(item):
                mode = "renameHierarchy"
            else:
                mode = "rename"
            query = self._renameTag(item.data, text, mode)
        if query is not None:
            self._search(query)

    @browserEditorSaveThen
    def _reorganizeItem(self, item: SidebarItem) -> Optional[str]:
        user_input, ret = getText(
            "Please enter a new tag:",
            parent=self,
            title="Reorganize tag structure",
            default=item.data,
        )
        if not ret or not user_input:
            return

        query = None
        with resetBrowser(self.browser, "Reorganize Tag"):
            query = self._renameTag(item.data, user_input, "reorganize")

        if query is not None:
            self._search(query)

    # exclusively called from drag-and-drop operations

    @browserEditorSaveThen
    def _repositionItems(
        self, source_items: List[SidebarItem], target_item: SidebarItem
    ):
        target_is_root = not bool(target_item)
        target_tag = "" if target_is_root else target_item.data

        action = "Reposition items"

        new_tags = []
        with resetBrowser(self.browser, action, progress_max=len(source_items)):
            for idx, source_item in enumerate(source_items):
                if source_item.type != SIDEBAR_ITEM_TYPE_TAG:
                    continue
                source_tag = source_item.data

                result = self._tagReplacer.reposition(source_tag, target_tag)

                tag_state = user_data["tagState"]
                tag_state[result.tag] = tag_state.get(source_tag, {})
                if source_tag in tag_state:
                    del tag_state[source_tag]

                new_tags.append(result.tag)
                self.focused_tags.append(result.tag)
                self.undo_tags.append(source_tag)
                self.browser.mw.progress.update(label=action, value=idx + 1)

        if new_tags:
            query = " OR ".join(f'"tag:{tag}*"' for tag in new_tags)
            self._search(query)

    # TAG ACTIONS ###################

    # Called from item actions ###################

    def _renameTag(self, old: str, new: str, mode: str):
        func = getattr(self._tagReplacer, mode)
        result = func(old, new)
        # preserve focus
        self.focused_tags.append(result.tag)
        self.undo_tags.append(old)
        # migrate state
        if mode in ("rename", "renameHierarchy"):
            tag_state = user_data["tagState"]
            tag_state[result.tag] = tag_state.get(old, {})
            if old in tag_state:
                del tag_state[old]
        # updated search
        ast = "*" if mode in ("reorganize", "renameHierarchy") else ""
        new_search = f'"tag:{result.tag}{ast}"'
        return new_search

    def _onTagPin(self, tag: str, position: int):
        tag_state = user_data["tagState"]
        if tag not in tag_state:
            tag_state[tag] = {}
        tag_state[tag]["pinned"] = position
        self.focused_tags.append(tag)

    def _onTagUnpin(self, tag: str):
        tag_state = user_data["tagState"]
        if tag not in tag_state or "pinned" not in tag_state[tag]:
            return
        del tag_state[tag]["pinned"]

    def _onTagColor(self, tag: str, color: str):
        tag_state = user_data["tagState"]
        if tag not in tag_state:
            tag_state[tag] = {}
        tag_state[tag]["color"] = color
        self.focused_tags.append(tag)
        self.noselect_focused = True

    def _onTagResetColor(self, tag: str):
        tag_state = user_data["tagState"]
        if tag not in tag_state or "color" not in tag_state[tag]:
            return
        del tag_state[tag]["color"]
        self.focused_tags.append(tag)
        self.noselect_focused = True

    # Browser tie-in helpers

    def _search(self, query: str):
        self.browser.form.searchEdit.lineEdit().setText(query)
        self.browser.onSearchActivated()
