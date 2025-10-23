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


@pytest.mark.cmd_check("vela_sched_interface_pthread_test01_main")
def test_vela_sched_interface_pthread_test01_ntegration():

    cmd = "vela_sched_interface_pthread_test01"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_pthread_test02_main")
def test_vela_sched_interface_pthread_test02_ntegration():

    cmd = "vela_sched_interface_pthread_test02"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_pthread_test03_main")
def test_vela_sched_interface_pthread_test03_ntegration():

    cmd = "vela_sched_interface_pthread_test03"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_pthread_test04_main")
def test_vela_sched_interface_pthread_test04_ntegration():

    cmd = "vela_sched_interface_pthread_test04"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_pthread_test05_main")
def test_vela_sched_interface_pthread_test05_ntegration():

    cmd = "vela_sched_interface_pthread_test05"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_interface_pthread_test06_main")
def test_vela_sched_interface_pthread_test06_ntegration():

    cmd = "vela_sched_interface_pthread_test06"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("vela_sched_pthreads_pth01_main")
def test_vela_sched_pthreads_pth01_integration():

    cmd = "vela_sched_pthreads_pth01"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.skip("No Ready")
@pytest.mark.cmd_check("vela_sched_pthreads_pth02_main")
def test_vela_sched_pthreads_pth02_integration():

    cmd = "vela_sched_pthreads_pth02"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=20)
    assert ret == 0


@pytest.mark.skip("No Ready")
@pytest.mark.cmd_check("vela_sched_pthreads_pth03_main")
def test_vela_sched_pthreads_pth03_integration():
    cmd = "vela_sched_pthreads_pth03"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=40)
    assert ret == 0


@pytest.mark.skip("No Ready")
@pytest.mark.cmd_check("vela_sched_pthreads_pth04_main")
def test_vela_sched_pthreads_pth04_integration():
    cmd = "vela_sched_pthreads_pth04"
    EXPECTED_LIST = ["TEST PASSED"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0
