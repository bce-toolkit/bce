#!/usr/bin/env python
#
#  Copyright 2014 - 2015 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.types as _types


class Base:
    """Base class for MathML components."""

    def __init__(self, comp_type):
        """Initialize the component.

        :type comp_type: int
        :param comp_type: Component type (one of COMPONENT_TYPE_* in types.py).
        """

        self.__comp_type = comp_type
        self.__prop = {}

    def get_component_type(self):
        """Get the type of the component.

        :rtype : int
        :return: The component type (one of COMPONENT_TYPE_* in types.py).
        """

        return self.__comp_type

    def is_operator(self):
        """Get whether the component is a <mo>.

        :rtype : bool
        :return: Whether the component is a <mo>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_OPERATOR

    def is_text(self):
        """Get whether the component is a <mtext>.

        :rtype : bool
        :return: Whether the component is a <mtext>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_TEXT

    def is_number(self):
        """Get whether the component is a <mn>.

        :rtype : bool
        :return: Whether the component is a <mn>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_NUMBER

    def is_fraction(self):
        """Get whether the component is a <mfrac>.

        :rtype : bool
        :return: Whether the component is a <mfrac>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_FRACTION

    def is_row(self):
        """Get whether the component is a <mrow>.

        :rtype : bool
        :return: Whether the component is a <mrow>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_ROW

    def is_super(self):
        """Get whether the component is a <msup>.

        :rtype : bool
        :return: Whether the component is a <msup>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_SUPER

    def is_sub(self):
        """Get whether the component is a <msub>.

        :rtype : bool
        :return: Whether the component is a <msub>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_SUB

    def is_sub_and_super(self):
        """Get whether the component is a <msubsup>.

        :rtype : bool
        :return: Whether the component is a <msubsup>.
        """

        return self.__comp_type == _types.COMPONENT_TYPE_SUB_AND_SUPER

    def set_property(self, key, value):
        """Set the property of the component.

        :type key: str
        :param key: The property name.
        :param value: The value of the property.
        """

        self.__prop[key] = value

    def get_property(self, key):
        """Get the property of the component.

        :type key: str
        :param key: The property name.
        :return: The property value.
        """

        return self.__prop[key]

    def have_property(self, key):
        """Get whether the component has specific property.

        :type key: str
        :param key: The property name.
        :rtype : bool
        :return: Whether the component has specific property.
        """

        return key in self.__prop

    def remove_property(self, key):
        """Remove specific property from the component.

        :type key: str
        :param key: The property name.
        """

        del self.__prop[key]

    def clear_property(self):
        """Clear all property of the component."""

        self.__prop = {}

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        raise RuntimeError("to_string() method should be overrided.")
