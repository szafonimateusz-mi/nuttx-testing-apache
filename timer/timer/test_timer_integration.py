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
        "test_nuttx_clock_test_smoke01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_smoke01",
    ),
    pytest.param(
        "test_nuttx_clock_test_timer01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_timer01",
    ),
    pytest.param(
        "test_nuttx_clock_test_timer03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_timer03",
    ),
    pytest.param(
        "test_nuttx_clock_test_timer04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_timer04",
    ),
    pytest.param(
        "test_nuttx_clock_test_timer05",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_timer05",
    ),
    pytest.param(
        "test_nuttx_clock_test_clock01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_clock01",
    ),
    pytest.param(
        "test_nuttx_clock_test_clock02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_nuttx_clock_test_clock02",
    ),
]


@pytest.mark.dep_config("CONFIG_CM_TIME_TEST")
@pytest.mark.cmd_check("cmocka", "cmocka_time_test")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_nuttx_clock_test_clock_02_integration(
    case, expected_list, core, switch_to_core
) -> None:

    BASE_CMD = "cmocka_time_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    assert ret == 0
