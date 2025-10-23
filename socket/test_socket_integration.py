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
    # TestNuttxNetSocketTest
    pytest.param(
        "TestNuttxNetSocketTest05",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="Byte_order",
    ),
    pytest.param(
        "TestNuttxNetSocketTest06",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="IP_addressing",
    ),
    pytest.param(
        "TestNuttxNetSocketTest08",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="Multi-threading_networking",
    ),
    pytest.param(
        "TestNuttxNetSocketTest09",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="Polling_server",
    ),
    pytest.param(
        "TestNuttxNetSocketTest10",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="Socket_operation",
    ),
    pytest.param(
        "TestNuttxNetSocketTest11",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="Socket_handling",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_socket_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_SOCKET_TEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_socket_integration(case, expected_list) -> None:
    """Execute socket integration tests"""

    BASE_CMD = "cmocka_socket_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=5)
    assert ret == 0
