#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class ASTNodeBase:
    """Base class for AST nodes."""

    def __init__(self, node_type):
        """Initialize the AST node.

        :type node_type: int
        :param node_type: The node type identifier.
        """

        self.__node_type = node_type
        self.__properties = {}
        self.__children = []
        self.__parent = None

    def __len__(self):
        """Get the children count.

        :rtype : int
        :return: The count.
        """

        return len(self.__children)

    def get_node_type(self):
        """Get the node type identifier.

        :rtype : int
        :return: The identifier.
        """

        return self.__node_type

    def set_property(self, key, value):
        """Set a property.

        :type key: str
        :param key: The key of the property.
        :param value: The value of the property.
        """

        self.__properties[key] = value

    def has_property(self, key):
        """Check whether the node has specified property.

        :type key: str
        :param key: The key of the property.
        :rtype : bool
        :return: True if the property exists. Otherwise, return False.
        """

        return key in self.__properties

    def get_property(self, key, default=None):
        """Get the value of specified property.

        :type key: str
        :param key: The key of the property.
        :param default: The value to be returned when the property doesn't exist.
        :return: The value of the property.
        """

        if self.has_property(key):
            return self.__properties[key]
        else:
            return default

    def remove_property(self, key):
        """Remove a property.

        :type key: str
        :param key: The key of the property.
        :raise KeyError: Raise when the key is invalid.
        """

        #  Check the key.
        if not self.has_property(key):
            raise KeyError("Invalid property key.")

        #  Delete the property.
        del self.__properties[key]

    def append_child(self, child_node):
        """Append a child node.

        :type child_node: ASTNodeBase
        :param child_node: The child node.
        """

        self.__children.append(child_node)

    def __getitem__(self, idx):
        """Get the child on specified index.

        :type idx: int
        :param idx: The index.
        :rtype : ASTNodeBase
        :return: The child node.
        """

        return self.__children[idx]

    def __setitem__(self, idx, new_node):
        """Set the child on specified index.

        :type idx: int
        :type new_node: ASTNodeBase
        :param idx: The index.
        :param new_node: The new child node.
        """

        self.__children[idx] = new_node

    def __delitem__(self, idx):
        """Delete the child on specified index.

        :type idx: int
        :param idx: The index.
        """

        self.__children.pop(idx)

    def get_parent_node(self):
        """Get parent node.

        :rtype : ASTNodeBase
        :return: The parent node.
        """

        return self.__parent

    def set_parent_node(self, new_parent_node):
        """Set parent node.

        :type new_parent_node: ASTNodeBase
        :param new_parent_node: The new parent node.
        """

        self.__parent = new_parent_node

    def register_starting_position_in_source_text(self, pos):
        """Register the starting position of current node in the source text.

        :type pos: int
        :param pos: The position.
        """

        self.set_property("src_text_starting", pos)

    def register_ending_position_in_source_text(self, pos):
        """Register the ending position of current node in the source text.

        :type pos: int
        :param pos: The position.
        """

        self.set_property("src_text_ending", pos)

    def get_starting_position_in_source_text(self):
        """Get the starting position of current node in the source text.

        :rtype : int
        :return: The position (if the position hasn't been registered, return -1).
        """

        return self.get_property("src_text_starting", -1)

    def get_ending_position_in_source_text(self):
        """Get the ending position of current node in the source text.

        :rtype : int
        :return: The position (if the position hasn't been registered, return -1).
        """

        return self.get_property("src_text_ending", -1)

    def register_source_text_range(self, starting_pos, ending_pos):
        """Register the starting position and the ending position of current node in the source text.

        :type starting_pos: int
        :type ending_pos: int
        :param starting_pos: The starting position.
        :param ending_pos: The ending position.
        """

        self.register_starting_position_in_source_text(starting_pos)
        self.register_ending_position_in_source_text(ending_pos)

    #
    #  Debug codes.
    #
    def debug_print(self, source_expr=None):
        """Print debug messages.

        :type source_expr: str | None
        :param source_expr: The source expression.
        """

        #  Print the header.
        print("Node Information")
        print("----------------------------")

        #  Print the node type.
        print("Type: " + self.__class__.__name__)

        #  Print the source expression.
        if source_expr is None:
            print("Source: [%d, %d]" % (self.get_starting_position_in_source_text(),
                                        self.get_ending_position_in_source_text()))
        else:
            print("Source: '%s'" % source_expr[self.get_starting_position_in_source_text():
                                               self.get_ending_position_in_source_text() + 1])

        #  Print the properties.
        properties = []
        for prop_name in self.__properties:
            properties.append(prop_name)
        print("Properties: %s" % str(properties))

        #  Print the children count.
        print("Children Count: %d" % len(self))

        #  Print the end line.
        print("----------------------------")
