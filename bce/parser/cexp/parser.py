#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_cst
import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg
import bce.parser.cexp.error as _cexp_error
import bce.parser.common.error as _cm_error
import bce.parser.interface.cexp_parser as _cexp_interface
import bce.parser.interface.option as _interface_opt

#  States of the state machine.
_STATE_ROUTE_1 = 1
_STATE_READ_MINUS_1 = 2
_STATE_READ_MOLECULE = 3
_STATE_ROUTE_2 = 4
_STATE_READ_PLUS = 5
_STATE_READ_MINUS_2 = 6
_STATE_READ_SEPARATOR = 7
_STATE_READ_EQUAL_SIGN = 8

#  Chemical equation forms.
_FORM_NORMAL = 1
_FORM_AUTO_CORRECTION = 2


def _macro_register_form(expression, origin_form, new_form, options):
    """Macro of registering new form.

    :type expression: str
    :type origin_form: int
    :type new_form: int
    :type options: bce.option.Option
    :param expression: The chemical expression.
    :param origin_form: The origin form.
    :param new_form: The new form.
    :param options: The options.
    :rtype : int
    :return: The new form if no conflict exists.
    """

    #  Get the language ID.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

    if origin_form is not None and origin_form != new_form:
        err = _cm_error.Error(
            _cexp_error.CEXP_MIXED_FORM,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.mixed_form.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            0,
            len(expression) - 1,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.mixed_form.message"
            )
        )
        raise err

    return new_form


