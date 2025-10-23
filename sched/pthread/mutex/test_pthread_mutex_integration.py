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
        "TestNuttxMutexTest01",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="TestNuttxMutexTest01",
    ),
    pytest.param(
        "TestNuttxMutexTest19",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="TestNuttxMutexTest19",
    ),
    pytest.param(
        "TestNuttxMutexTest20", "Cmocka Test Completed", id="TestNuttxMutexTest20"
    ),
]


@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_MUTEX_TEST")
@pytest.mark.cmd_check("cmocka", "cmocka_mutex_test")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_pthread_mutex_integration(case, expected_list) -> None:
    """Execute pthread mutex integration tests"""

    BASE_CMD = "cmocka_mutex_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=10)
    assert ret == 0
