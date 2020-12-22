# -*- coding: utf-8 -*-

# Search Everywhere - Ctrl+F Find Add-on for Anki
#
# Copyright (C) 2017-2020  Aristotelis P. <https://glutanimate.com/>
# Copyright (C) 2019  ijgnd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from typing import Optional, List, Tuple

from PyQt5.QtCore import QObject, Qt, QTimer
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEnginePage  # type: ignore
from PyQt5.QtWidgets import (
    QDockWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QShortcut,
    QWidget,
)

from anki.hooks import addHook, wrap
from aqt.browser import Browser
from aqt.editor import Editor
from aqt.main import AnkiQt

from .config import config


HOTKEY_SEARCH = config["local"]["hotkey_search"]
HOTKEY_SEARCH_BROWSER = config["local"]["hotkey_search_browser"]
HOTKEY_NEXT = config["local"]["hotkey_next_match"]
HOTKEY_PREVIOUS = config["local"]["hotkey_previous_match"]

# Reviewer

# TODO: Explore unifying modifications by switching to a
#       widget similar to the one in the Editor


class ReviewerSearchDock(QObject):
    """Creates a search dock for the main window"""

    def __init__(self, mw: AnkiQt):
        super().__init__(parent=mw)
        self.mw = mw
        self.dock: Optional[QDockWidget] = None
        self.widget: Optional[QWidget] = None
        self.shown: bool = False

    def setupWidget(self):
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        widget.searchEdit = QLineEdit()
        widget.searchNxt = QPushButton("∨")
        widget.searchPrv = QPushButton("∧")
        for i in (widget.searchEdit, widget.searchNxt, widget.searchPrv):
            layout.addWidget(i)
        return widget

    def setupDock(self):
        dock = QDockWidget("", self.mw)
        dock.setObjectName("SearchDock")
        dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        dock.setFeatures(QDockWidget.DockWidgetClosable)
        dock.setTitleBarWidget(QWidget(dock))
        return dock

    def setupEvents(self):
        self.widget.searchNxt.clicked.connect(lambda _: self.findText(0))
        self.widget.searchPrv.clicked.connect(lambda _: self.findText(1))
        if self.dock:
            t = QShortcut(QKeySequence("Esc"), self.dock)
            t.activated.connect(self.hide)
            t = QShortcut(QKeySequence("Ctrl+Return"), self.dock)
            t.activated.connect(self.widget.searchNxt.animateClick)
            t = QShortcut(QKeySequence("Shift+Return"), self.dock)
            t.activated.connect(self.widget.searchNxt.animateClick)

        t = QShortcut(QKeySequence(HOTKEY_NEXT), self.mw)
        t.activated.connect(self.widget.searchNxt.animateClick)
        t = QShortcut(QKeySequence(HOTKEY_PREVIOUS), self.mw)
        t.activated.connect(self.widget.searchPrv.animateClick)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.findText(0))

        self.widget.searchEdit.textEdited.connect(lambda: self.timer.start())

    def showOrFocus(self):
        if not self.shown:
            self.show()
        else:
            self.widget.searchEdit.setFocus()
            self.widget.searchEdit.selectAll()

    def show(self):
        if not self.dock:
            self.dock = self.setupDock()
            self.widget = self.setupWidget()
            self.dock.setWidget(self.widget)
            self.setupEvents()
            self.mw.addDockWidget(Qt.BottomDockWidgetArea, self.dock)
        self.dock.show()
        self.widget.searchEdit.setFocus()
        self.widget.searchEdit.selectAll()
        self.shown = True

    def hide(self):
        if self.dock:
            self.dock.hide()
            self.shown = False

    def toggle(self):
        if self.shown:
            self.hide()
        else:
            self.show()

    def findText(self, direction: int):
        if not self.widget:
            return
        text = self.widget.searchEdit.text()
        # for an explanation see below at EditorSearchWidget.findText
        if direction == 1:
            options = QWebEnginePage.FindBackward
            self.mw.web.findText(text, options)
        else:
            self.mw.web.findText(text)


