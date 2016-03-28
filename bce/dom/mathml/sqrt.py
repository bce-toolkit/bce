#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class SquareRootComponent(_base.Base):
    """Square-root component."""

    def __init__(self, base_obj):
        """Initialize the component.

        :param base_obj: The base object.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_SQRT)
        self.__base_obj = base_obj

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

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        #  Add the header.
        s = " " * indent + "<msqrt>\n"

        #  Serialize and add the base object.
        s += self.__base_obj.to_string(indent + 4) + "\n"

        #  Add the tail.
        s += " " * indent + "</msqrt>"

        return s
