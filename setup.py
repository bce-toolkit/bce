#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.base.version as _version
import setuptools as _setuptools

ver_major, ver_minor, ver_revision = _version.get_version()
ver_descriptor = "%d.%d.%d" % (ver_major, ver_minor, ver_revision)

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

    #  Version.
    version="%d.%d.%d" % (ver_major, ver_minor, ver_revision),

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
