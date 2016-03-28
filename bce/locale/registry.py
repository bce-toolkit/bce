#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.tree as _tree

#  Message trees container.
_MESSAGE_TREES = []

#  Fallback language ID (use English by default).
_FALLBACK_LANGUAGE_ID = "en_US"


def register_message_tree(tree):
    """Register a message tree.

    :type tree: bce.locale.tree.MessageTree
    :param tree: The message tree object.
    """

    _MESSAGE_TREES.append(tree)


def register_fallback_language_id(language_id):
    """Register the fallback language ID.

    :type language_id: str
    :param language_id: The ID.
    """

    global _FALLBACK_LANGUAGE_ID
    _FALLBACK_LANGUAGE_ID = language_id


def apply_replace_map(text, replace_map):
    """Apply replace map to a text.

    :type text: str
    :type replace_map: dict[str, str]
    :param text: The text.
    :param replace_map: The map.
    """

    #  Do replacing.
    for to_replace in replace_map:
        text = text.replace(to_replace, replace_map[to_replace])

    return text


def get_message(language_id, key_path, default=None, allow_fallback=True, replace_map=None):
    """Get a message from registered message trees.

    :type language_id: str
    :type key_path: str
    :type default: str | None
    :type allow_fallback: bool
    :type replace_map: dict | None
    :param language_id: The language ID.
    :param key_path: The key path of the message.
    :param default: The default value. (If not allowed, set to None.)
    :param allow_fallback: Set to True if fallback language is allowed.
    :param replace_map: The replace map.
    :rtype : str
    :return: The message.
    """

    if replace_map is None:
        replace_map = {}

    for msg_tree in _MESSAGE_TREES:
        assert isinstance(msg_tree, _tree.MessageTree)

        #  Check the language ID.
        if not msg_tree.is_language_matches(language_id):
            continue

        #  Try to get the message from current tree.
        if msg_tree.has_message(key_path):
            return apply_replace_map(msg_tree.get_message(key_path), replace_map)

    if allow_fallback:
        #  Fallback.
        return get_message(
            _FALLBACK_LANGUAGE_ID,
            key_path,
            default=default,
            allow_fallback=False,
            replace_map=replace_map
        )
    else:
        raise KeyError("No such message.")
