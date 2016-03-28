#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

#
#  NOTE:
#    In this module, all items in a matrix should be SymPy objects.
#

import bce.math.constant as _constant
import bce.math.matrix as _matrix


class SolutionSystem:
    """Solution system."""

    def __init__(self, constant_vector, base_vectors):
        """Initialize the object.

        :type constant_vector: list
        :type base_vectors: bce.math.matrix.Matrix
        :param constant_vector: The constant vector.
        :param base_vectors: The base vectors.
        """

        #  Check the size.
        if len(constant_vector) != base_vectors.get_row_count():
            raise RuntimeError("Invalid solution system.")

        #  Save the vectors.
        self.__const_vector = constant_vector
        self.__base_vectors = base_vectors

    def get_constant_vector(self):
        """Get the constant vector.

        :rtype : list
        :return: The vector.
        """

        return self.__const_vector

    def get_base_vectors(self):
        """Get the base vectors.

        :rtype : bce.math.matrix.Matrix
        :return: The vectors matrix.
        """

        return self.__base_vectors

    def get_length(self):
        """Get the length(count of rows) of the solution system.

        :rtype : int
        :return: The length.
        """

        return len(self.__const_vector)


def solve_equations(mtx):
    """Solve a linear equation group.

    Note:
      [1] The source matrix will be changed during solving the equations.
          If you want to keep the origin matrix, you have to copy it before
          calling this method.

    :type mtx: bce.math.matrix.Matrix
    :param mtx: The matrix of the equations.
    :rtype : SolutionSystem
    :return: The solution system.
    """

    #  Initialize the base-vector flags container.
    bv_flags = [False] * (mtx.get_column_count() - 1)

    #  Initialize the diagonal line container.
    diagonal_line = []

    #  Initialize the cursor.
    cursor_row = 0
    cursor_column = 0

    #  ZF the lower triangular (and also set the base-vector flags).
    while cursor_row < mtx.get_row_count() and cursor_column + 1 < mtx.get_column_count():
        #  Find the first non-zero item in current column.
        found_non_zero = False
        for row_id in range(cursor_row, mtx.get_row_count()):
            item = mtx.get_item_by_position(row_id, cursor_column)
            item = item.simplify()
            if not item.is_zero:
                found_non_zero = True
                mtx.exchange_row(row_id, cursor_row)
                break

        #  If there is no non-zero item, keep finding in next column and mark current
        #  column as a base vector column.
        if not found_non_zero:
            bv_flags[cursor_column] = True
            cursor_column += 1
            continue

        #  Add current position to the diagonal line.
        diagonal_line.append((cursor_row, cursor_column))

        #  Divide all items in current row with the first item of current row.
        first_value = mtx.get_item_by_position(cursor_row, cursor_column)
        for column_id in range(cursor_column, mtx.get_column_count()):
            item = mtx.get_item_by_position(cursor_row, column_id)
            item /= first_value
            item = item.simplify()
            mtx.write_item_by_position(cursor_row, column_id, item)

        #  Eliminate other rows.
        for row_id in range(cursor_row + 1, mtx.get_row_count()):
            first_value = mtx.get_item_by_position(row_id, cursor_column)
            for column_id in range(cursor_column, mtx.get_column_count()):
                item = mtx.get_item_by_position(row_id, column_id)
                item -= first_value * mtx.get_item_by_position(cursor_row, column_id)
                item = item.simplify()
                mtx.write_item_by_position(row_id, column_id, item)

        #  Move the cursor.
        cursor_row += 1
        cursor_column += 1

    #  Mark remain columns as base-vector columns.
    for column_id in range(cursor_column, mtx.get_column_count() - 1):
        bv_flags[column_id] = True

    #  Reverse the diagonal line.
    diagonal_line.reverse()

    #  ZF the upper triangular.
    for cursor_row, cursor_column in diagonal_line:
        for row_id in range(0, cursor_row):
            first_value = mtx.get_item_by_position(row_id, cursor_column)
            for column_id in range(cursor_column, mtx.get_column_count()):
                item = mtx.get_item_by_position(row_id, column_id)
                item -= first_value * mtx.get_item_by_position(cursor_row, column_id)
                item = item.simplify()
                mtx.write_item_by_position(row_id, column_id, item)

    #  Reverse again.
    diagonal_line.reverse()

    #  Get the count of vectors of the basic solution system.
    bv_count = 0
    for column_id in range(0, mtx.get_column_count() - 1):
        if bv_flags[column_id]:
            bv_count += 1

    #  Initialize the base-vector data container.
    bv_data = []
    for idx in range(0, bv_count):
        bv_data.append([])

    #  Extract base-vector columns from the origin matrix.
    bv_id = 0
    for column_id in range(0, mtx.get_column_count() - 1):
        if bv_flags[column_id]:
            for row_id in range(0, mtx.get_row_count()):
                item = mtx.get_item_by_position(row_id, column_id)
                item = -item
                item = item.simplify()
                bv_data[bv_id].append(item)
            bv_id += 1

    #  Add components that is mapped to base vectors.
    bv_id = 0
    for column_id in range(0, mtx.get_column_count() - 1):
        if bv_flags[column_id]:
            for vector_id in range(0, bv_count):
                if vector_id == bv_id:
                    bv_data[vector_id].insert(column_id, _constant.ONE)
                else:
                    bv_data[vector_id].insert(column_id, _constant.ZERO)
            bv_id += 1

    #  Construct the constant vector.
    const_vector = []
    for row_id in range(0, len(diagonal_line)):
        const_vector.append(mtx.get_item_by_position(row_id, mtx.get_column_count() - 1))
    for column_id in range(0, mtx.get_column_count() - 1):
        if bv_flags[column_id]:
            const_vector.insert(column_id, _constant.ZERO)

    #  Convert base-vector data to matrix.
    bv_mtx = _matrix.Matrix(mtx.get_column_count() - 1, bv_count)
    for bv_id in range(0, bv_count):
        for bv_sub_id in range(0, mtx.get_column_count() - 1):
            bv_mtx.write_item_by_position(bv_sub_id, bv_id, bv_data[bv_id][bv_sub_id])

    return SolutionSystem(const_vector, bv_mtx)


def check_answer(mtx, answers):
    """Check whether an answers satisfied all equations.

    :type mtx: bce.math.matrix.Matrix
    :type answers: list
    :param mtx: The matrix of the equations.
    :param answers: The answers list.
    :rtype : bool
    :return: True if satisfied.
    """

    for row_id in range(0, mtx.get_row_count()):
        #  Initialize sum.
        sum_value = _constant.ZERO

        #  Get the sum.
        for col_id in range(0, mtx.get_column_count() - 1):
            sum_value += mtx.get_item_by_position(row_id, col_id) * answers[col_id]

        #  Simplify before checking.
        sum_value = sum_value.simplify()

        #  Check the sum.
        if sum_value != mtx.get_item_by_position(row_id, mtx.get_column_count() - 1):
            return False

    return True
