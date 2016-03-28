#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.base.version as _version
import bce.locale.registry as _l10n_registry
import bce.public.api as _public_api
import bce.public.database as _public_db
import bce.public.exception as _public_exception
import bce.public.option as _public_option
import bce.public.printer as _public_printer
import bce.shell.console.l10n as _shell_l10n
import bce.utils.compatible as _utils_compatible
import bce.utils.file_io as _utils_file_io
import bce.utils.input_checker as _utils_input_chk
import bce.option as _option
import argparse as _argparse
import copy as _copy
import json as _json
import signal as _signal
import sys as _sys


def is_valid_unknown_header(header):
    """Check whether characters of a header are all valid.

    :type header: str
    :rtype : bool
    :param header: The header.
    :return: True if so.
    """

    #  Construct valid characters.
    valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    #  Check all characters.
    for ch in header:
        if valid_char.find(ch) == -1:
            return False

    return True


# noinspection PyUnusedLocal
def exit_signal_handler(signal, frame):
    """The handler for the exit signal.

    :param signal: The signal.
    :param frame: The calling frame.
    """

    print("")

    _sys.exit(0)


def main():
    """Main entry of the BCE console shell."""

    #  Initialize the localization module.
    _shell_l10n.setup_localization()

    #  Capture SIGINT signal.
    _signal.signal(_signal.SIGINT, exit_signal_handler)

    #  Initialize a new option instance.
    option = _option.Option()

    #  Wrap the localization options.
    l10n_option = _public_option.LocaleOptionWrapper(option)

    #  Wrap the balancer options.
    balancer_option = _public_option.BalancerOptionWrapper(option)

    #  Create an argument parser and do parsing.
    arg_parser = _argparse.ArgumentParser(
        description=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.header"
        )
    )
    arg_parser.add_argument(
        "--output-mathml",
        dest="output_mathml",
        action="store_const",
        const=True,
        default=False,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.output_mathml"
        )
    )
    arg_parser.add_argument(
        "--disable-banner",
        dest="show_banner",
        action="store_const",
        const=False,
        default=True,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.disable_banner"
        )
    )
    arg_parser.add_argument(
        "--disable-bundled-abbreviations",
        dest="use_bundled_abbreviations",
        action="store_const",
        const=False,
        default=True,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.disable_bundled_abbreviations"
        )
    )
    arg_parser.add_argument(
        "--disable-error-correction",
        dest="enable_error_correction",
        action="store_const",
        const=False,
        default=True,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.disable_error_correction"
        )
    )
    arg_parser.add_argument(
        "--disable-auto-arranging",
        dest="enable_auto_arranging",
        action="store_const",
        const=False,
        default=True,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.disable_auto_arranging"
        )
    )
    arg_parser.add_argument(
        "--unknown-header",
        dest="unknown_header",
        action="store",
        type=str,
        default="X",
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.unknown_header"
        )
    )
    arg_parser.add_argument(
        "--load-abbreviations-file",
        dest="abbreviations_file",
        action="store",
        type=str,
        default=None,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.load_abbreviations_file"
        )
    )
    arg_parser.add_argument(
        "--language",
        dest="language",
        action="store",
        type=str,
        default=l10n_option.get_language_id(),
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.language"
        )
    )
    arg_parser.add_argument(
        "--version",
        dest="show_version",
        action="store_const",
        const=True,
        default=False,
        help=_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.command.show_version"
        )
    )
    args = arg_parser.parse_args()

    #  Set the language.
    l10n_option.set_language_id(args.language)

    #  Enable / disable all balancer features.
    balancer_option.enable_error_correction_feature(args.enable_error_correction)
    balancer_option.enable_auto_side_arranging_feature(args.enable_auto_arranging)

    #  Get the software version.
    ver_major, ver_minor, ver_revision = _version.get_version()

    #  Show the version.
    if args.show_version:
        print(_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.application.version",
            replace_map={
                "$1": str(ver_major),
                "$2": str(ver_minor),
                "$3": str(ver_revision)
            }
        ))
        _sys.exit(0)

    #  Show the banner.
    if args.show_banner and _sys.stdin.isatty():
        print(_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.application.banner",
            replace_map={
                "$1": str(ver_major),
                "$2": str(ver_minor),
                "$3": str(ver_revision)
            }
        ))
        print(_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.application.copyright"
        ))

    #  Get and check the unknown header.
    unknown_header = args.unknown_header
    assert isinstance(unknown_header, str)
    unknown_header = unknown_header.strip()
    if len(unknown_header) == 0 or not is_valid_unknown_header(unknown_header):
        print(_l10n_registry.get_message(
            l10n_option.get_language_id(),
            "shell.console.error.invalid_unknown_header.description"
        ))
        _sys.exit(1)

    #  Initialize abbreviations.
    abbreviations = {}

    #  Load bundled abbreviations.
    if args.use_bundled_abbreviations:
        abbreviations = _copy.deepcopy(_public_db.BUNDLED_ABBREVIATION_DATABASE)

    #  Load extra abbreviations file.
    extra_arv_file_path = args.abbreviations_file
    if extra_arv_file_path is not None:
        #  Read the file.
        extra_arv_file_content = _utils_file_io.read_text_file(extra_arv_file_path)
        if extra_arv_file_content is None:
            print(_l10n_registry.get_message(
                l10n_option.get_language_id(),
                "shell.console.error.file_reading_error.description",
                replace_map={
                    "$1": extra_arv_file_path
                }
            ))
            _sys.exit(1)

        #  Parse the file.
        extra_abbreviations = {}
        try:
            extra_abbreviations = _json.loads(extra_arv_file_content)
        except ValueError:
            print(_l10n_registry.get_message(
                l10n_option.get_language_id(),
                "shell.console.error.file_corrupted.description",
                replace_map={
                    "$1": extra_arv_file_path
                }
            ))
            _sys.exit(1)

        #  Check.
        if not isinstance(extra_abbreviations, dict):
            print(_l10n_registry.get_message(
                l10n_option.get_language_id(),
                "shell.console.error.file_corrupted.description",
                replace_map={
                    "$1": extra_arv_file_path
                }
            ))
            _sys.exit(1)

        for arv_name in extra_abbreviations:
            #  Get the abbreviation expression.
            arv_expression = extra_abbreviations[arv_name]

            #  Convert unicode to string in Python 2.
            if _utils_compatible.is_old_python():
                # noinspection PyUnresolvedReferences
                if isinstance(arv_name, unicode):
                    arv_name = str(arv_name)
                # noinspection PyUnresolvedReferences
                if isinstance(arv_expression, unicode):
                    arv_expression = str(arv_expression)

            #  Check.
            if not (isinstance(arv_expression, str) and
                    _utils_input_chk.check_input_expression_characters(arv_expression)):
                print(_l10n_registry.get_message(
                    l10n_option.get_language_id(),
                    "shell.console.error.file_corrupted.description",
                    replace_map={
                        "$1": extra_arv_file_path
                    }
                ))
                _sys.exit(1)

            #  Save the abbreviation.
            abbreviations[arv_name] = arv_expression

    #  Set abbreviations in the option object.
    _public_option.MoleculeParserOptionWrapper(option).set_abbreviation_mapping(abbreviations)

    while True:
        #  Input a chemical equation / expression.
        try:
            expression = _utils_compatible.input_prompt(">> ").replace(" ", "")
        except EOFError:
            break

        #  Ignore zero-length expressions and comment lines.
        if len(expression) == 0 or expression[0] == "#":
            continue

        #  Balance chemical equation / expression and print it out.
        try:
            printer_id = _public_printer.PRINTER_TEXT
            if args.output_mathml:
                printer_id = _public_printer.PRINTER_MATHML
            result = _public_api.balance_chemical_equation(
                expression,
                option,
                printer=printer_id,
                unknown_header=unknown_header
            )
            print(result)
        except _public_exception.ParserErrorWrapper as err:
            print(str(err))
        except _public_exception.LogicErrorWrapper as err:
            print(str(err))
        except _public_exception.InvalidCharacterException:
            print(_l10n_registry.get_message(
                l10n_option.get_language_id(),
                "shell.console.error.invalid_character.description"
            ))

    #  Print an empty line.
    print("")

    _sys.exit(0)
