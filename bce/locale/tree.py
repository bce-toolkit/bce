#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import re as _re


class MessageTree:
    """Base class for all message tree classes."""

    def __init__(self, tree):
        """Initialize the tree.

        :type tree: dict
        :param tree: The message tree.
        """

        self.__tree = tree

    # noinspection PyMethodMayBeStatic
    def is_language_matches(self, language_id):
        """Is a language ID matches with the message tree.

        :type language_id: str
        :param language_id: The language ID.
        """

        raise RuntimeError("is_language_matches() method should be overrided.")

    def has_message(self, key_path):
        """Get whether a message exists in the tree.

        :param key_path: The key path of the message.
        :rtype : bool
        :return: True if so.
        """

        #  Try to get the message.
        try:
            self.get_message(key_path, default=None)
        except KeyError:
            return False

        return True

    def get_message(self, key_path, default=None):
        """Get a message from the tree.

        :type key_path: str
        :type default: str | None
        :param key_path: The key path of the message.
        :param default: The default value. (If not allowed, set to None.)
        :rtype : str
        :return: The message.
        """

        #  Initialize.
        current = self.__tree

        for folder in key_path.split("."):
            #  Check the existence of the sub folder.
            if isinstance(current, dict) == False or folder not in current:
                if default is None:
                    raise KeyError("No such key.")
                return default

            #  Go to the inner folder.
            current = current[folder]

        #  Check message type.
        if not isinstance(current, str):
            if default is None:
                raise KeyError("No such key.")
            return default

        return current


class EnglishMessageTree(MessageTree):
    """Base class for all English message tree classes."""

    def __init__(self, tree):
        """Initialize the tree.

        :type tree: dict
        :param tree: The message tree.
        """

        MessageTree.__init__(self, tree)

    def is_language_matches(self, language_id):
        """Is a language ID matches with the message tree.

        :type language_id: str
        :param language_id: The language ID.
        """

        return language_id.lower().startswith("en")


class ChineseSimplifiedMessageTree(MessageTree):
    """Base class for all Chinese(Simplified) message tree classes."""

    def __init__(self, tree):
        """Initialize the tree.

        :type tree: dict
        :param tree: The message tree.
        """

        MessageTree.__init__(self, tree)

    def is_language_matches(self, language_id):
        """Is a language ID matches with the message tree.

        :type language_id: str
        :param language_id: The language ID.
        """

        return _re.match(r"^zh(\-|_)(cn|hans)$", language_id.lower())