def parse(expression, token_list, options, mexp_protected_header_enabled=False, mexp_protected_header_prefix="X"):
    """Parse the tokenized chemical equation.

    :type expression: str
    :type token_list: list[bce.parser.cexp.token.Token]
    :type options: bce.option.Option
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param expression: Origin chemical equation.
    :param token_list: The tokenized chemical equation.
    :param options: The options.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.parser.interface.cexp_parser.ChemicalEquation
    :return: The parsed chemical equation.
    """

    #  Wrap the interface option.
    if_opt = _interface_opt.OptionWrapper(options)

    #  Get the language ID.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

    #  Initialize an empty chemical equation.
    ret = _cexp_interface.ChemicalEquation()

    #  Initialize the sign.
    operator = _cexp_interface.OPERATOR_PLUS

    #  Initialize the form container.
    form = None

    #  Initialize the side mark.
    #  (side == False: Left side; side == True: Right side;)
    side = False

    #  Initialize the state.
    state = _STATE_ROUTE_1

    #  Initialize other variables.
    read_molecule_end = None
    equal_sign_position = -1

    #  Initialize the token cursor.
    cursor = 0
    while True:
        token = token_list[cursor]

        if state == _STATE_ROUTE_1:
            #  Reset the operator to '+'.
            operator = _cexp_interface.OPERATOR_PLUS

            #  Redirect by rules.
            if token.is_operator_minus():
                #  Go to read the '-'.
                state = _STATE_READ_MINUS_1
            else:
                #  Go and try to read a molecule.
                read_molecule_end = _STATE_ROUTE_2
                state = _STATE_READ_MOLECULE
        elif state == _STATE_READ_MINUS_1:
            #  Register the new form.
            form = _macro_register_form(expression, form, _FORM_NORMAL, options)

            #  Set the operator to '-'.
            operator = _cexp_interface.OPERATOR_MINUS

            #  Next token.
            cursor += 1

            #  Go to read-molecule state.
            read_molecule_end = _STATE_ROUTE_2
            state = _STATE_READ_MOLECULE
        elif state == _STATE_READ_MOLECULE:
            if not token.is_molecule():
                if token.is_end():
                    if cursor == 0:
                        #  In this condition, we got an empty expression. Raise an error.
                        err = _cm_error.Error(
                            _cexp_error.CEXP_EMPTY_EXPRESSION,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.empty_expression.description"
                            ),
                            options
                        )
                        raise err
                    else:
                        #  There is no content between the end token and previous token. Raise an error.
                        err = _cm_error.Error(
                            _cexp_error.CEXP_NO_CONTENT,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.no_content.description"
                            ),
                            options
                        )
                        err.push_traceback(
                            expression,
                            token.get_position() - 1,
                            token.get_position() - 1,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.no_content.operator_after"
                            )
                        )
                        raise err
                else:
                    err = _cm_error.Error(
                        _cexp_error.CEXP_NO_CONTENT,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.cexp.error.no_content.description"
                        ),
                        options
                    )
                    if cursor == 0:
                        #  There is no content before this token. Raise an error.
                        err.push_traceback(
                            expression,
                            token.get_position(),
                            token.get_position() + len(token.get_symbol()) - 1,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.no_content.operator_before"
                            )
                        )
                    else:
                        #  There is no content between this token and previous token. Raise an error.
                        err.push_traceback(
                            expression,
                            token.get_position() - 1,
                            token.get_position() + len(token.get_symbol()) - 1,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.no_content.operator_between"
                            )
                        )
                    raise err

            try:
                #  Get the molecule parser.
                ml_parser = if_opt.get_molecule_parser()

                #  Parse the molecule.
                ml_ast_root = ml_parser.parse_expression(
                    token.get_symbol(),
                    options,
                    mexp_protected_header_enabled=mexp_protected_header_enabled,
                    mexp_protected_header_prefix=mexp_protected_header_prefix
                )

                #  Separate the coefficient from the AST.
                ml_coefficient = ml_ast_root.get_prefix_number()
                ml_ast_root.set_prefix_number(_math_cst.ONE)

                #  Parse the AST.
                ml_atoms_dict = ml_parser.parse_ast(
                    token.get_symbol(),
                    ml_ast_root,
                    options,
                    mexp_protected_header_enabled=mexp_protected_header_enabled,
                    mexp_protected_header_prefix=mexp_protected_header_prefix
                )

                #  Add the molecule to the chemical equation.
                if side:
                    ret.append_right_item(operator, ml_coefficient, ml_ast_root, ml_atoms_dict)
                else:
                    ret.append_left_item(operator, ml_coefficient, ml_ast_root, ml_atoms_dict)
            except _cm_error.Error as err:
                #  Add error description.
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.cexp.error.parsing_molecule.message"
                    )
                )
                raise err

            #  Next token.
            cursor += 1

            #  Redirect by pre-saved state.
            state = read_molecule_end
        elif state == _STATE_ROUTE_2:
            #  Redirect by rules.
            if token.is_operator_plus():
                state = _STATE_READ_PLUS
            elif token.is_operator_minus():
                state = _STATE_READ_MINUS_2
            elif token.is_operator_separator():
                state = _STATE_READ_SEPARATOR
            elif token.is_equal():
                state = _STATE_READ_EQUAL_SIGN
            elif token.is_end():
                break
            else:
                raise RuntimeError("BUG: Unexpected token (should never happen).")
        elif state == _STATE_READ_PLUS:
            #  Register the new form.
            form = _macro_register_form(expression, form, _FORM_NORMAL, options)

            #  Set the operator to '+'.
            operator = _cexp_interface.OPERATOR_PLUS

            #  Next token.
            cursor += 1

            #  Go to read-molecule state.
            read_molecule_end = _STATE_ROUTE_2
            state = _STATE_READ_MOLECULE
        elif state == _STATE_READ_MINUS_2:
            #  Register the new form.
            form = _macro_register_form(expression, form, _FORM_NORMAL, options)

            #  Set the operator to '-'.
            operator = _cexp_interface.OPERATOR_MINUS

            #  Next token.
            cursor += 1

            #  Go to read-molecule state.
            read_molecule_end = _STATE_ROUTE_2
            state = _STATE_READ_MOLECULE
        elif state == _STATE_READ_SEPARATOR:
            #  Register the new form.
            form = _macro_register_form(expression, form, _FORM_AUTO_CORRECTION, options)

            #  Set the operator to '+'.
            operator = _cexp_interface.OPERATOR_PLUS

            #  Next token.
            cursor += 1

            #  Go to read-molecule state.
            read_molecule_end = _STATE_ROUTE_2
            state = _STATE_READ_MOLECULE
        elif state == _STATE_READ_EQUAL_SIGN:
            #  Register the new form.
            form = _macro_register_form(expression, form, _FORM_NORMAL, options)

            #  Next token.
            cursor += 1

            #  Raise an error if the equal sign is duplicated.
            if side:
                err = _cm_error.Error(
                    _cexp_error.CEXP_DUPLICATED_EQUAL_SIGN,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.cexp.error.duplicated_equal_sign.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.cexp.error.duplicated_equal_sign.duplicated"
                    )
                )
                err.push_traceback(
                    expression,
                    equal_sign_position,
                    equal_sign_position,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.cexp.error.duplicated_equal_sign.previous"
                    )
                )
                raise err

            #  Save the position of the equal sign.
            equal_sign_position = token.get_position()

            #  Mark the side flag.
            side = True

            #  Go to route 1.
            state = _STATE_ROUTE_1
        else:
            raise RuntimeError("BUG: Unexpected state.")

    #  Raise an error if there is only 1 molecule.
    if len(ret) == 1:
        err = _cm_error.Error(
            _cexp_error.CEXP_ONLY_ONE_MOLECULE,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.only_one_molecule.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            0,
            len(expression) - 1,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.only_one_molecule.message"
            )
        )
        raise err

    #  Check form.
    if form is None:
        raise RuntimeError("BUG: Form was not set.")

    #  Raise an error if there is no equal sign (for normal form only).
    if form == _FORM_NORMAL and not side:
        err = _cm_error.Error(
            _cexp_error.CEXP_NO_EQUAL_SIGN,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.no_equal_sign.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            0,
            len(expression) - 1,
            _l10n_reg.get_message(
                lang_id,
                "parser.cexp.error.no_equal_sign.message"
            )
        )
        raise err

    return ret
