#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

#  Reaction directions.
GSD_UNDETERMINED = 0
GSD_LEFT_TO_RIGHT = 1
GSD_RIGHT_TO_LEFT = 2


def guess_reaction_direction(cexp_object):
    """Guess the direction of a reaction.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :param cexp_object: The chemical equation object.
    :rtype : int
    :return: The direction descriptor.
    """

    #  Calculate the sum of the prefix coefficients of gas on the left side.
    gas_left = 0
    for substance_id in range(0, cexp_object.get_left_item_count()):
        substance = cexp_object.get_left_item(substance_id)
        substance_ast = substance.get_molecule_ast()
        if substance_ast.is_gas_status():
            gas_left += substance.get_coefficient() * substance_ast.get_prefix_number()

    #  Calculate the sum of the prefix coefficients of gas on the right side.
    gas_right = 0
    for substance_id in range(0, cexp_object.get_right_item_count()):
        substance = cexp_object.get_right_item(substance_id)
        substance_ast = substance.get_molecule_ast()
        if substance.get_molecule_ast().is_gas_status():
            gas_right += substance.get_coefficient() * substance_ast.get_prefix_number()

    #  Determine.
    if gas_left == gas_right:
        return GSD_UNDETERMINED
    elif gas_left < gas_right:
        return GSD_LEFT_TO_RIGHT
    else:
        return GSD_RIGHT_TO_LEFT
