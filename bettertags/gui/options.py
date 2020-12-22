# -*- coding: utf-8 -*-

# BetterTags Add-on for Anki
#
# Copyright (C) 2017-2020  Aristotelis P. <https//glutanimate.com/>
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
Options dialog and associated components
"""

from aqt import mw
from anki.hooks import runHook

from PyQt5.QtWidgets import QApplication, QAction

from ..libaddon.gui.dialog_options import OptionsDialog
from ..libaddon.platform import PLATFORM

from ..config import config

from .forms import options as qtform_options

__all__ = ["BetterTagsOptions", "invokeOptionsDialog"]

tag_expansion_behaviors = {
    "restore": {"label": "Restore state"},
    "collapse_all": {"label": "Collapse all"},
    "expand_all": {"label": "Expand all"},
}


class BetterTagsOptions(OptionsDialog):

    """
    Add-on-specific options dialog implementation
    """

    _mapped_widgets = (
        (
            "form.cb_enable_sidebar",
            (("value", {"dataPath": "local/enableSidebarModifications"}),),
        ),
        (
            "form.cb_enable_completer",
            (("value", {"dataPath": "local/enableHierarchicalCompleter"}),),
        ),
        (
            "form.cb_completer_substrings",
            (
                (
                    "value",
                    {"dataPath": "local/hierarchicalCompleterArbitrarySubstrings"},
                ),
            ),
        ),
        (
            "form.cb_completer_workaround",
            (
                (
                    "value",
                    {"dataPath": "local/hierarchicalCompleterHighlightWorkaround"},
                ),
            ),
        ),
        (
            "form.hotkey_replace",
            (("value", {"dataPath": "local/hotkeyFindReplace"},),),
        ),
        (
            "form.hotkey_refresh",
            (("value", {"dataPath": "local/hotkeyRefreshTags"},),),
        ),
        ("form.hotkey_delete", (("value", {"dataPath": "local/hotkeyDeleteTag"},),),),
        ("form.hotkey_rename", (("value", {"dataPath": "local/hotkeyRenameTag"},),),),
        (
            "form.le_separator",
            (("value", {"dataPath": "local/hierarchicalTagsSeparator"},),),
        ),
        (
            "form.sel_tag_expansion",
            (
                # order is important (e.g. to set-up items before current item)
                ("items", {"setter": "_setSelTagExpansionItems"}),
                ("value", {"dataPath": "local/hierarchyExpansionBehavior"},),
            ),
        ),
        (
            "form.cb_confirm_deletion",
            (("value", {"dataPath": "local/confirmItemDeletion"}),),
        ),
    )

    def __init__(self, config, mw, parent=None, **kwargs):
        # Mediator methods defined in mapped_widgets might need access to
        # certain instance attributes. As super().__init__ calls these
        # mediator methods it is important that we set the attributes
        # beforehand:
        self.parent = parent or mw
        self.mw = mw
        super(BetterTagsOptions, self).__init__(
            self._mapped_widgets,
            config,
            form_module=qtform_options,
            parent=self.parent,
            **kwargs
        )
        # Instance methods that modify the initialized UI should either be
        # called from self._setupUI or from here

    # UI adjustments

    def _setupUI(self):
        super(BetterTagsOptions, self)._setupUI()

        # manually adjust title label font sizes on Windows
        # gap between default windows font sizes and sizes that work well
        # on Linux and macOS is simply too big
        # TODO: find a better solution
        if PLATFORM == "win":
            default_size = QApplication.font().pointSize()
            for label in [self.form.fmtLabContrib, self.form.labHeading]:
                font = label.font()
                font.setPointSize(int(default_size * 1.5))
                label.setFont(font)

    # Events:

    def _onAccept(self):
        super()._onAccept()
        # reset browser sidebar
        runHook("newTag")

    # Actions:

    # Helpers:

    def _getComboItems(self, dct):
        return list((val["label"], key) for key, val in dct.items())

    # Config setters:

    def _setSelTagExpansionItems(self, data_val):
        return self._getComboItems(tag_expansion_behaviors)

    # Config getters:


def invokeOptionsDialog(parent=None):
    """Call settings dialog"""
    dialog = BetterTagsOptions(config, mw, parent=parent)
    return dialog.exec_()


def initializeOptions():
    config.setConfigAction(invokeOptionsDialog)
    # Set up menu entry:
    options_action = QAction("Better&Tags Settings...", mw)
    options_action.triggered.connect(lambda _: invokeOptionsDialog())  # type:ignore
    mw.form.menuTools.addAction(options_action)
