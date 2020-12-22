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

from typing import TYPE_CHECKING

from PyQt5.QtCore import (
    QAbstractItemModel,
    QItemSelectionModel,
    QModelIndex,
    Qt,
    QVariant,
)
from PyQt5.QtGui import QColor, QFont, QIcon
from PyQt5.QtWidgets import QAbstractItemView

try:
    from PyQt5 import sip
except ImportError:
    import sip  # type: ignore

from aqt import browser

from .item import SidebarItem

if TYPE_CHECKING:
    from .view import SidebarTreeView

try:
    from aqt.theme import theme_manager
except (ImportError, ModuleNotFoundError):
    theme_manager = None

if theme_manager:

    def iconFromRef(browser: browser.Browser, iconRef: str) -> QIcon:
        return theme_manager.icon_from_resources(iconRef)


else:

    def iconFromRef(browser: browser.Browser, iconRef: str) -> QIcon:
        return browser.iconFromRef(iconRef)


class SidebarModel(browser.SidebarModel):

    # Qt API
    ######################################################################

    def itemFromIndex(self, index: QModelIndex) -> SidebarItem:
        return index.internalPointer()

    def indexFromItem(self, item: SidebarItem) -> QModelIndex:
        return self.createIndex(item.childNumber(), 0, item)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> QVariant:
        if not index.isValid():
            return QVariant()

        if role not in (
            Qt.DisplayRole,
            Qt.EditRole,
            Qt.DecorationRole,
            Qt.ToolTipRole,
            Qt.ForegroundRole,
            Qt.BackgroundRole,
            Qt.FontRole,
        ):
            return QVariant()

        item: SidebarItem = index.internalPointer()

        try:
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return QVariant(item.name)
            elif role == Qt.ToolTipRole:
                return QVariant(item.tooltip)
            elif role == Qt.DecorationRole:
                return QVariant(iconFromRef(self, item.icon))
            elif role == Qt.ForegroundRole and item.fg_color:
                return QVariant(QColor(item.fg_color))
            elif role == Qt.BackgroundRole and item.bg_color:
                return QVariant(QColor(item.bg_color))
            elif role == Qt.FontRole and item.font_weight:
                font = QFont()
                font.setWeight(item.font_weight)
                return QVariant(font)
            else:
                return QVariant()
        except AttributeError:
            # workaround for add-ons using their own SidebarItems
            return QVariant()

    def setData(
        self, index: QModelIndex, value: QVariant, role: int = Qt.EditRole
    ) -> bool:
        if not index.isValid():
            return False

        item: SidebarItem = index.internalPointer()

        if role == Qt.EditRole:
            if not value or value == item.name or " " in value:
                return False
            item.name = value
        else:
            return False

        self.dataChanged.emit(index, index)

        return True

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        flags = QAbstractItemModel.flags(self, index)
        if not index.isValid():
            return Qt.ItemIsDropEnabled  # drop indicator on root item

        item: SidebarItem = index.internalPointer()

        try:
            if item.draggable:
                flags = flags | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

            if item.editable:
                flags = flags | Qt.ItemIsEditable
        except AttributeError:
            # workaround for add-ons using their own SidebarItems
            return flags

        return flags

    def supportedDropActions(self) -> Qt.DropAction:
        return Qt.MoveAction

    # Helpers
    ######################################################################

    def expandWhereNeccessary(self, tree: "SidebarTreeView") -> None:
        # FIXME: find a proper solution
        if sip.isdeleted(tree):  # type: ignore
            return
        
        super().expandWhereNeccessary(tree)

        # Set selection
        selection_model = tree.selectionModel()
        selection_model.clear()

        # need to set current item first, for whatever reason
        if tree.focused_items:
            current_index = self.indexFromItem(tree.focused_items[-1])
            tree.setCurrentIndex(current_index)
            selection_model.select(current_index, QItemSelectionModel.Current)

            # conditionally scroll viewport around edges
            tree_rect = tree.rect()
            item_rect = tree.visualRect(current_index)
            if (tree_rect.bottomLeft().y() - item_rect.bottomLeft().y()) < 10 or (
                item_rect.topRight().y() - tree_rect.topRight().y()
            ) < 10:
                tree.scrollTo(current_index, QAbstractItemView.PositionAtCenter)

        if tree.noselect_focused:
            selection_model.clearSelection()  # keep keyboard-focused but not selected
        else:
            for item in tree.focused_items:
                index = self.indexFromItem(item)
                selection_model.select(index, QItemSelectionModel.Select)

        # Reset
        tree.focused_items = []
        tree.noselect_focused = False
