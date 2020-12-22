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

from anki.collection import _Collection

import re

from .config import config
from .tags import findReplaceTags, FindReplaceRequest

from typing import NamedTuple

SEPARATOR = config["local"]["hierarchicalTagsSeparator"]


class ReplacementResult(NamedTuple):
    tag: str
    count: int


class TagReplacementMediator:
    def __init__(self, col: _Collection):
        self._col = col

    def reposition(self, old: str, new: str) -> ReplacementResult:
        """
        Reposition tag under different parent tag

        Arguments:
            old {str} -- Tag (hierarchy) to reposition
            new {str} -- New tag (hierarchy) to position source tag under.
                         Leave blank to position tag under root tree.
        """
        components = old.split(SEPARATOR)
        last_node = components.pop()
        old_stem = (SEPARATOR.join(components) + SEPARATOR) if components else ""

        find = r"^{}(({})({}.*|$))".format(
            re.escape(old_stem), re.escape(last_node), SEPARATOR
        )

        if new:  # other tag
            replace = "{}{}\g<1>".format(new.replace("\\", "\\\\"), SEPARATOR)
            new_tags = new.split(SEPARATOR) + [last_node]
        else:  # root tree
            replace = "\g<1>"
            new_tags = [last_node]

        request = FindReplaceRequest(
            find=find,
            replace=replace,
            nids=[],
            whole_tags=False,
            regex=True,
            search_str=f'"tag:{old}*"',
        )

        count = findReplaceTags(self._col, request)

        return ReplacementResult(tag=SEPARATOR.join(new_tags), count=count)

    def reorganize(self, old: str, new: str) -> ReplacementResult:
        find = r"^({})({}.*|$)".format(re.escape(old), SEPARATOR)
        replace = r"{}\g<2>".format(new.replace("\\", "\\\\"))

        request = FindReplaceRequest(
            find=find,
            replace=replace,
            search_str=f'"tag:{old}*"',
            nids=[],
            whole_tags=False,
            regex=True,
        )

        count = findReplaceTags(self._col, request)

        return ReplacementResult(tag=new, count=count)

    def rename(self, old: str, new: str) -> ReplacementResult:
        """
        Replace provided tag with user-entered string

        Arguments:
            old {str} -- Tag to replace
            new {str} -- Replacement
        """
        # need to split in case user has replaced a regular tag with
        # a hierarchical tag:
        request = FindReplaceRequest(
            find=old,
            replace=new,
            search_str=f'"tag:{old}"',
            nids=[],
            whole_tags=True,
            regex=False,
        )
        new_tags = [new]

        count = findReplaceTags(self._col, request)

        return ReplacementResult(tag=SEPARATOR.join(new_tags), count=count)

    def renameHierarchy(self, old: str, new: str) -> ReplacementResult:
        components = old.split(SEPARATOR)
        last_comp = components[-1]
        preceding_comp = SEPARATOR.join(components[:-1])
        root = old == last_comp

        prefix = f"{preceding_comp}{SEPARATOR}" if preceding_comp else ""

        if root:
            find = r"^({})({}.*|$)".format(re.escape(last_comp), SEPARATOR)
            # need to escape potential backslashes in user input
            # (re.escape only works for matching strings):
            replace = r"{}\g<2>".format(new.replace("\\", "\\\\"))
        else:
            find = r"^({})({})({}.*|$)".format(
                re.escape(prefix), re.escape(last_comp), SEPARATOR
            )
            replace = r"\g<1>{}\g<3>".format(new.replace("\\", "\\\\"))

        request = FindReplaceRequest(
            find=find,
            replace=replace,
            nids=[],
            search_str=f'"tag:{old}*"',
            whole_tags=False,
            regex=True,
        )

        new_tags = components[:-1] + [new]

        count = findReplaceTags(self._col, request)

        return ReplacementResult(tag=SEPARATOR.join(new_tags), count=count)

    def delete(self, tag: str, is_hierarchy: bool) -> ReplacementResult:
        """
        Delete provided tag
        and (in case of hierarchy) all subtags

        Arguments:
            tag {str} -- Tag (hierarchy) to be deleted
            is_hierarchy {bool} -- Whether or not tag is part of a hierarchy
        """
        search_str = f'"tag:{tag}"'
        if is_hierarchy:
            request = FindReplaceRequest(
                find=r"^{}({}.*|$)".format(re.escape(tag), SEPARATOR),
                replace="",
                nids=[],
                search_str=search_str + "*",
                whole_tags=False,
                regex=True,
            )
        else:
            request = FindReplaceRequest(
                find=tag,
                replace="",
                nids=[],
                search_str=search_str,
                whole_tags=True,
                regex=False,
            )

        count = findReplaceTags(self._col, request)

        return ReplacementResult(tag="", count=count)
