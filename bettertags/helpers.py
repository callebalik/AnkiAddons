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
Helpers
"""

import functools
import sre_constants
from contextlib import contextmanager
from typing import Callable, Iterator, Optional

from aqt.browser import Browser
from aqt.utils import showInfo, tooltip

from .consts import ADDON
from .tags import FindError


@contextmanager
def resetBrowser(
    browser: Browser,
    checkpoint: str,
    progress_max: int = 0,
    search: Optional[str] = None,
) -> Iterator:

    browser.mw.checkpoint(f"{ADDON.MODULE}: {checkpoint}")
    browser.mw.progress.start(label=checkpoint, max=progress_max)
    browser.model.beginReset()

    try:
        yield
    except sre_constants.error as e:
        print(e)
        showInfo("Invalid regular expression.", parent=browser)
    except FindError as e:
        print(e)
        search = None
        tooltip("No matching tags found")
    finally:
        browser.mw.requireReset()
        # Trigger collection tag refresh (not passing nids → trigger full refresh):
        browser.col.tags.registerNotes()
        browser.model.endReset()
        browser.mw.progress.finish()
        if search:
            browser.form.searchEdit.lineEdit().setText(search)
            browser.onSearchActivated()


def browserEditorSaveThen(callback: Callable):
    @functools.wraps(callback)
    def onSaved(sidebar, *args, **kwargs):
        sidebar.browser.editor.saveNow(lambda: callback(sidebar, *args, **kwargs))

    return onSaved
