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
Utility functions used to find and replace tags in the database
"""

import re
from typing import List, NamedTuple, Optional, Tuple

from anki.collection import _Collection
from anki.utils import ids2str, intTime


class FindError(Exception):
    pass


class FindReplaceRequest(NamedTuple):
    """
    Arguments:
        nids {list} -- List of note IDs to iterate through. If empty
                       iterate through all notes in the collection.
        find {str} -- Original string
        replace {str} -- Replacement string

    Keyword Arguments:
        whole_tags {bool} -- Whether or not to match whole words instead of
                             substrings (default: {True})
        ignore_case {bool} -- Whether or not to ignore case (default: {True})
        regex {bool} -- Whether or not to treat find and replace as regular
                        expressions (default: {False})
    
    """

    find: str = ""
    replace: str = ""
    nids: Optional[list] = None
    search_str: Optional[str] = None
    whole_tags: bool = True
    ignore_case: bool = False
    regex: bool = False


def findReplaceTags(col: _Collection, request: FindReplaceRequest) -> int:
    """Perform tag replacements on provided notes within Anki collection
    
    Arguments:
        col {_Collection} -- Anki collection object
        request {FindReplaceRequest} -- Find and replace arguments packed in a
                                        FidnReplaceRequest tuple
    
    Raises:
        FindError: When no matching notes are found
    
    Returns:
        int -- Number of updated notes
    """

    # unpack performance-relevant members
    find = request.find
    replace = request.replace
    nids = request.nids
    ignore_case = request.ignore_case

    # Sanity check
    assert find, "No find string provided."

    # Adjust regular expression according to supplied user settings
    # and compile it:
    if not request.regex:
        find = re.escape(find)

    if request.whole_tags:
        find = r"^" + find + r"$"

    if ignore_case:
        find = r"(?i)" + find

    re_compiled = re.compile(find)

    # Check and adjust note limits
    if not nids and request.search_str:
        # attempt to narrow down nids to iterate over
        nids = col.findNotes(request.search_str)

    if nids:
        # query selected nids
        nids_string = ids2str(nids)
        query = "select id, tags from notes where id in " + nids_string
    else:
        # query entire collection
        query = "select id, tags from notes"

    # Walk through provided note IDs, query the database for the
    # corresponding tag strings, and compile a list of changes
    # to apply subsequently
    # notes_to_update: tag_string, mod_time, usn, nid
    notes_to_update: List[Tuple[str, int, int, int]] = []
    updated_nids = []

    for nid, tags_string in col.db.execute(query):

        tags = col.tags.split(tags_string)

        new_tags = [re_compiled.sub(replace, tag) for tag in tags]

        new_tags_string = col.tags.join(_customTagCanonify(col, new_tags, ignore_case))

        if new_tags_string.strip() != tags_string.strip():
            updated_nids.append(nid)
            notes_to_update.append(
                (new_tags_string, intTime(), col.usn(), nid)
            )

    if not notes_to_update:
        raise FindError("No matching notes found")

    # Commit previously registered changes to the database and update
    # caches / regenerate cards
    col.db.executemany(
        "update notes set tags=?,mod=?,usn=? where id=?", notes_to_update
    )

    return len(notes_to_update)


def _customTagCanonify(
    col: _Collection, tag_list: List[str], ignore_case: bool
) -> list:
    """
    Strip duplicates, adjust case to match existing tags if
    ignore_case set, and sort.

    Modified version of anki.tags.tagCanonify

    Arguments:
        col {anki.collection._Collection} -- Anki collection object
        tag_list {list} -- List of tags to canonify
        ignore_case {boolean} -- Whether or not to normalize case

    Returns:
        list -- List of canonified tags
    """
    if not ignore_case:
        stripped = [re.sub("[\"']", "", t) for t in tag_list if t]
    else:
        stripped = []
        for t in tag_list:
            if t == "":
                continue
            s = re.sub("[\"']", "", t)
            if ignore_case:
                for existing in col.tags.tags:
                    if s.lower() == existing.lower():
                        s = existing
            stripped.append(s)

    return sorted(set(stripped))


def getSearchString(tag: str, whole_tags: bool) -> str:
    """
    Return query language search token for provided tag.

    Arguments:
        tag {str} -- Tag (component) to look for
        whole_tags {boolean} -- Whether 'tag' is a full tag or not

    Returns:
        str -- Query language search token
    """
    if not tag:
        return ""
    elif whole_tags:
        return '"tag:{}"'.format(tag)
    else:
        return '"tag:*{}*"'.format(tag)
