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


@pytest.mark.cmd_check("cmocka", "cmocka_driver_oneshot")
@pytest.mark.dep_config("CONFIG_TESTING_DRIVER_TEST", "CONFIG_TESTING_ONESHOT_TEST")
def test_case_oneshot_integration():
    cmd = f"cmocka -s cmocka_driver_oneshot -t drivertest_oneshot"

    ret = pytest.product.sendCommand(
        cmd, ["[  PASSED  ]", "Cmocka Test Completed"], timeout=30
    )
    assert ret == 0
