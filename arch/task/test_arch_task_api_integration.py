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

pytestmark = pytest.mark.dep_config("CONFIG_SCHED_TEST")


@pytest.mark.cmd_check("vela_sched_interface_task_test01_main")
def test_vela_sched_interface_task_test01():

    cmd = "vela_sched_interface_task_test01"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test02_main")
def test_vela_sched_interface_task_test02():

    cmd = "vela_sched_interface_task_test02"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test03_main")
def test_vela_sched_interface_task_test03():

    cmd = "vela_sched_interface_task_test03"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test04_main")
def test_vela_sched_interface_task_test04():

    cmd = "vela_sched_interface_task_test04"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test05_main")
def test_vela_sched_interface_task_test05():

    cmd = "vela_sched_interface_task_test05"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test06_main")
def test_vela_sched_interface_task_test06():

    cmd = "vela_sched_interface_task_test06"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_task_test07_main")
def test_vela_sched_interface_task_test07():

    cmd = "vela_sched_interface_task_test07"
    EXPECTED_LIST = "TEST PASSED !"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0
