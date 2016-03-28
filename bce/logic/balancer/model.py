#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.matrix as _math_matrix
import bce.math.constant as _math_constant
import sympy as _sympy


def build_model_equations(cexp_object):
    """Build model equations from the a chemical equation.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :param cexp_object: The chemical equation object.
    :rtype : bce.math.matrix.Matrix
    :return: The model equations matrix.
    """

    #  A dictionary that contains the row index of each atom / electronic.
    ref_atom_idx = {}

    #  Row index counter.
    ref_atom_counter = 0

    #  Calculate the row index of each atom.
    #  Process left items.
    for idx in range(0, cexp_object.get_left_item_count()):
        #  Get the atom dictionary of the molecule.
        atom_dict = cexp_object.get_left_item(idx).get_atoms_dictionary()

        #  Process atoms.
        for atom_symbol in atom_dict:
            if atom_symbol not in ref_atom_idx:
                #  Write the row index of the atom and increase the row counter.
                ref_atom_idx[atom_symbol] = ref_atom_counter
                ref_atom_counter += 1

    #  Process right items.
    for idx in range(0, cexp_object.get_right_item_count()):
        #  Get the atom dictionary of the molecule.
        atom_dict = cexp_object.get_right_item(idx).get_atoms_dictionary()

        #  Process atoms.
        for atom_symbol in atom_dict:
            if atom_symbol not in ref_atom_idx:
                #  Write the row index of the atom and increase the row counter.
                ref_atom_idx[atom_symbol] = ref_atom_counter
                ref_atom_counter += 1

    #  Build an empty matrix that only contains zero.
    mtx = _math_matrix.Matrix(len(ref_atom_idx), len(cexp_object) + 1, _math_constant.ZERO)

    #  Initialize column index counter.
    column_id = 0

    #  Process items on the left side.
    for idx in range(0, cexp_object.get_left_item_count()):
        #  Get the item.
        item = cexp_object.get_left_item(idx)

        #  Get the atom dictionary of the molecule.
        atom_dict = item.get_atoms_dictionary()

        for atom in atom_dict:
            #  Write the count of each atom to specific position.
            if item.is_operator_plus():
                mtx.write_item_by_position(ref_atom_idx[atom], column_id, atom_dict[atom])
            else:
                mtx.write_item_by_position(ref_atom_idx[atom], column_id, -atom_dict[atom])

        #  Increase the column counter.
        column_id += 1

    #  Process items on the right side.
    for idx in range(0, cexp_object.get_right_item_count()):
        #  Get the item.
        item = cexp_object.get_right_item(idx)

        #  Get the atom dictionary of the molecule.
        atom_dict = item.get_atoms_dictionary()

        for atom in atom_dict:
            #  Write the count of each atom to specific position.
            if item.is_operator_plus():
                mtx.write_item_by_position(ref_atom_idx[atom], column_id, -atom_dict[atom])
            else:
                mtx.write_item_by_position(ref_atom_idx[atom], column_id, atom_dict[atom])

        #  Increase the column counter.
        column_id += 1

    return mtx


def generate_balanced_coefficients(solution, header="X"):
    """Generate balanced coefficients from the result of equations.

    :type solution: bce.math.equation.SolutionSystem
    :type header: str
    :param solution: The solution system of the model equations.
    :param header: The header of unknown symbols.
    :rtype : list
    :return: The coefficients list.
    """

    #  Get the constant vector and the base vectors.
    const_vector = solution.get_constant_vector()
    base_vectors = solution.get_base_vectors()

    #  Initialize the result container.
    result = []

    #  Treat single-solution condition.
    if base_vectors.get_column_count() == 1:
        #  Check the constant vector.
        non_zero = False
        for value in const_vector:
            #  Simplify.
            value = value.simplify()

            #  Check.
            if not value.is_zero:
                non_zero = True
                break

        if not non_zero:
            #  Copy the base vector to the result list.
            for idx in range(0, solution.get_length()):
                #  Get the value.
                value = base_vectors.get_item_by_position(idx, 0)

                #  Simplify.
                value = value.simplify()

                #  Append the value to the list.
                result.append(value)

            return result

    #  Treat multiple-solutions condition.
    for idx in range(0, solution.get_length()):
        #  Calculate the sum.
        sum_value = const_vector[idx]
        for base_id in range(0, base_vectors.get_column_count()):
            sum_value += base_vectors.get_item_by_position(idx, base_id) * \
                         _sympy.Symbol(header + _convert_unknown_id_to_symbol(base_id))

        #  Simplify.
        sum_value = sum_value.simplify()

        #  Append the sum to the result list.
        result.append(sum_value)

    return result


def _convert_unknown_id_to_symbol(unknown_id):
    """Get the symbol of an unknown.

    :type unknown_id: int
    :param unknown_id: The ID of the unknown.
    :rtype : str
    :return: The symbol.
    """

    #  If the |unknown_id| is zero, just returns |PROTECT_HEADER|a.
    if unknown_id == 0:
        return "a"

    #  Initialize alphabet table.
    ch_table = "abcdefghijklmnopqrstuvwxyz"
    ch_table_len = len(ch_table)

    #  Convert decimal to 26 ary.
    cur_id = unknown_id
    r = ""

    while cur_id != 0:
        r = ch_table[cur_id % ch_table_len] + r
        cur_id = int(cur_id / ch_table_len)

    return r
