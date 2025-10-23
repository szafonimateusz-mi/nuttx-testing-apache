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

import time

import pytest


@pytest.mark.dep_config("CONFIG_FS_TEST_POWEROFF")
@pytest.mark.cmd_check(
    "power_off_test01_main", "setlogmask_main", "cmd_sleep", "cmd_reboot"
)
def test_fs_poweroff01():
    pytest.product.sendCommand("rm /data/powerOffTestFile", "")
    pytest.product.sendCommand("sleep 10", "")
    ret = pytest.product.sendCommand(
        "power_off_test01 /data &", "You can try to power off ... ...", timeout=120
    )
    assert ret == 0
    # pytest.product.sendCommand("reboot", "")
    pytest.product.reboot()
    time.sleep(200)
    pytest.product.sendCommand("setlogmask i", "")
    ret = pytest.product.sendCommand(
        "power_off_test01 /data &", "TEST PASSED", timeout=60
    )
    assert ret == 0
