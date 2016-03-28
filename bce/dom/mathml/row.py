#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types


class RowComponent(_base.Base):
    """Row component."""

    def __init__(self):
        """Initialize the row component."""

        _base.Base.__init__(self, _types.COMPONENT_TYPE_ROW)
        self.__objects = []

    def __len__(self):
        """Get the count of sub-items of the component.

        :return: The count.
        """

        return len(self.__objects)

    def __getitem__(self, key):
        """Get the item at specific position.

        :param key: The position.
        :return: The item at specific position.
        """

        return self.__objects[key]

    def __setitem__(self, key, value):
        """Set the item at specific position.

        :param key: The position.
        :param value: The value.
        """

        self.__objects[key] = value

    def __delitem__(self, key):
        """Delete the item at specific position.

        :param key: The position.
        """

        del self.__objects[key]

    def append_object(self, obj):
        """Append an item to the tail of the sub-object list.

        :param obj: The object.
        """

        self.__objects.append(obj)

    def insert_object(self, index, obj):
        """Insert an item before specific position.

        :param index: The position.
        :param obj: The object.
        """

        self.__objects.insert(index, obj)

    def pop_object(self, index=-1):
        """Pop the item at specific position.

        :param index: The position.
        :return: The item at the position.
        """

        return self.__objects.pop(index)

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        #  Add the header.
        s = " " * indent + "<mrow>\n"

        #  Serialize and add sub-items.
        for obj in self.__objects:
            s += obj.to_string(indent + 4) + "\n"

        #  Add the tail.
        s += " " * indent + "</mrow>"

        return s
