#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import sys as _sys


def is_old_python():
    """Get whether the major version of Python runtime is less than 3.

    :rtype : bool
    :return: Return True if the runtime is old python (< 3.0). Otherwise, return False.
    """

    return _sys.version_info.major < 3


def input_prompt(prompt_str=""):
    """Input a line.

    :type prompt_str: str
    :param prompt_str: The prompt message.
    :return: The input data.
    """

    #  Show the prompt only if the standard input is a console(TTY).
    if _sys.stdin.isatty():
        pmt = prompt_str
    else:
        pmt = ""

    if is_old_python():
        # noinspection PyUnresolvedReferences
        return raw_input(pmt)
    else:
        # noinspection PyUnresolvedReferences
        return input(pmt)
