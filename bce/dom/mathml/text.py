#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class TextComponent(_base.Base):
    """Text component."""

    def __init__(self, text):
        """Initialize the component.

        :param text: The text.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_TEXT)
        self.__text = text

    def get_text(self):
        """Get the text.

        :return: The text.
        """

        return self.__text

    def set_text(self, text):
        """Set the text.

        :param text: The text.
        """

        self.__text = text

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        return " " * indent + "<mtext>" + self.__text + "</mtext>"
