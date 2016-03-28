#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class Matrix:
    """Matrix structure."""

    def __init__(self, row_count, column_count, default_value=None):
        """Initialize a |row_count| * |column_count| matrix and set all
        values to |default_value|.

        :type row_count: int
        :type column_count: int
        """

        #  Initialize basic matrix information and the value pool.
        self.__rc = row_count
        self.__cc = column_count
        self.__v = [default_value] * (row_count * column_count)
        self.__ptr = []

        #  Initialize index pointers of rows.
        data_ptr = 0
        for row in range(0, row_count):
            self.__ptr.append(data_ptr)
            data_ptr += column_count

    def exchange_row(self, row1, row2):
        """Exchange two rows.

        :type row1: int
        :type row2: int
        :param row1: The first row index.
        :param row2: The second row index.
        """

        #  Exchange the index pointer of two rows.
        t = self.__ptr[row1]
        self.__ptr[row1] = self.__ptr[row2]
        self.__ptr[row2] = t

    def get_row_count(self):
        """Get the row count of the matrix.

        :rtype : int
        :return: The row count.
        """

        return self.__rc

    def get_column_count(self):
        """Get the column count of the matrix.

        :rtype : int
        :return: The column count.
        """

        return self.__cc

    def _get_row_offset(self, row):
        """Get the offset of the first value of specific row.

        :type row: int
        :param row: The row offset.
        :rtype : int
        :return: The offset.
        """

        return self.__ptr[row]

    def _get_item_offset(self, row, column):
        """Calculate the item offset by its row index and column index.

        :type row: int
        :type column: int
        :param row: The row index.
        :param column: The column index.
        :rtype : int
        :return: The calculated offset.
        """

        return self._get_row_offset(row) + column

    def write_item_by_position(self, row, column, new_value):
        """Set the value of the item at specific position.

        :type row: int
        :type column: int
        :param row: The row index of the item.
        :param column: The column index of the item.
        :param new_value: The new value of the item.
        """

        self._write_item_by_offset(self._get_item_offset(row, column), new_value)

    def _write_item_by_offset(self, offset, new_value):
        """Set the value of the item at specific offset.

        :type offset: int
        :param offset: The offset.
        :param new_value: The new value of the item.
        """

        self.__v[offset] = new_value

    def get_item_by_position(self, row, column):
        """Get the item at specific position.

        :type row: int
        :type column: int
        :param row: The row index of the item.
        :param column: The column index of the item.
        :return: The value of the item.
        """

        return self._get_item_by_offset(self._get_item_offset(row, column))

    def _get_item_by_offset(self, offset):
        """Get the item at specific offset.

        :type offset: int
        :param offset: The offset.
        :return: The value of the item.
        """

        return self.__v[offset]

    #
    #  Debug codes.
    #
    def debug_print(self, title="Test", ofx_row=0, ofy_col=0):
        """Print function for debugging.

        :type title: str
        :type ofx_row: int
        :type ofy_col: int
        :param title: Header text.
        :param ofx_row: Row offset.
        :param ofy_col: Column offset.
        """

        #  Print banner.
        print("----- " + title + " -----")

        for row in range(ofx_row, self.__rc):
            line_str = ""

            #  Join row items.
            for col in range(ofy_col, self.__cc):
                line_str += str(self.get_item_by_position(row, col))
                line_str += ", "

            #  Print the row.
            print(line_str)

        #  Print end line.
        print("-------------------------")
