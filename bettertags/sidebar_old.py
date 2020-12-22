# -*- coding: utf-8 -*-

# BetterTags Add-on for Anki
#
# Copyright (C) 2017-2020  Aristotelis P. <https//glutanimate.com/>
# Copyright (C) 2014       Patrice Neff <http://patrice.ch/>
#                          (Hierarchical Tags)
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

"""
Modifications to the card browser sidebar
"""

from typing import Callable, Dict, List, Optional, Union

from PyQt5.QtCore import QModelIndex, QPoint, Qt, pyqtSlot
from PyQt5.QtGui import QBrush, QColor, QDropEvent, QFont, QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QColorDialog,
    QMenu,
    QShortcut,
    QTreeWidget,
    QTreeWidgetItem,
)

from anki.hooks import runHook, wrap
from anki.lang import ngettext
from aqt.browser import Browser
from aqt.utils import askUser, getText

from .config import config, user_data
from .helpers import browserEditorSaveThen, resetBrowser
from .mediator import TagReplacementMediator

SEPARATOR = config["local"]["hierarchicalTagsSeparator"]
TAGWIDGETITEM_TYPE_DEFAULT = 0
ITEM_TYPE_TAG = 1

TAG_PINNED_TOP = 1
TAG_PINNED_BOTTOM = 2

TAG_ICON = ":/icons/tag.svg"

TYPE_TREE_OR_ITEM = Union[QTreeWidget, QTreeWidgetItem]

# Hierarchical Tags ###################

PINNED_PREFIXES = {TAG_PINNED_TOP: "\u0001", TAG_PINNED_BOTTOM: "\u9999"}


def sortTags(tag: str, tag_state: Dict[str, dict]) -> str:
    # pin by hierarchy
    components = tag.split(SEPARATOR)

    substring = []
    for idx, c in enumerate(components):
        substring.append(c)
        subtag = SEPARATOR.join(substring)
        pinned = tag_state.get(subtag, {}).get("pinned")
        if not pinned:
            continue

        components[idx] = PINNED_PREFIXES[pinned] + components[idx]

        return SEPARATOR.join(components)

    return tag


def hierarchicalUserTagTree(browser: Browser, root: TYPE_TREE_OR_ITEM):
    """
    Add tag tree items to the browse sidebar
    (hierarchical)

    Modified version of aqt.browser.Browser.userTagTree

    Arguments:
        root {QTreeWidget/SidebarItem} -- Parent Qt element to add
                                              items to
    """
    #
    sidebar = browser.sidebarTree

    # get tags & prepare tag tree dict
    tag_state_conf = user_data["tagState"]
    expansion_behavior = config["local"]["hierarchyExpansionBehavior"]

    tags = sorted(browser.col.tags.all(), key=lambda tag: sortTags(tag, tag_state_conf))
    tags_tree = {}

    # get tags that are to be expanded / selected
    focus_tags = sidebar.focused_tags or sidebar.undo_tags
    last_selected = None

    # for each tag in collection
    for t in tags:
        if t.lower() == "marked" or t.lower() == "leech":
            # skip over Anki-reserved tags
            continue

        components = t.split(SEPARATOR)
        # for each component in hierarchical tag
        for idx, c in enumerate(components):
            # tag hierarchy up to the current component:
            partial_tag = SEPARATOR.join(components[0 : idx + 1])

            tag_state = tag_state_conf.get(partial_tag, {})

            if tags_tree.get(partial_tag):  # hierarchy already processed
                continue

            if idx == 0:
                parent = root
            else:
                parent_tag = SEPARATOR.join(components[0:idx])
                parent = tags_tree[parent_tag]

            # Create item, add it to the parent, set properties
            item = SidebarItem(parent, c, None, draggable=True, editable=True)
            item.onclick = lambda i=item, t=partial_tag: sidebar.onTagClick(i, t)
            item.oncollapse = lambda i=item, t=partial_tag: sidebar.onTagCollapse(i, t)
            item.setIcon(0, QIcon(TAG_ICON))
            item.itype = ITEM_TYPE_TAG
            item.idata = partial_tag

            if partial_tag in focus_tags:
                sidebar.expandItem(item)
                item.setSelected(True)
                last_selected = item
                if tag_state.get("expanded"):
                    item.setExpanded(True)
            elif expansion_behavior == "expand_all" or (
                expansion_behavior == "restore" and tag_state.get("expanded")
            ):
                item.setExpanded(True)

            pinned = tag_state.get("pinned")
            if pinned:
                if pinned == TAG_PINNED_TOP:
                    sidebar.setHighlight(item, weight=QFont.Bold)
                elif pinned == TAG_PINNED_BOTTOM:
                    sidebar.setHighlight(item, weight=QFont.Thin, color="#8C8C8C")

            color = tag_state.get("color")
            if color:
                sidebar.setHighlight(item, color=color)

            tags_tree[partial_tag] = item

    if last_selected:
        # scroll, center, and select
        root.scrollToItem(last_selected, QAbstractItemView.PositionAtCenter)
        if len(focus_tags) == 1:
            root.setCurrentItem(last_selected, 0)

    # reset tags to expand
    if sidebar.focused_tags:
        sidebar.focused_tags = []
    elif sidebar.undo_tags:
        sidebar.undo_tags = []


