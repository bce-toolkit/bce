#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class NumberComponent(_base.Base):
    """Number component."""

    def __init__(self, number_str):
        """Initialize the number component.

        :type number_str: str
        :param number_str: The string of the number.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_NUMBER)
        self.__num_str = number_str

    def get_number_string(self):
        """Get the string of the number.

        :rtype : str
        :return: The string of the number.
        """

        return self.__num_str

    def set_number_string(self, number_str):
        """Set the string of the number.

        :type number_str: str
        :param number_str: The string of the number.
        """

        self.__num_str = number_str

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        return " " * indent + "<mn>" + self.__num_str + "</mn>"
