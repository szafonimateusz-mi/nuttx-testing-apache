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

import logging

import pytest


@pytest.mark.cmd_check("cmocka", "cmocka_driver_gpio")
@pytest.mark.dep_config(
    "CONFIG_TESTING_DRIVER_TEST", "CONFIG_ARCH_SIM", "CONFIG_DEV_GPIO"
)
class TestDriverGPIO:
    BASE_CMD = "cmocka_driver_gpio"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    def test_driver_gpio_integration01(self):
        case = "drivertest_gpio"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=5)
        assert ret == 0

    def test_driver_gpio_integration02(self):
        case = "drivertest_rw_gpio"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=5)
        assert ret == 0

    def test_driver_gpio_integration03(self):
        case = "drivertest_int_edge"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=5)
        assert ret == 0

    def test_driver_gpio_integration04(self):
        case = "drivertest_int_level"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=5)
        assert ret == 0
