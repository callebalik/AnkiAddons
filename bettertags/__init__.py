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
Initializes add-on components.
"""

from ._version import __version__  # noqa: F401

from .libaddon import maybeVendorTyping

maybeVendorTyping()

def initializeAddon():
    """Initializes add-on after performing a few checks

    Allows more fine-grained control over add-on execution, which can
    be helpful when implementing workarounds for Anki bugs (e.g. the module
    import bug present in all Anki 2.1 versions up to 2.1.14)
    """
    
    from .libaddon import checkFor2114ImportError
    from .consts import ADDON

    if not checkFor2114ImportError(ADDON.NAME):
        return False

    from .libaddon.consts import setAddonProperties

    setAddonProperties(ADDON)

    from .browser import initializeBrowser
    from .tagedit import initializeTagedit

    from .gui.options import initializeOptions
    from .gui import initializeQtResources
    
    initializeQtResources()
    initializeOptions()
    initializeBrowser()
    initializeTagedit()

initializeAddon()
