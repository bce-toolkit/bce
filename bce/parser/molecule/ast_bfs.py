#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.ast.molecule as _ast_base


def do_bfs(root_node, reverse_order=True):
    """Do BFS on specified AST tree.

    :type root_node: _ast_base._ASTNodeBaseML
    :type reverse_order: bool
    :param root_node: The root node.
    :param reverse_order: Set to True if you want to iterate from leaves to the root. Otherwise, set to False.
    :rtype : list[_ast_base._ASTNodeBaseML]
    :return: A list that contains the BFS result.
    """

    #  Initialize the BFS queue.
    queue = [root_node]
    """:type : list[_ml_ast_base._ASTNodeBaseML]"""

    #  Initialize the result container.
    r = []
    """:type : list[_ml_ast_base._ASTNodeBaseML]"""

    while len(queue) != 0:
        #  Pop the first item off from the queue.
        front_node = queue.pop(0)

        #  Insert the item to the result.
        if reverse_order:
            r.insert(0, front_node)
        else:
            r.append(front_node)

        #  Add children.
        if front_node.is_hydrate_group() or front_node.is_molecule():
            for child_id in range(0, len(front_node)):
                queue.append(front_node[child_id])
        elif front_node.is_parenthesis():
            assert isinstance(front_node, _ast_base.ASTNodeParenthesisWrapper)
            queue.append(front_node.get_inner_node())
        else:
            pass

    return r
