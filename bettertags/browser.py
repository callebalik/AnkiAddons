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

"""
Modifications to the card browser, precluding the sidebar
"""

from PyQt5.QtGui import QCursor, QKeySequence
from PyQt5.QtWidgets import QMenu

from anki.hooks import addHook, runHook, remHook, wrap
from anki.lang import ngettext
from anki.utils import ids2str
from aqt.browser import Browser
from aqt.qt import qtminor
from aqt.utils import showInfo, tooltip

from .config import config, user_data
from .consts import ADDON, is_new_anki
from .gui.findreplacetags import FindAndReplaceTagsDialog
from .gui.options import invokeOptionsDialog
from .helpers import resetBrowser
from .libaddon.anki.editor import widgetEditorSaveThen
from .libaddon.config.errors import ConfigNotLoadedError
from .tags import FindReplaceRequest, findReplaceTags, getSearchString

if is_new_anki:
    from .sidebar import initializeBrowserSidebar
else:
    from .sidebar_old import initializeBrowserSidebar


def getUserSelections(self, selected_nids):
    autocomplete_replace = self.col.tags.all()
    if selected_nids:
        autocomplete_find = set(
            self.col.tags.split(
                " ".join(
                    self.col.db.list(
                        "select distinct tags from notes where id in "
                        + ids2str(selected_nids)
                    )
                )
            )
        )
    else:
        autocomplete_find = autocomplete_replace

    dialog = FindAndReplaceTagsDialog(
        self,
        autocomplete_find,
        autocomplete_replace,
        count=len(selected_nids),
        total=self.col.noteCount(),
    )
    ret = dialog.exec_()

    if not ret:
        return False

    return dialog.getInputs()


@widgetEditorSaveThen
def onFindReplaceTags(self):
    """
    Call Find and Replace Dialog and pass
    settings on to doFindAndReplaceTags().

    self is an aqt.browser.Browser instance
    """
    selected_nids = self.selectedNotes()

    args = getUserSelections(self, selected_nids)

    if not args:
        return False
    elif not args["find"]:
        tooltip("No changes performed.", parent=self)
        return False

    nids = selected_nids if args.pop("limit") else []
    args["nids"] = nids
    args["search_str"] = getSearchString(args["find"], args["whole_tags"])

    changed = None
    with resetBrowser(self, "Find and Replace Tags"):
        request = FindReplaceRequest(**args)
        changed = findReplaceTags(self.col, request)

    if changed:
        new_search = getSearchString(args["replace"], args["whole_tags"])
        self.form.searchEdit.lineEdit().setText(new_search)
        self.onSearchActivated()

    changed = changed or 0
    if nids:
        text = ngettext(
            "%(a)d of %(b)d note updated", "%(a)d of %(b)d notes updated", len(nids)
        ) % {"a": changed, "b": len(nids)}
    else:
        text = ngettext("%(a)d note updated", "%(a)d notes updated", changed) % {
            "a": changed
        }

    showInfo(text, parent=self)


@widgetEditorSaveThen
def onRefreshTags(self):
    """
    Update tag database, removing unused notes and refreshing
    tag hierarchies
    """
    self.mw.col.tags.registerNotes()
    tooltip("Updated tag database.")


# Menu entries


def setupMenu(self):
    """
    Add menu entries to Browser

    self is an aqt.browser.Browser instance
    """

    try:
        # The Tags menu is used by several of my add-ons,
        # so we check for its existence first:
        menu = self.menuTags
    except AttributeError:
        # Tags menu does not exist, so create it from scratch
        self.menuTags = QMenu("Better&Tags")
        self.menuBar().insertMenu(self.mw.form.menuTools.menuAction(), self.menuTags)

    menu = self.menuTags
    menu.addSeparator()

    # Add submenus, assign them shortcuts, and connect them
    # to their respective functions
    a = menu.addAction("Find and Replace Tags...")
    a.setShortcut(QKeySequence(config["local"]["hotkeyFindReplace"]))
    a.triggered.connect(lambda _: self.onFindReplaceTags())

    a = menu.addAction("Refresh Tag List...")
    a.setShortcut(QKeySequence(config["local"]["hotkeyRefreshTags"]))
    a.triggered.connect(lambda _: self.onRefreshTags())

    a = menu.addAction("Open &Settings...")
    a.triggered.connect(lambda _: invokeOptionsDialog(self))  # type: ignore


# TODO: Submit pull request to dae/anki to allow add-on authors to add
# menu actions without overwriting onContextMenu


def onResultListContextMenuWrap(self, _point):
    """
    Patch aqt.browser.Browser.onContextMenu to add "Find and Replace
    Tags" action to the result list context menu

    self is an aqt.browser.Browser instance
    """
    m = QMenu()
    for act in self.form.menu_Cards.actions():
        m.addAction(act)
    m.addSeparator()
    for act in self.form.menu_Notes.actions():
        m.addAction(act)
    # mod start
    onResultListContextMenu(self, m)
    # mod stop
    if qtminor < 10:
        return
    for act in m.actions():
        act.setShortcutVisibleInContextMenu(True)
    m.exec_(QCursor.pos())


def onResultListContextMenu(self: Browser, menu: QMenu):
    menu.addSeparator()
    a = menu.addAction("Find and Replace Tags...")
    a.setShortcut(QKeySequence(config["local"]["hotkeyFindReplace"]))
    a.triggered.connect(lambda _: self.onFindReplaceTags())
    runHook("Browser.contextMenuEvent", self, menu)



# Undo handling and cleanup

def onRevertedState(browser, name):
    if name.startswith(ADDON.MODULE):
        browser.maybeRefreshSidebar()

def onBrowserInit(browser, *args, **kwargs):
    # Handle undo
    addHook("revertedState", browser._onRevertedState)

def onBrowserClose(browser, *args, **kwargs):
    remHook("revertedState", browser._onRevertedState)
    try:
        user_data.save()
    except ConfigNotLoadedError:  # already saved
        pass


def initializeBrowser():
    """Add our own methods to the Browser class, so that we can call them as
    instance methods, *and* modify existing methods with our own changes
    """

    # Browser sidebar
    if config["local"]["enableSidebarModifications"]:
        initializeBrowserSidebar()

    # Other browser components
    Browser.onFindReplaceTags = onFindReplaceTags
    Browser.onRefreshTags = onRefreshTags
    addHook("browser.setupMenus", setupMenu)

    if is_new_anki:
        addHook("browser.onContextMenu", onResultListContextMenu)
    else:
        Browser.onContextMenu = onResultListContextMenuWrap

    # Undo handling and cleanup
    Browser._onRevertedState = onRevertedState
    Browser.__init__ = wrap(Browser.__init__, onBrowserInit, "after")
    Browser._closeWindow = wrap(Browser._closeWindow, onBrowserClose, "after")
