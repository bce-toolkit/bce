#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.utils.compatible as _utils_compatible


def read_text_file(file_path, encoding="utf-8"):
    """Read a text file.

    :type file_path: str
    :type encoding: str
    :param file_path: The file path.
    :param encoding: The file encoding.
    :rtype : str | None
    :return: The file content. (None if failed.)
    """

    #  Initialize the handler.
    handler = None

    # noinspection PyBroadException
    try:
        if _utils_compatible.is_old_python():
            handler = open(file_path, "r")
        else:
            handler = open(file_path, "r", encoding=encoding)
        content = handler.read()
        handler.close()
    except Exception:
        #  Close if possible.
        if handler is not None and not handler.closed:
            handler.close()

        #  Clear the content.
        content = None

    return content
