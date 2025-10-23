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
        "test_nuttx_pthread_test03",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test03",
    ),
    pytest.param(
        "test_nuttx_pthread_test04",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test04",
    ),
    pytest.param(
        "test_nuttx_pthread_test05",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test05",
    ),
    pytest.param(
        "test_nuttx_pthread_test06",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test06",
    ),
    pytest.param(
        "test_nuttx_pthread_test09",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test09",
    ),
    pytest.param(
        "test_nuttx_pthread_test18",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test18",
    ),
    pytest.param(
        "test_nuttx_pthread_test19",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test19",
    ),
    pytest.param(
        "test_nuttx_pthread_test21",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_nuttx_pthread_test21",
    ),
]


@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_PTHREAD_TEST")
@pytest.mark.cmd_check("cmocka", "cmocka_pthread_test")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_pthread_integration(case, expected_list, core, switch_to_core) -> None:
    """Execute pthread mutex integration tests"""

    BASE_CMD = "cmocka_pthread_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    assert ret == 0
