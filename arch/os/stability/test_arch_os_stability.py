############################################################################
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.  The
# ASF licenses this file to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
############################################################################

import pytest

global_mm_count = 0
HEAP_REPEAT = 10


@pytest.mark.dep_config("CONFIG_TESTING_HEAP")
@pytest.mark.cmd_check("heap_main")
@pytest.mark.repeat(HEAP_REPEAT)
def test_mm_sta():
    global global_mm_count
    global_mm_count += 1
    ret = pytest.product.sendCommand("heap", "TEST COMPLETE", timeout=120)
    assert ret == 0
    if global_mm_count == HEAP_REPEAT:
        global_mm_count = 0


@pytest.mark.dep_config("CONFIG_TESTING_FSTEST", "CONFIG_SYSTEM_CUTERM")
@pytest.mark.cmd_check("cmd_echo", "fstest_main", "cu_main")
def test_fs_sta():
    pytest.product.sendCtrlCmd("c")
    pytest.product.sendCommand("echo V > /dev/watchdog0", "ap>", timeout=5)
    pytest.product.sendCommand("cu -l /dev/ttyTEE", timeout=5)
    fstest_dir = "{}/{}_fstest".format("/tmp", "ap")
    # rmdir fstest first
    pytest.product.sendCommand("rm -r %s" % fstest_dir, timeout=5)
    pytest.product.sendCommand("mkdir %s" % fstest_dir, timeout=5)
    ret = pytest.product.sendCommand(
        "fstest -n 1000 -m %s" % fstest_dir, "Final memory usage", timeout=600
    )
    pytest.product.sendCommand("ls %s" % fstest_dir, timeout=5)
    pytest.product.sendCommand("rm -r %s" % fstest_dir, timeout=5)
    assert ret == 0
