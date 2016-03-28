#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class SubComponent(_base.Base):
    """Sub component."""

    def __init__(self, main_obj, sub_obj):
        """Initialize the component.

        :param main_obj: The main object.
        :param sub_obj: The sub object.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_SUB)
        self.__main_obj = main_obj
        self.__sub_obj = sub_obj

    def get_main_object(self):
        """Get the main object.

        :return: The main object.
        """

        return self.__main_obj

    def set_main_object(self, main_obj):
        """Set the main object.

        :param main_obj: The main object.
        """

        self.__main_obj = main_obj

    def get_sub_object(self):
        """Get the sub object.

        :return: The sub object.
        """

        return self.__sub_obj

    def set_sub_object(self, sub_obj):
        """Set the sub object.

        :param sub_obj: The sub object.
        """

        self.__sub_obj = sub_obj

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        #  Add the header.
        s = " " * indent + "<msub>\n"

        #  Serialize and add main object and sub object.
        s += self.__main_obj.to_string(indent + 4) + "\n"
        s += self.__sub_obj.to_string(indent + 4) + "\n"

        #  Add the tail.
        s += " " * indent + "</msub>"

        return s
