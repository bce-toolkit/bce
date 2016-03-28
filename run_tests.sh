#!/usr/bin/env sh
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

for test_module in `cat "test/modules.lst"`; do
    python -B -m unittest --verbose "$test_module"
    if [ "$?" != "0" ]; then
        exit 1
    fi
done

exit 0
