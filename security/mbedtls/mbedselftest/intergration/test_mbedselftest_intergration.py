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


@pytest.mark.dep_config("CONFIG_MBEDTLS_SELF_TEST", "CONFIG_MBEDTLS_APP_SELFTEST")
@pytest.mark.cmd_check("mbedselftest_main")
def test_mbedselftest_integration():

    cmd = f"mbedselftest"
    EXPECTED_LIST = ["Executed 30 test suites", "All tests PASS"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=70)
    assert ret == 0
