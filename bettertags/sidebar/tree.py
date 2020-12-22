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


from typing import Dict

from PyQt5.QtGui import QFont

from aqt.browser import Browser

from ..config import config, user_data
from .const import PIN_STATE_BOTTOM, PIN_STATE_TOP, SEPARATOR, SIDEBAR_ITEM_TYPE_TAG
from .item import SidebarItem
from .view import SidebarTreeView

PINNED_PREFIXES = {
    PIN_STATE_TOP: "\u0001",
    PIN_STATE_BOTTOM: "\u9999"
}

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


def userTagTree(browser: Browser, root: SidebarItem):
    """
    Add tag tree items to the browse sidebar
    (hierarchical)

    Modified version of aqt.browser.Browser.userTagTree

    Arguments:
        root {QTreeWidget/CustomSidebarItem} -- Parent Qt element to add
                                              items to
    """
    #
    sidebar: SidebarTreeView = browser.sidebarTree

    # get tags & prepare tag tree dict
    tag_state_conf = user_data["tagState"]
    expansion_behavior = config["local"]["hierarchyExpansionBehavior"]

    tags = sorted(browser.col.tags.all(), key=lambda tag: sortTags(tag, tag_state_conf))
    tags_tree = {}

    # get tags that are to be expanded / selected
    focus_tags = sidebar.focused_tags or sidebar.undo_tags
    to_select = []
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

            if tags_tree.get(partial_tag):  # hierarchy already processed
                continue

            if idx == 0:
                parent = root
            else:
                parent_tag = SEPARATOR.join(components[0:idx])
                parent = tags_tree[parent_tag]

            # Create item, add it to the parent, set properties
            item = SidebarItem(
                c,
                ":/icons/tag.svg",
                type=SIDEBAR_ITEM_TYPE_TAG,
                data=partial_tag,
                draggable=True,
                editable=True,
            )
            item.onClick = lambda i=item, t=partial_tag: sidebar.onTagClick(i, t)
            item.onExpanded = lambda expanded, t=partial_tag: sidebar.onTagCollapse(
                expanded, t
            )

            tag_state = tag_state_conf.get(partial_tag, {})

            expand = False
            if partial_tag in focus_tags:
                expand = True
                if tag_state.get("expanded"):
                    item.expanded = True
                to_select.append(item)
            elif expansion_behavior == "expand_all" or (
                expansion_behavior == "restore" and tag_state.get("expanded")
            ):
                item.expanded = True

            pinned = tag_state.get("pinned")
            if pinned:
                if pinned == PIN_STATE_TOP:
                    item.font_weight = QFont.Bold
                elif pinned == PIN_STATE_BOTTOM:
                    item.font_weight = QFont.Thin
                    item.fg_color = "#828282"

            # overrules pinned color:
            item.fg_color = tag_state.get("color", item.fg_color)

            parent.addChild(item)
            if expand and not parent.expanded:
                item.expandTree()

            tags_tree[partial_tag] = item

    # reset tags to expand
    if sidebar.focused_tags:
        sidebar.focused_tags = []
    elif sidebar.undo_tags:
        sidebar.undo_tags = []

    # Pass on data on selections
    sidebar.focused_items = to_select
