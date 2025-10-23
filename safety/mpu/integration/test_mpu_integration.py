#!/############################################################################
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

EXPECTED_RESULT = ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"]

# Run grep -rhoP "\KDECLARE_TEST\(\K(\w+)" frameworks/autocore/tests/os/task | sort | sed 's/.*/    "&",/'
# to get the follow test cases
TEST_MPU_CASES = [
    "test_user_read_nocrash",
    "test_user_write_nocrash",
    "test_user_read_crash_ksram_s",
    "test_user_read_crash_ksram_m",
    "test_user_read_crash_ksram_e",
    "test_user_write_crash_core0_kflash_s",
    "test_user_write_crash_core0_kflash_m",
    "test_user_write_crash_core0_kflash_e",
    "test_user_write_crash_core0_uflash_s",
    "test_user_write_crash_core0_uflash_m",
    "test_user_write_crash_core0_uflash_e",
    "test_user_write_crash_core1_kflash_s",
    "test_user_write_crash_core1_kflash_m",
    "test_user_write_crash_core1_kflash_e",
    "test_user_write_crash_core1_uflash_s",
    "test_user_write_crash_core1_uflash_m",
    "test_user_write_crash_core1_uflash_e",
    "test_user_write_crash_core0_ksram_s",
    "test_user_write_crash_core0_ksram_m",
    "test_user_write_crash_core0_ksram_e",
    "test_user_write_crash_core1_ksram_s",
    "test_user_write_crash_core1_ksram_m",
    "test_user_write_crash_core1_ksram_e",
    "test_user_write_crash_usram_s",
    "test_user_write_crash_usram_m",
    "test_user_write_crash_usram_e",
    "test_user_write_crash_core0_kcalib_s",
    "test_user_write_crash_core0_kcalib_m",
    "test_user_write_crash_core0_kcalib_e",
    "test_user_write_crash_core1_kcalib_s",
    "test_user_write_crash_core1_kcalib_m",
    "test_user_write_crash_core1_kcalib_e",
    "test_user_mode",
    "test_kernel_read_nocrash",
    "test_kernel_write_nocrash",
    "test_kernel_write_crash_core0_kflash_s",
    "test_kernel_write_crash_core0_kflash_m",
    "test_kernel_write_crash_core0_kflash_e",
    "test_kernel_write_crash_core0_uflash_s",
    "test_kernel_write_crash_core0_uflash_m",
    "test_kernel_write_crash_core0_uflash_e",
    "test_kernel_write_crash_core1_kflash_s",
    "test_kernel_write_crash_core1_kflash_m",
    "test_kernel_write_crash_core1_kflash_e",
    "test_kernel_write_crash_core1_uflash_s",
    "test_kernel_write_crash_core1_uflash_m",
    "test_kernel_write_crash_core1_uflash_e",
    "test_kernel_write_crash_ksram_s",
    "test_kernel_write_crash_ksram_m",
    "test_kernel_write_crash_ksram_e",
    "test_kernel_write_crash_usram_s",
    "test_kernel_write_crash_usram_m",
    "test_kernel_write_crash_usram_e",
    "test_kernel_mode",
]

TEST_MPU_CASES_SKIPPED = {
    "test_user_read_crash_ksram_s",
    "test_user_read_crash_ksram_m",
    "test_user_read_crash_ksram_e",
    "test_user_write_crash_core0_kflash_s",
    "test_user_write_crash_core0_kflash_m",
    "test_user_write_crash_core0_kflash_e",
    "test_user_write_crash_core0_uflash_s",
    "test_user_write_crash_core0_uflash_m",
    "test_user_write_crash_core0_uflash_e",
    "test_user_write_crash_core1_kflash_s",
    "test_user_write_crash_core1_kflash_m",
    "test_user_write_crash_core1_kflash_e",
    "test_user_write_crash_core1_uflash_s",
    "test_user_write_crash_core1_uflash_m",
    "test_user_write_crash_core1_uflash_e",
    "test_user_write_crash_core0_ksram_s",
    "test_user_write_crash_core0_ksram_m",
    "test_user_write_crash_core0_ksram_e",
    "test_user_write_crash_core1_ksram_s",
    "test_user_write_crash_core1_ksram_m",
    "test_user_write_crash_core1_ksram_e",
    "test_user_write_crash_usram_s",
    "test_user_write_crash_usram_m",
    "test_user_write_crash_usram_e",
    "test_user_write_crash_core0_kcalib_s",
    "test_user_write_crash_core0_kcalib_m",
    "test_user_write_crash_core0_kcalib_e",
    "test_user_write_crash_core1_kcalib_s",
    "test_user_write_crash_core1_kcalib_m",
    "test_user_write_crash_core1_kcalib_e",
    "test_kernel_write_crash_core0_kflash_s",
    "test_kernel_write_crash_core0_kflash_m",
    "test_kernel_write_crash_core0_kflash_e",
    "test_kernel_write_crash_core0_uflash_s",
    "test_kernel_write_crash_core0_uflash_m",
    "test_kernel_write_crash_core0_uflash_e",
    "test_kernel_write_crash_core1_kflash_s",
    "test_kernel_write_crash_core1_kflash_m",
    "test_kernel_write_crash_core1_kflash_e",
    "test_kernel_write_crash_core1_uflash_s",
    "test_kernel_write_crash_core1_uflash_m",
    "test_kernel_write_crash_core1_uflash_e",
    "test_kernel_write_crash_ksram_s",
    "test_kernel_write_crash_ksram_m",
    "test_kernel_write_crash_ksram_e",
    "test_kernel_write_crash_usram_s",
    "test_kernel_write_crash_usram_m",
    "test_kernel_write_crash_usram_e",
}


@pytest.mark.dep_config("CONFIG_MPU_TEST")
@pytest.mark.cmd_check("cmocka", "cmocka_mputest")
@pytest.mark.parametrize(
    "case, expected_list",
    [
        pytest.param(
            t,
            EXPECTED_RESULT,
            id=t,
            marks=pytest.mark.skip("Not Ready") if t in TEST_MPU_CASES_SKIPPED else (),
        )
        for t in TEST_MPU_CASES
    ],
)
def test_mpu_integration(case, expected_list) -> None:

    BASE_CMD = "cmocka_mputest"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand("\n", timeout=10)
    ret = pytest.product.sendCommand(cmd, expected_list, timeout=30)
    time.sleep(0.3)
    assert ret == 0
