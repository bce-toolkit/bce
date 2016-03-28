#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import os as _os
import setuptools as _setuptools
import sys as _sys

#
#  Note:
#    [1] Do NOT import "bce" package in this installation script. Due to the fact
#        that "bce" package would import other third-party libraries as well. An
#        error would occurred when one of these libraries wasn't installed.
#


#
#  Routine(s) copied from "bce.utils.compatible" package.
#
def is_old_python():
    """Get whether the major version of Python runtime is less than 3.

    :rtype : bool
    :return: Return True if the runtime is old python (< 3.0). Otherwise, return False.
    """

    return _sys.version_info.major < 3


#
#  Routine(s) copied from "bce.utils.file_io" package.
#
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
        if is_old_python():
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


def get_version():
    """Get the version from "bce.base.version" package.

    :rtype : (int, int, int)
    :return: A tuple (Major, Minor, Revision).
    """

    #  Get the content of "bce.base.version".
    version_py = read_text_file(_os.path.join(
        _os.path.abspath(_os.path.dirname(__file__)),
        "bce",
        "base",
        "version.py"
    ))
    if version_py is None:
        raise RuntimeError("Can't read the software version.")

    #  Execute the Python script.
    ctx = {}
    exec(version_py, ctx, ctx)

    return ctx["get_version"]()

#
#  Setup.
#

VER_MAJOR, VER_MINOR, VER_REVISION = get_version()

_setuptools.setup(
    #  Base information.
    name="bce",
    author="The BCE Authors",
    author_email="xiaojsoft@gmail.com",
    description="A chemical equation balancer.",
    long_description="A program that can balance chemical equations and help you deal with complex chemical equations.",
    license="BSD",
    keywords=["bce", "chemistry", "chemical", "equation"],
    url="https://github.com/TaikiAkita/BCE",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Chemistry"
    ],
    include_package_data=True,

    #  Version.
    version="%d.%d.%d" % (VER_MAJOR, VER_MINOR, VER_REVISION),

    #   Packages and dependencies.
    packages=_setuptools.find_packages(),
    install_requires=[
        "sympy>=0.7.3"
    ],

    #  Entry points.
    entry_points={
        "console_scripts": [
            "bce-console = bce.shell.console.main:main"
        ]
    }
)
