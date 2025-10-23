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


@pytest.mark.run(order=1)
@pytest.mark.dep_config("CONFIG_SYSTEM_SETLOGMASK", "CONFIG_TESTING_OSTEST")
@pytest.mark.cmd_check("ostest_main")
def test_os(core, switch_to_core):
    ret = pytest.product.sendCommand("setlogmask e", timeout=10)
    assert ret == 0 or ret == -2

    ret = pytest.product.sendCommand(
        "ostest",
        ["Exiting with status", "ostest_main: Exit"],
        match_all=False,
        timeout=800,
    )
    assert ret == 0

    ret = pytest.product.sendCommand("setlogmask i", timeout=10)
    assert ret == 0 or ret == -2, f"Command sent, but expected pattern not found."