class SidebarItem(Browser.CallbackItem):
    """
    Initiliazes a browse sidebar QTreeWidgetItem with custom
    properties and methods

    Modified version of aqt.browser.Browser.CallbackItem

    Arguments:
        root {QTreeWidget/QTreeWidgetItem} -- Parent Qt element
        name {str} -- User-visible name
        onclick {function} -- Function executed upon left-clicking
                              on the item

    Keyword Arguments:
        oncollapse {function} -- Function executed when item is collapsed
                                 (default: {None})
        expanded {bool} -- Whether or not to expand item (default: {False})
        draggable {bool} -- Whether or not item should be draggable
                            (default: {False})
        itype {int} -- Item type. 0 for default item. 1 for tag item.
                       (default: {TAGWIDGETITEM_TYPE_DEFAULT})
        idata {str} -- Extra data associated with the item, e.g. the
                       partial tag in case of hierarchical tags (default: {""})
    """

    def __init__(
        self,
        root: TYPE_TREE_OR_ITEM,
        name: str,
        onclick: Optional[Callable] = None,
        oncollapse: Optional[Callable] = None,
        expanded: bool = False,
        draggable: bool = False,
        editable: bool = False,
        itype: int = TAGWIDGETITEM_TYPE_DEFAULT,
        idata: str = "",
    ):
        super().__init__(root, name, onclick, oncollapse=oncollapse, expanded=expanded)

        # Create additional properties for better interop with other parts of the add-on
        self.itype = itype
        self.idata = idata

        self.setDraggable(draggable)
        self.setEditable(editable)

    def setDraggable(self, draggable: bool):
        """
        Toggle between draggable states

        Arguments:
            draggable {boolean} -- Whether or not to enable dragging for item
        """
        if draggable:
            self.setFlags(self.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        else:
            self.setFlags(self.flags() & ~Qt.ItemIsDragEnabled & ~Qt.ItemIsDropEnabled)

    def setEditable(self, editable: bool):
        if editable:
            self.setFlags(self.flags() | Qt.ItemIsEditable)
        else:
            self.setFlags(self.flags() & ~Qt.ItemIsEditable)


class CustomSidebarTreeWidget(Browser.SidebarTreeWidget):
    def __init__(self):
        super().__init__()
        self.browser: Browser = None

        self.focused_tags: List[str] = []
        self.undo_tags: List[str] = []
        self.focused_items: List[SidebarItem] = []
        self.noselect_focused = False  # only expand and keyboard-focus, do not select

        # Enable context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.onContextMenu)

        # Enable drag-and-drop
        self.setDragEnabled(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.viewport().setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        # UI setup
        self._setupHotkeys()
        self.model().dataChanged.connect(self._onModelDataChanged)

    def _setupTagReplacer(self):
        self._tagReplacer: TagReplacementMediator = TagReplacementMediator(
            self.browser.col
        )

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

        selected_items = self._filterItems(self.selectedItems(), [ITEM_TYPE_TAG])

        if not selected_items:
            return
        tag_state = user_data["tagState"].get(item.idata, {})

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
            if pinned_state == TAG_PINNED_BOTTOM:
                m.addAction(*pin_top_action)
            elif pinned_state == TAG_PINNED_TOP:
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
        dropped_on_item = self.itemFromIndex(self.indexAt(event.pos()))
        indicator_pos = self.dropIndicatorPosition()

        event.setDropAction(Qt.IgnoreAction)

        if not self._filterItems([dropped_on_item], [ITEM_TYPE_TAG]):
            return super().dropEvent(event)

        if indicator_pos == QAbstractItemView.OnItem:
            # released on top of other item
            target_item = dropped_on_item
        else:
            # released between items
            target_item = dropped_on_item.parent()

        # Filter out invalid operations
        source_items = [i for i in source_items if i.parent() != target_item]

        if not source_items:
            return super().dropEvent(event)

        self._repositionItems(source_items, target_item)

        return super().dropEvent(event)

    # Slots ###################

    @pyqtSlot(QModelIndex, QModelIndex, "QVector<int>")
    def _onModelDataChanged(
        self, topLeft: QModelIndex, bottomRight: QModelIndex, roles: List[int]
    ):
        if not roles or Qt.EditRole not in roles:
            return
        item = self.itemFromIndex(topLeft)
        new_name = item.text(0)
        self._renameItem(item, new_name)

    def onTagCollapse(self, item: SidebarItem, partial_tag: str):
        if config["local"]["hierarchyExpansionBehavior"] != "restore":
            return
        tag_state = user_data["tagState"]
        if partial_tag not in tag_state:
            tag_state[partial_tag] = {}
        tag_state[partial_tag]["expanded"] = item.isExpanded()

    def onTagClick(self, item: SidebarItem, tag: str):
        """
        Set search filter for tag items depending on
        their level in hierarchy

        Arguments:
            item {SidebarItem} -- Sidebar item clicked on
            tag {str} -- Associated partial tag
        """
        if item.childCount():  # has children
            self.browser.setFilter(f'("tag:{tag}" or "tag:{tag}{SEPARATOR}*")')
        else:
            self.browser.setFilter("tag", tag)

    def setHighlight(
        self, item: SidebarItem, weight: QFont.Weight = None, color: str = None
    ):
        """change font weight and color of tree items"""
        if weight:
            font = item.font(0)
            font.setWeight(weight)
            item.setFont(0, font)
        if color:
            item.setForeground(0, QBrush(QColor(color)))

    def expandItem(self, item: SidebarItem):
        parent = item.parent()
        if parent:
            parent.setExpanded(True)
            self.expandItem(parent)

    # Item helpers ###################

    def _filterItems(self, items: List[SidebarItem], types: List[int]):
        return [item for item in items if getattr(item, "itype", None) in types]

    def _itemIsHierarchical(self, item: SidebarItem, ignore_root: bool = False):
        # If item has a parent or children it's part of a hierarchy:
        if ignore_root and not item.parent() and item.childCount():
            return False
        elif item.parent() or item.childCount():
            return True
        return False

    def _itemNearestNeighbor(self, item: SidebarItem):
        if item.childCount():
            # TODO: determine next top-level item instead
            return self.itemAbove(item)
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
        selected_items = self._filterItems(self.selectedItems(), [ITEM_TYPE_TAG])

        if not selected_items:
            return

        if action == "rename":
            (i.setSelected(False) for i in selected_items[1:])
            self.editItem(selected_items[0])
        elif action == "reorg":
            (i.setSelected(False) for i in selected_items[1:])
            self._reorganizeItem(selected_items[0])
        elif action == "delete":
            self._deleteItems(selected_items)
        elif action == "unpin":
            self._unpinItems(selected_items)
        elif action == "pinTop":
            self._pinItems(selected_items, TAG_PINNED_TOP)
        elif action == "pinBottom":
            self._pinItems(selected_items, TAG_PINNED_BOTTOM)
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
            tag = item.idata
            if item.childCount():
                subquery = f'("tag:{tag}" or "tag:{tag}{SEPARATOR}*")'
            else:
                subquery = f'"tag:{tag}"'
            subqueries.append(subquery)
        query = " ".join(subqueries)
        self.mw.onCram(query)

    def _pinItems(self, items: List[SidebarItem], mode: int):
        for item in items:
            self._onTagPin(item.idata, mode)
        self.browser.buildTree()

    def _unpinItems(self, items: List[SidebarItem]):
        for item in items:
            self._onTagUnpin(item.idata)
        self.browser.buildTree()

    def _colorItems(self, items: List[SidebarItem], color: str):
        if color == "custom":
            qcolor = QColorDialog.getColor()
            if not qcolor.isValid():
                return
            color = qcolor.name()
        for item in items:
            self._onTagColor(item.idata, color)
        self.browser.buildTree()

    def _uncolorItems(self, items: List[SidebarItem]):
        for item in items:
            self._onTagResetColor(item.idata)
        self.browser.buildTree()

    @browserEditorSaveThen
    def _deleteItems(self, items: List[SidebarItem]):

        tags = [i.text(0) for i in items]

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
        select_after = "" if not neighbor else neighbor.text(0) or ""

        action = "Delete tags"

        with resetBrowser(self.browser, action):
            # TODO: only call findReplaceTags once
            for idx, item in enumerate(items):
                tag = item.idata
                is_hierarchy = self._itemIsHierarchical(item)
                self.undo_tags.append(tag)
                self._tagReplacer.delete(tag, is_hierarchy)
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
            query = self._renameTag(item.idata, text, mode)
        if query is not None:
            self._search(query)

    @browserEditorSaveThen
    def _reorganizeItem(self, item: SidebarItem) -> Optional[str]:
        user_input, ret = getText(
            "Please enter a new tag:",
            parent=self,
            title="Reorganize tag structure",
            default=item.idata,
        )
        if not ret or not user_input:
            return

        query = None
        with resetBrowser(self.browser, "Reorganize Tag"):
            query = self._renameTag(item.idata, user_input, "reorganize")

        if query is not None:
            self._search(query)

    # exclusively called from drag-and-drop operations

    @browserEditorSaveThen
    def _repositionItems(
        self, source_items: List[SidebarItem], target_item: SidebarItem
    ):
        target_is_root = not bool(target_item)
        target_tag = "" if target_is_root else target_item.idata

        action = "Reposition items"

        new_tags = []
        with resetBrowser(self.browser, action, progress_max=len(source_items)):
            for idx, source_item in enumerate(source_items):
                if source_item.itype != ITEM_TYPE_TAG:
                    continue
                source_tag = source_item.idata

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
        # preserve state
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

    # Browser tie-in helpers ###################

    def _search(self, query: str):
        self.browser.form.searchEdit.lineEdit().setText(query)
        self.browser.onSearchActivated()


def onSetupSidebar(browser: Browser):
    browser.sidebarTree.browser = browser
    browser.sidebarTree._setupTagReplacer()


def onBuildTree(browser: Browser, _old: Callable):
    browser.sidebarTree.blockSignals(True)
    _old(browser)
    browser.sidebarTree.blockSignals(False)


def initializeBrowserSidebar():
    Browser.setupSidebar = wrap(Browser.setupSidebar, onSetupSidebar, "after")
    Browser.SidebarTreeWidget = CustomSidebarTreeWidget
    Browser.CallbackItem = SidebarItem
    Browser._userTagTree = hierarchicalUserTagTree
    Browser.buildTree = wrap(Browser.buildTree, onBuildTree, "around")
