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
        "test_case_fdsan_unowned_untagged_close",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="fdsan_unowned_untagged_close",
    ),
    pytest.param(
        "test_case_unowned_tagged_close",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="unowned_tagged_close",
    ),
    pytest.param(
        "test_case_owned_tagged_close",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="owned_tagged_close",
    ),
    pytest.param(
        "test_case_overflow",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="overflow",
    ),
    pytest.param(
        "test_case_vfork",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="vfork",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_fdsan_simple")
@pytest.mark.dep_config("CONFIG_TESTING_FDSAN_TEST", "CONFIG_TESTING_FDSAN_TEST_SIMPLE")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_fdsan_simple_integration(case, expected_list) -> None:
    """Execute fdsan simple integration tests"""

    BASE_CMD = "cmocka_fdsan_simple"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=5)
    assert ret == 0
