#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class RootComponent(_base.Base):
    """Root component."""

    def __init__(self, base_obj, exp_obj):
        """Initialize the component.

        :param base_obj: The base object.
        :param exp_obj: The exponent object.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_ROOT)
        self.__base_obj = base_obj
        self.__exp_obj = exp_obj

    def get_base_object(self):
        """Get the base object.

        :return: The base object.
        """

        return self.__base_obj

    def set_base_object(self, base_obj):
        """Set the base object.

        :param base_obj: The base object.
        """

        self.__base_obj = base_obj

    def get_exponent_object(self):
        """Get the exponent object.

        :return: The exponent object.
        """

        return self.__exp_obj

    def set_exponent_object(self, exp_obj):
        """Set the exponent object.

        :param exp_obj: The exponent object.
        """

        self.__exp_obj = exp_obj

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        #  Add the header.
        s = " " * indent + "<mroot>\n"

        #  Serialize and add the base object and the exponent type.
        s += self.__base_obj.to_string(indent + 4) + "\n"
        s += self.__exp_obj.to_string(indent + 4) + "\n"

        #  Add the tail.
        s += " " * indent + "</mroot>"

        return s
