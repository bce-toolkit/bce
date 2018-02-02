#!/usr/bin/env python
#
#  Copyright 2014 - 2017 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import sys as _sys


def send_message(msg):
    """Send a message to standard output.

    :type msg: str
    :param msg: The message.
    """

    #  Split the message into lines.
    lines = msg.splitlines(False)

    #  Print content lines.
    for line in lines:
        _sys.stdout.write("<" + line + "\n")

    #  Print the ending line.
    _sys.stdout.write(">\n")

    #  Flush the standard output.
    _sys.stdout.flush()


def read_message():
    """Read a message from standard input.

    :rtype: str
    :return: The message.
    """

    msg = ""
    while True:
        line = _sys.stdin.readline()
        if line.startswith("<"):
            msg += line[1:]
        elif line.startswith(">"):
            return msg
        else:
            pass
