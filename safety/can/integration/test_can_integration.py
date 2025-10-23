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

TEST_CASES = [
    pytest.param(
        "test_char_can_controller",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_char_can_controller",
    ),
    pytest.param(
        "test_char_can_transceiver",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        marks=pytest.mark.skip("Not Ready"),
        id="test_char_can_transceiver",
    ),
    pytest.param(
        "test_charcan_multi_echo",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_charcan_multi_echo",
    ),
    pytest.param(
        "test_charcan_nonblock_sent_overflow",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_charcan_nonblock_sent_overflow",
    ),
    pytest.param(
        "test_char_can_poll",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="test_char_can_poll",
    ),
]


@pytest.mark.dep_config("CONFIG_TESTING_CHARCAN")
@pytest.mark.cmd_check("cmocka", "cmocka_canecho")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_can_integration(case, expected_list) -> None:

    BASE_CMD = "cmocka_canecho"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand("\n", timeout=10)
    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    time.sleep(0.3)
    assert ret == 0
