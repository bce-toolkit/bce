#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class Stack:
    """Stack structure."""

    def __init__(self):
        """Initialize the object."""

        self.__data = []

    def __len__(self):
        """Get the item count.

        :rtype : int
        :return: The item count.
        """

        return len(self.__data)

    def push(self, item):
        """Push an item onto the stack.

        :param item: The item (any type).
        """

        self.__data.append(item)

    def pop(self):
        """Pop the top item off from the stack and return it.

        :return: The top item.
        """

        #  Safe check.
        if len(self.__data) == 0:
            raise IndexError("No item.")

        return self.__data.pop()

    def top(self):
        """Get the item at the top of the stack.

        :return: The item.
        """

        #  Safe check.
        if len(self.__data) == 0:
            raise IndexError("No item.")

        return self.__data[-1]
