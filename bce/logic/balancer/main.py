#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg
import bce.logic.balancer.direction as _bce_direct
import bce.logic.balancer.error as _bce_error
import bce.logic.balancer.merger as _bce_merger
import bce.logic.balancer.model as _bce_model
import bce.logic.balancer.option as _bce_option
import bce.logic.common.error as _cm_error
import bce.math.equation as _math_equation


def balance_chemical_equation(cexp_object, options, unknown_header="X"):
    """Balance a chemical equation.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :type options: bce.option.Option
    :type unknown_header: str
    :param cexp_object: The chemical equation object.
    :param options: The options.
    :param unknown_header: The header of unknowns.
    """

    #  Get the language ID.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

    #  Wrap the balancer options.
    balancer_opt = _bce_option.OptionWrapper(options)

    #  Get enabled features.
    is_error_correction_enabled = balancer_opt.is_error_correction_feature_enabled()
    is_auto_arranging_enabled = balancer_opt.is_auto_side_arranging_feature_enabled()

    #  Get whether the chemical equation is in auto-arranging form.
    is_auto_arranging_form = (cexp_object.get_right_item_count() == 0)

    #  Raise an error if the chemical equation is in auto-arranging form without the feature enabled.
    if is_auto_arranging_form and not is_auto_arranging_enabled:
        raise _cm_error.Error(
            _bce_error.BALANCER_FEATURE_DISABLED,
            _l10n_reg.get_message(
                lang_id,
                "logic.balancer.error.feature_disabled.auto_arranging"
            ),
            options
        )

    #  Build a matrix and backup.
    equations = _bce_model.build_model_equations(cexp_object)

    #  Solve the equation and check the answer.
    solved = _math_equation.solve_equations(equations)

    #  Post solving.
    coefficients = _bce_model.generate_balanced_coefficients(solved, header=unknown_header)

    #  Merge.
    _bce_merger.merge_coefficients_with_cexp_object(cexp_object, coefficients)

    #  Remove items with coefficient 0.
    if is_error_correction_enabled:
        cexp_object.remove_items_with_coefficient_zero()

    #  Move items that have negative coefficient to another side.
    if is_auto_arranging_form or is_error_correction_enabled:
        cexp_object.move_items_with_negative_coefficient_to_another_side()

    #  Check balancing errors in left items.
    for idx in range(0, cexp_object.get_left_item_count()):
        #  Get the coefficient.
        coefficient = cexp_object.get_left_item(idx).get_coefficient()

        #  Simplify before checking.
        coefficient = coefficient.simplify()

        #  Check.
        if coefficient.is_negative or coefficient.is_zero:
            raise _cm_error.Error(
                _bce_error.BALANCER_FEATURE_DISABLED,
                _l10n_reg.get_message(
                    lang_id,
                    "logic.balancer.error.feature_disabled.error_correction"
                ),
                options
            )

    #  Check balancing errors in right items.
    for idx in range(0, cexp_object.get_right_item_count()):
        #  Get the coefficient.
        coefficient = cexp_object.get_right_item(idx).get_coefficient()

        #  Simplify before checking.
        coefficient = coefficient.simplify()

        #  Check.
        if coefficient.is_negative or coefficient.is_zero:
            raise _cm_error.Error(
                _bce_error.BALANCER_FEATURE_DISABLED,
                _l10n_reg.get_message(
                    lang_id,
                    "logic.balancer.error.feature_disabled.error_correction"
                ),
                options
            )

    #  Integerize the coefficients.
    cexp_object.coefficients_integerize()

    #  'All-eliminated' check.
    if len(cexp_object) == 0:
        raise _cm_error.Error(
            _bce_error.BALANCER_SIDE_ELIMINATED,
            _l10n_reg.get_message(
                lang_id,
                "logic.balancer.error.side_eliminated.all"
            ),
            options
        )

    #  'Auto-arranging form with multiple answer' check.
    if is_auto_arranging_form and (cexp_object.get_left_item_count() == 0 or cexp_object.get_right_item_count() == 0):
        raise _cm_error.Error(
            _bce_error.BALANCER_SIDE_ELIMINATED,
            _l10n_reg.get_message(
                lang_id,
                "logic.balancer.error.auto_arrange_with_multiple_answers.description"
            ),
            options
        )

    #  'Left side eliminated' check.
    if cexp_object.get_left_item_count() == 0:
        raise _cm_error.Error(
            _bce_error.BALANCER_SIDE_ELIMINATED,
            _l10n_reg.get_message(
                lang_id,
                "logic.balancer.error.side_eliminated.left"
            ),
            options
        )

    #  'Right side eliminated' check.
    if cexp_object.get_right_item_count() == 0:
        raise _cm_error.Error(
            _bce_error.BALANCER_SIDE_ELIMINATED,
            _l10n_reg.get_message(
                lang_id,
                "logic.balancer.error.side_eliminated.right"
            ),
            options
        )

    #  Guess direction if the form is auto-correction.
    if is_auto_arranging_form and _bce_direct.guess_reaction_direction(cexp_object) == _bce_direct.GSD_RIGHT_TO_LEFT:
        cexp_object.flip()


def check_chemical_equation(cexp_object):
    """Check whether a chemical equation is balanced.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :param cexp_object: The chemical equation object.
    :rtype : bool
    :return: True if so.
    """

    #  Build matrix.
    mtx = _bce_model.build_model_equations(cexp_object)

    #  Generate the solution of the matrix from the expression.
    pfx_list = []
    for i in range(0, cexp_object.get_left_item_count()):
        pfx_list.append(cexp_object.get_left_item(i).get_coefficient())
    for i in range(0, cexp_object.get_right_item_count()):
        pfx_list.append(cexp_object.get_right_item(i).get_coefficient())

    #  Check whether the solution matches with the matrix.
    return _math_equation.check_answer(mtx, pfx_list)
