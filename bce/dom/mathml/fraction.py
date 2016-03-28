#!/usr/bin/env python
#
#  Copyright 2014 - 2015 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class FractionComponent(_base.Base):
    """Fraction component."""

    def __init__(self, numerator_obj, denominator_obj):
        """Initialize the fraction component.

        :param numerator_obj: Numerator object.
        :param denominator_obj: Denominator object.
        """

        self.__numer = numerator_obj
        self.__denom = denominator_obj
        _base.Base.__init__(self, _types.COMPONENT_TYPE_FRACTION)

    def get_numerator_object(self):
        """Get the numerator object.

        :return: The numerator object.
        """
        return self.__numer

    def set_numerator_object(self, value):
        """Set the numerator object.

        :param value: The numerator object.
        """
        self.__numer = value

    def get_denominator_object(self):
        """Get the denominator object.

        :return: The denominator object.
        """

        return self.__denom

    def set_denominator_object(self, value):
        """Set the denominator object.

        :param value: The denominator object.
        """

        self.__denom = value

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        #  Add header.
        s = " " * indent + "<mfrac>\n"

        #  Serialize and add the numerator and the denominator.
        s += self.__numer.to_string(indent + 4) + "\n"
        s += self.__denom.to_string(indent + 4) + "\n"

        #  Add tail.
        s += " " * indent + "</mfrac>"

        return s
