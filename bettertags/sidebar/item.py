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

from typing import List, Optional, Callable, Iterator

from .const import SIDEBAR_ITEM_TYPE_DEFAULT
from itertools import chain


class SidebarItem:

    __slots__ = (
        "name",
        "icon",
        "onClick",
        "onExpanded",
        "expanded",
        "type",
        "data",
        "draggable",
        "editable",
        "fg_color",
        "bg_color",
        "font_weight",
        "children",
        "parentItem",
        "tooltip",
    )

    def __init__(
        self,
        name: str,
        icon: str,
        onClick: Callable[[], None] = None,
        onExpanded: Callable[[bool], None] = None,
        expanded: bool = False,
        type: int = SIDEBAR_ITEM_TYPE_DEFAULT,
        data: str = "",
        draggable: bool = False,
        editable: bool = False,
        fg_color: Optional[str] = None,
        bg_color: Optional[str] = None,
        font_weight: Optional[int] = None,
    ) -> None:
        self.name = name
        self.icon = icon
        self.onClick = onClick
        self.onExpanded = onExpanded
        self.expanded = expanded
        self.type = type
        self.data = data
        self.draggable = draggable
        self.editable = editable
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.font_weight = font_weight
        self.children: List["SidebarItem"] = []
        self.parentItem: Optional[SidebarItem] = None
        self.tooltip: Optional[str] = None

    def __iter__(self) -> Iterator["SidebarItem"]:
        for item in chain(*map(iter, self.children)):
            yield item
        yield self

    def addChild(self, cb: "SidebarItem") -> None:
        self.children.append(cb)
        cb.parentItem = self

    def rowForChild(self, child: "SidebarItem") -> Optional[int]:
        try:
            return self.children.index(child)
        except ValueError:
            return None

    def expandTree(self, expanded=True):
        item = self.parentItem
        while item:
            item.expanded = expanded
            item = item.parentItem

    def childNumber(self):
        if self.parentItem:
            return self.parentItem.children.index(self)
        return 0

    def hierarchyList(self) -> List["SidebarItem"]:
        family = []
        item = self
        while item:
            family.append(item)
            item = item.parentItem
        family.reverse()
        return family
