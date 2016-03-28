#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


def merge_coefficients_with_cexp_object(cexp_object, coefficients):
    """Merge balanced coefficients with a chemical equation.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :type coefficients: list
    :param cexp_object: The chemical equation object.
    :param coefficients: The balanced coefficients list.
    """

    #  Check the size.
    assert len(coefficients) == len(cexp_object)

    #  Process left items.
    for idx in range(0, cexp_object.get_left_item_count()):
        item = cexp_object.get_left_item(idx)
        item.set_coefficient(coefficients[idx])
        cexp_object.set_left_item(idx, item)

    #  Process right items.
    for idx in range(0, cexp_object.get_right_item_count()):
        item = cexp_object.get_right_item(idx)
        item.set_coefficient(coefficients[cexp_object.get_left_item_count() + idx])
        cexp_object.set_right_item(idx, item)
