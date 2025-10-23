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


@pytest.mark.dep_config(
    "CONFIG_RPMSG", "CONFIG_RPMSG_PROCFS", "CONFIG_SYSTEM_CUTERM", "CONFIG_RPMSG_PING"
)
@pytest.mark.cmd_check("cmd_rpmsg", "cu_main")
def test_rpmsg_ping():
    # get core list
    core_list = pytest.product.core
    expected_list = [*(f"{core}>" for core in core_list)]
    core_list = [core.upper() for core in core_list]

    # check if get the core list
    if len(core_list) <= 1:
        pytest.skip(f"Fail to get core list: {core_list}")

    # test ping command
    for core in core_list[1:]:
        ret = pytest.product.sendCommand(
            "rpmsg ping all 1 1 1 1", ["ping times: 1"], timeout=15, match_all=False
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            f"cu -l /dev/tty{core}\n\n", expected_list, timeout=10, match_all=False
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            "rpmsg ping all 1 1 1 1", ["ping times: 1"], timeout=15, match_all=False
        )
        assert ret == 0
        pytest.product.sendCtrlCmd("c")
        time.sleep(1)
