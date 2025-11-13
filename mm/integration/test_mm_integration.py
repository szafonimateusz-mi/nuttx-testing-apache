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

TEST_CASES = [
    pytest.param(
        "test_nuttx_mm01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_basic_test",
    ),
    pytest.param(
        "test_nuttx_mm02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_error_handling",
    ),
    pytest.param(
        "test_nuttx_mm03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_basic_test",
    ),
    pytest.param(
        "test_nuttx_mm04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_error_handling",
    ),
    pytest.param(
        "test_nuttx_mm05",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_basic_test",
    ),
    pytest.param(
        "test_nuttx_mm06",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_error_handling",
    ),
    pytest.param(
        "test_nuttx_mm07",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_basic_test",
    ),
    pytest.param(
        "test_nuttx_mm08",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="mutex_deadlock_prevention",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_mm_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_MM_TEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_mm_integration(case, expected_list, core, switch_to_core) -> None:
    """Execute mm integration tests"""

    BASE_CMD = "cmocka_mm_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=15)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_HEAP")
@pytest.mark.cmd_check("heap_main")
def test_mm():
    ret = pytest.product.sendCommand("heap", "TEST COMPLETE", timeout=30)
    assert ret == 0
