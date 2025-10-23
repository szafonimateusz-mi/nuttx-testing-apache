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
        "test_nuttx_syscall_chdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_chdir01",
    ),
    pytest.param(
        "test_nuttx_syscall_chdir02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_chdir02",
    ),
    pytest.param(
        "test_nuttx_syscall_getitimer01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getitimer01",
    ),
    pytest.param(
        "test_nuttx_syscall_clockgettime01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_clockgettime01",
    ),
    pytest.param(
        "test_nuttx_syscall_clocknanosleep01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_clocknanosleep01",
    ),
    pytest.param(
        "test_nuttx_syscall_clocksettime01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_clocksettime01",
    ),
    pytest.param(
        "test_nuttx_syscall_close01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_close01",
    ),
    pytest.param(
        "test_nuttx_syscall_close02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_close02",
    ),
    pytest.param(
        "test_nuttx_syscall_close03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_close03",
    ),
    pytest.param(
        "test_nuttx_syscall_creat01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_creat01",
    ),
    pytest.param(
        "test_nuttx_syscall_creat02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_creat02",
    ),
    pytest.param(
        "test_nuttx_syscall_fcntl02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fcntl02",
    ),
    pytest.param(
        "test_nuttx_syscall_fcntl03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fcntl03",
    ),
    pytest.param(
        "test_nuttx_syscall_fcntl04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fcntl04",
    ),
    pytest.param(
        "test_nuttx_syscall_fstatfs01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fstatfs01",
    ),
    pytest.param(
        "test_nuttx_syscall_fsync01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fsync01",
    ),
    pytest.param(
        "test_nuttx_syscall_fsync02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fsync02",
    ),
    pytest.param(
        "test_nuttx_syscall_fsync03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fsync03",
    ),
    pytest.param(
        "test_nuttx_syscall_getpeername01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getpeername01",
    ),
    pytest.param(
        "test_nuttx_syscall_getsockopt01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getsockopt01",
    ),
    pytest.param(
        "test_nuttx_syscall_setsockopt01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_setsockopt01",
    ),
    pytest.param(
        "test_nuttx_syscall_listen01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_listen01",
    ),
    pytest.param(
        "test_nuttx_syscall_ftruncate01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_ftruncate01",
    ),
    pytest.param(
        "test_nuttx_syscall_getcwd01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getcwd01",
    ),
    pytest.param(
        "test_nuttx_syscall_getcwd02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getcwd02",
    ),
    pytest.param(
        "test_nuttx_syscall_getpid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getpid01",
    ),
    pytest.param(
        "test_nuttx_syscall_getppid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getppid01",
    ),
    pytest.param(
        "test_nuttx_syscall_gethostname01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_gethostname01",
    ),
    pytest.param(
        "test_nuttx_syscall_gettimeofday01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_gettimeofday01",
    ),
    pytest.param(
        "test_nuttx_syscall_lseek01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_lseek01",
    ),
    pytest.param(
        "test_nuttx_syscall_lseek07",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_lseek07",
    ),
    pytest.param(
        "test_nuttx_syscall_lstat01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_lstat01",
    ),
    pytest.param(
        "test_nuttx_syscall_dup01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup01",
    ),
    pytest.param(
        "test_nuttx_syscall_dup02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup02",
    ),
    pytest.param(
        "test_nuttx_syscall_dup03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup03",
    ),
    pytest.param(
        "test_nuttx_syscall_dup04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup04",
    ),
    pytest.param(
        "test_nuttx_syscall_dup05",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup05",
    ),
    pytest.param(
        "test_nuttx_syscall_dup201",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup201",
    ),
    pytest.param(
        "test_nuttx_syscall_dup202",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_dup202",
    ),
    pytest.param(
        "test_nuttx_syscall_fpathconf01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_fpathconf01",
    ),
    pytest.param(
        "test_nuttx_syscall_getegid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getegid01",
    ),
    pytest.param(
        "test_nuttx_syscall_getegid02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getegid02",
    ),
    pytest.param(
        "test_nuttx_syscall_geteuid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_geteuid01",
    ),
    pytest.param(
        "test_nuttx_syscall_getgid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getgid01",
    ),
    pytest.param(
        "test_nuttx_syscall_getgid02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getgid02",
    ),
    pytest.param(
        "test_nuttx_syscall_getuid01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_getuid01",
    ),
    pytest.param(
        "test_nuttx_syscall_pathconf01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pathconf01",
    ),
    pytest.param(
        "test_nuttx_syscall_pipe01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pipe01",
    ),
    pytest.param(
        "test_nuttx_syscall_pipe02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pipe02",
    ),
    pytest.param(
        "test_nuttx_syscall_pread01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pread01",
    ),
    pytest.param(
        "test_nuttx_syscall_rmdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_rmdir01",
    ),
    pytest.param(
        "test_nuttx_syscall_rmdir02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_rmdir02",
    ),
    pytest.param(
        "test_nuttx_syscall_truncate01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        marks=pytest.mark.skip("Not Ready"),
        id="syscall_truncate01",
    ),
    pytest.param(
        "test_nuttx_syscall_unlink01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_unlink01",
    ),
    pytest.param(
        "test_nuttx_syscall_nansleep01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_nansleep01",
    ),
    pytest.param(
        "test_nuttx_syscall_nansleep02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_nansleep02",
    ),
    pytest.param(
        "test_nuttx_syscall_time01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_time01",
    ),
    pytest.param(
        "test_nuttx_syscall_time02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_time02",
    ),
    pytest.param(
        "test_nuttx_syscall_timercreate01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_timercreate01",
    ),
    pytest.param(
        "test_nuttx_syscall_timerdelete01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_timerdelete01",
    ),
    pytest.param(
        "test_nuttx_syscall_timergettime01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_timergettime01",
    ),
    pytest.param(
        "test_nuttx_syscall_mkdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_mkdir01",
    ),
    pytest.param(
        "test_nuttx_syscall_mkdir02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_mkdir02",
    ),
    pytest.param(
        "test_nuttx_syscall_mkdir03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_mkdir03",
    ),
    pytest.param(
        "test_nuttx_syscall_sched01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_sched01",
    ),
    pytest.param(
        "test_nuttx_syscall_sched02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_sched02",
    ),
    pytest.param(
        "test_nuttx_syscall_sched03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_sched03",
    ),
    pytest.param(
        "test_nuttx_syscall_pwrite01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pwrite01",
    ),
    pytest.param(
        "test_nuttx_syscall_pwrite02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_pwrite02",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_syscall_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_SYSCALL_TEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_syscall_integration(case, expected_list, core, switch_to_core) -> None:
    """Execute syscall integration tests"""

    BASE_CMD = "cmocka_syscall_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=300)
    assert ret == 0


TEST_CASES_2 = [
    pytest.param(
        "test_nuttx_syscall_socketpair02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="syscall_socketpair02",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_syscall_test")
@pytest.mark.dep_config(
    "CONFIG_TESTS_TESTSUITES", "CONFIG_CM_SYSCALL_TEST", "CONFIG_NET_LOCAL_DGRAM"
)
@pytest.mark.parametrize("case, expected_list", TEST_CASES_2)
def test_syscall_socketpair_integration(
    case, expected_list, core, switch_to_core
) -> None:
    """Execute syscall integration tests"""

    BASE_CMD = "cmocka_syscall_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=120)
    assert ret == 0
