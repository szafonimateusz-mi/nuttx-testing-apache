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
    # test_nuttx_sched_pthread
    pytest.param(
        "test_nuttx_sched_pthread01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_01",
    ),
    pytest.param(
        "test_nuttx_sched_pthread02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_02",
    ),
    pytest.param(
        "test_nuttx_sched_pthread03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_03",
    ),
    pytest.param(
        "test_nuttx_sched_pthread04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_04",
    ),
    pytest.param(
        "test_nuttx_sched_pthread05",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_05",
    ),
    pytest.param(
        "test_nuttx_sched_pthread06",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_06",
    ),
    pytest.param(
        "test_nuttx_sched_pthread07",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_07",
    ),
    pytest.param(
        "test_nuttx_sched_pthread08",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_08",
    ),
    pytest.param(
        "test_nuttx_sched_pthread09",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_pthread_operations_09",
    ),
    # test_nuttx_sched_task
    pytest.param(
        "test_nuttx_sched_task01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_01",
    ),
    pytest.param(
        "test_nuttx_sched_task02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_02",
    ),
    pytest.param(
        "test_nuttx_sched_task03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_03",
    ),
    pytest.param(
        "test_nuttx_sched_task04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_04",
    ),
    pytest.param(
        "test_nuttx_sched_task05",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_05",
    ),
    pytest.param(
        "test_nuttx_sched_task06",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_06",
    ),
    pytest.param(
        "test_nuttx_sched_task07",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_task_operations_07",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_sched_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_SCHED_TEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_sched_integration(case, expected_list, core, switch_to_core) -> None:
    """Execute sched integration tests"""

    BASE_CMD = "cmocka_sched_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    assert ret == 0


TEST_CASES_2 = [
    pytest.param(
        "test_work_notifier_signal",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_notifier_signal",
    ),
    pytest.param(
        "test_work_notifier_teardown",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="sched_notifier_teardown",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_sched_wqueue")
@pytest.mark.dep_config("CONFIG_TESTING_SCHEDTEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES_2)
def test_sched_wqueue(case, expected_list) -> None:
    """Execute sched wqueue tests"""

    BASE_CMD = "cmocka_sched_wqueue"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    assert ret == 0