def initialize_reviewer(mw):
    mw._search_dock = ReviewerSearchDock(mw)
    shortcut = QShortcut(QKeySequence(HOTKEY_SEARCH), mw)
    shortcut.activated.connect(mw._search_dock.showOrFocus)


# Editor

# We have to create a widget for the Editor because docks
# are only supported for QMainWindows


class EditorSearchWidget(QWidget):
    """Creates a search widget for the Editor"""

    def __init__(self, editor: Editor):
        parent: QWidget = editor.parentWindow
        super().__init__(parent=parent)
        self.editor = editor
        self.setupWidgets()
        self.setupEvents()
        QWidget.hide(self)

    def setupWidgets(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.searchEdit: QLineEdit = QLineEdit()
        self.searchNxt: QPushButton = QPushButton("∨")
        self.searchPrv: QPushButton = QPushButton("∧")
        for i in (self.searchEdit, self.searchNxt, self.searchPrv):
            layout.addWidget(i)

    def setupEvents(self):
        self.searchNxt.clicked.connect(lambda _: self.findText(0))
        self.searchPrv.clicked.connect(lambda _: self.findText(1))
        t = QShortcut(QKeySequence("Esc"), self)
        t.activated.connect(self.hide)
        t = QShortcut(QKeySequence("Return"), self)
        t.activated.connect(self.searchNxt.animateClick)
        t = QShortcut(QKeySequence("Shift+Return"), self)
        t.activated.connect(self.searchNxt.animateClick)
        t = QShortcut(QKeySequence(HOTKEY_NEXT), self)
        t.activated.connect(self.searchNxt.animateClick)
        t = QShortcut(QKeySequence(HOTKEY_PREVIOUS), self)
        t.activated.connect(self.searchPrv.animateClick)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.findText(0))
        self.searchEdit.textEdited.connect(lambda: self.timer.start())

    def showOrFocus(self):
        if not self.isVisible():
            self.show()
        self.searchEdit.setFocus()
        self.searchEdit.selectAll()

    def hide(self):
        self.editor.web.setFocus()
        if self.editor.currentField is not None:
            self.editor.web.eval("focusField(%d);" % self.editor.currentField)
        QWidget.hide(self)

    def findText(self, direction: int):
        text = self.searchEdit.text()
        if direction == 1:
            options = QWebEnginePage.FindBackward
            self.editor.web.findText(text, options)
        else:
            self.editor.web.findText(text)


def on_editor_did_init(editor: Editor):
    """Add search widget after tag widget"""
    editor._search_widget = EditorSearchWidget(editor)  # type: ignore
    editor.outerLayout.addWidget(editor._search_widget)  # type: ignore


def on_setup_editor_shortcuts(cuts: List[Tuple], editor: Editor):
    if not isinstance(editor.parentWindow, Browser):
        # AddCards or EditCurrent
        cuts.append(
            (HOTKEY_SEARCH, lambda: editor._search_widget.showOrFocus())  # type: ignore
        )
    else:
        # Browser: register shortcut with parent window, so that it works even
        # when editor pane is not focused
        t = QShortcut(QKeySequence(HOTKEY_SEARCH_BROWSER), editor.parentWindow)
        t.activated.connect(lambda: editor._search_widget.showOrFocus())  # type: ignore


def initialize_editor():
    try:  # Anki 2.1.20+
        from aqt.gui_hooks import editor_did_init_shortcuts

        editor_did_init_shortcuts.append(on_setup_editor_shortcuts)
    except (ImportError, ModuleNotFoundError):
        addHook("setupEditorShortcuts", on_setup_editor_shortcuts)

    try:  # Anki 2.1.24+
        from aqt.gui_hooks import editor_did_init

        editor_did_init.append(on_editor_did_init)
    except (ImportError, ModuleNotFoundError):
        # setupTags as a less-contested surrogate to Editor.__init__
        Editor.setupTags = wrap(Editor.setupTags, on_editor_did_init, "after")
