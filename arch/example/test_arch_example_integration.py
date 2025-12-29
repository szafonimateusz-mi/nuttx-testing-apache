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

import os
import random
import re
import string
import time

import pytest


@pytest.mark.dep_config("CONFIG_EXAMPLES_HELLO")
@pytest.mark.cmd_check("hello_main")
def test_hello_integration(core, switch_to_core):

    cmd = "hello"
    EXPECTED_LIST = "Hello, World!!"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=5)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_EXAMPLES_HELLOXX")
@pytest.mark.cmd_check("helloxx_main")
def test_helloxx_integration(core, switch_to_core):

    cmd = "helloxx"
    EXPECTED_LIST = "Hello, World!!"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=5)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_EXAMPLES_PIPE", "CONFIG_PIPES")
@pytest.mark.cmd_check("pipe_main")
def test_pipe_integration(core, switch_to_core):
    cmd = "pipe"
    EXPECTED_LIST = "PIPE redirection test PASSED"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=70)
    assert ret == 0
    ret = pytest.product.sendCommand("rm /var/testfifo-1", "")
    assert ret == 0
    ret = pytest.product.sendCommand("rm /var/testfifo-2", "")
    assert ret == 0


@pytest.mark.dep_config("CONFIG_EXAMPLES_POPEN", "CONFIG_SYSTEM_POPEN")
@pytest.mark.cmd_check("popen_main")
def test_popen_integration(core, switch_to_core):
    cmd = "popen"
    EXPECTED_LIST = "Calling pclose()"

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=30)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_EXAMPLES_ROMFS")
@pytest.mark.cmd_check("romfs_main")
def test_romfs(core, switch_to_core):
    if pytest.product.sendCommand("mkdir /usr", "failed"):
        pytest.skip("/usr exists")
    ret = pytest.product.sendCommand("romfs", "PASSED")
    assert ret == 0


@pytest.mark.skip("fail case skip")
@pytest.mark.dep_config("CONFIG_TESTING_CXXTEST")
@pytest.mark.cmd_check("cxxtest_main")
def test_cxxtest():
    ret = pytest.product.sendCommand("cxxtest", "Hello World", timeout=1)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_SCANFTEST")
@pytest.mark.cmd_check("scanftest_main")
def test_scanftest():
    ret = pytest.product.sendCommand("scanftest", "Test #25", timeout=3)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_GETPRIME")
@pytest.mark.cmd_check("getprime_main")
def test_getprime():
    ret = pytest.product.sendCommand("getprime", "getprime took", timeout=15)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_FATUTF8")
@pytest.mark.cmd_check("fatutf8_main")
def test_fatutf8():
    fs = "/tmp"
    ret = pytest.product.sendCommand("fatutf8 %s" % fs, "removed", timeout=3)
    assert ret == 0


@pytest.mark.dep_config("CONFIG_EXAMPLES_USRSOCKTEST")
@pytest.mark.cmd_check("usrsocktest_main")
def test_usrsocktest():
    ret = pytest.product.sendCommand("usrsocktest", "FAILED:0", timeout=60)
    assert ret == 0


def getLog(filename, str1, str2):
    l1 = []
    time.sleep(10)
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        buff = f.read()
        f.close()
    pat = re.compile(str1 + "(.*?)" + str2, re.S)
    result = pat.findall(buff)

    if "gtest" in str1:
        return result[0].strip("\n")
    else:
        # add line to l1
        for i in result[0].strip("\n").split("\n"):
            l1.append(i)
        return l1


def get_umem_free():
    """Get umem free size"""
    start_token = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(random.randint(5, 20))
    )
    free_start = f"echo {start_token}"

    end_token = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(random.randint(5, 20))
    )
    free_end = f"echo {end_token}"

    pytest.product.sendCommand("setlogmask r")
    pytest.product.sendCommand(free_start)
    pytest.product.sendCommand("free")
    pytest.product.sendCommand(free_end)
    pytest.product.sendCommand("setlogmask i")

    file_path = os.path.join(pytest.result_dir, "test_psram_test.console.txt")
    data = getLog(file_path, start_token, end_token)
    try:
        umem_free_value = next(line.split()[3] for line in data if "Umem:" in line)
    except StopIteration:
        umem_free_value = next(line.split()[2] for line in data if "Umem" in line)
    return int(umem_free_value)


@pytest.mark.skip(reason="Not ready")
@pytest.mark.dep_config("CONFIG_TESTING_FSTEST", "CONFIG_SYSTEM_SETLOGMASK")
@pytest.mark.cmd_check("fstest_main", "setlogmask_main")
def test_psram_test(load_value_from_config):
    if pytest.product.sendCommand("ls /", "tmp/") == 0:
        param_o = load_value_from_config("CONFIG_TESTING_FSTEST_MAXOPEN")
        if param_o == "":
            param_o = 512
        print("param_o:", param_o)
        free_umem_value = get_umem_free()
        param_s = free_umem_value // int(param_o) // 2
        ret = pytest.product.sendCommand(
            f"fstest -n 10 -s {param_s} -o {int(param_o)} -m /tmp",
            "Final memory usage",
            timeout=720,
        )
        assert ret == 0
