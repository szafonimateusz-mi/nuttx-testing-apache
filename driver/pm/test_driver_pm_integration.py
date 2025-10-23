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


@pytest.mark.dep_config("CONFIG_TESTING_DRIVER_TEST", "CONFIG_PM")
@pytest.mark.cmd_check("cmocka", "cmocka_driver_pm")
def test_case_drivertest_pm_integration() -> None:
    cmd = f"cmocka -s cmocka_driver_pm -t drivertest_pm"

    ret = pytest.product.sendCommand(
        cmd, ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"], timeout=20
    )
    assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_DRIVER_TEST", "CONFIG_PM_RUNTIME")
@pytest.mark.cmd_check("cmocka", "cmocka_driver_pm_runtime")
def test_case_drivertest_pm_runtime_integration() -> None:
    cmd = f"cmocka -s cmocka_driver_pm_runtime -t drivertest_pm_runtime"

    ret = pytest.product.sendCommand(
        cmd, ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"], timeout=5
    )
    assert ret == 0
