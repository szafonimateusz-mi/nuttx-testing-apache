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


@pytest.mark.dep_config(
    "CONFIG_TESTING_DRIVER_TEST", "CONFIG_TESTING_DRIVER_TEST_SIMPLE"
)
@pytest.mark.cmd_check("cmocka", "cmocka_driver_simple")
class TestDriverSimple:
    BASE_CMD = "cmocka_driver_simple"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    def test_driver_simple_01_integration(self):
        case = "drivertest_simple_assert"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=2)
        assert ret == 0

    def test_driver_simple_02_integration(self):
        case = "drivertest_simple_assert_string"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=2)
        assert ret == 0
