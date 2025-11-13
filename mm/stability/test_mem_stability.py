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

pytestmark = pytest.mark.skip(reason="Not ready")


class Test_Sta_Mm:

    @pytest.mark.dep_config("CONFIG_UTILS_MEMTESTER")
    @pytest.mark.cmd_check("memtester_main")
    @pytest.mark.repeat(100)
    def test_sta_memtester(self):
        pytest.product.sendCtrlCmd("c")
        ret = pytest.product.sendCommand("memtester 5M 1", "Done", timeout=400)
        assert ret == 0

    def get_largest_free_memblock(self):
        memdump_Overhead = False
        pytest.product.sendCommand("setlogmask i")
        memdump_free_info = pytest.product.sendCommandRead("memdump free", timeout=10)
        memdump_free_info = memdump_free_info.split("\n")
        for i in memdump_free_info:
            if "Overhead" in i:
                memdump_Overhead = True
            if " Total Blks" in i:
                index = memdump_free_info.index(i)
        if memdump_Overhead:
            size = memdump_free_info[index - 1].split()[-3]
            addr = memdump_free_info[index - 1].split()[-1]
        else:
            (size, addr) = memdump_free_info[index - 1].split()[-2:]
        test_size = int(size) // 8 * 2
        test_addr = hex(int(addr, 16) + int(hex(test_size), 16))
        pytest.product.sendCommand("setlogmask r")
        print(test_size)
        print(test_addr)
        return (test_size, test_addr)

    @pytest.mark.dep_config("CONFIG_TESTING_RAMTEST")
    @pytest.mark.cmd_check("ramtest_main")
    @pytest.mark.repeat(100)
    def test_sta_ramtest(self):
        pytest.product.sendCtrlCmd("c")
        parameters = ["w", "h", "b"]
        for para in parameters:
            # get memdump free info
            (size, addr) = self.get_largest_free_memblock()
            # print(size, addr)
            ret1 = pytest.product.sendCommand(
                "ramtest -%s -s %s" % (para, size), "Address-in-address", timeout=60
            )
            assert ret1 == 0

    @pytest.mark.dep_config(
        "CONFIG_KVDB",
        "CONFIG_TESTING_HEAP",
        "CONFIG_NSH_DISABLE_ECHO",
        "CONFIG_DISABLE_ENVIRON",
    )
    @pytest.mark.cmd_check("setprop_main", "heap_main", "cmd_echo", "reboot")
    @pytest.mark.repeat(50)
    def test_sta_ramtest_mm(self):

        for i in range(1, 131):
            pytest.product.sendCtrlCmd("c")
            pytest.product.sendCommand("setprop persist.boot_fail_count 0")
            echo_str = f"echo test_sta_ramtest_mm_{i}"
            pytest.product.sendCommand(echo_str)

            # self.common_method(p)

            pytest.product.sendCtrlCmd("c")
            ret = pytest.product.sendCommand("heap", "TEST COMPLETE", timeout=120)
            assert ret == 0
        # pytest.product.sendCommand("reboot", timeout=20)
        pytest.product.reboot()

    @pytest.mark.dep_config(
        "CONFIG_KVDB",
        "CONFIG_SYSTEM_SETLOGMASK",
        "CONFIG_TESTING_MEMORY_STRESS",
        "CONFIG_BOARDCTL_RESET",
    )
    @pytest.mark.cmd_check("setprop_main", "setlogmask", "memstress", "reboot")
    def test_sta_memstress(self):
        pytest.product.sendCtrlCmd("c")
        pytest.product.sendCommand("setprop persist.boot_fail_count 0")

        pytest.product.sendCommand("setlogmask i")
        ret = pytest.product.sendCommand(
            "memstress -m 99999 -n 100 -t 5 &", "MemoryStress", timeout=100
        )
        time.sleep(1800)
        # pytest.product.sendCommand("reboot", timeout=20)
        pytest.product.reboot()
        assert ret == 0

    @pytest.mark.dep_config(
        "CONFIG_KVDB",
        "CONFIG_BOARDCTL_RESET",
        "CONFIG_TESTING_OPUS_RAMTEST",
        "CONFIG_NSH_DISABLE_ECHO",
        "CONFIG_DISABLE_ENVIRON",
    )
    @pytest.mark.cmd_check("setprop_main", "cmd_echo", "opus_ramtest", "reboot")
    def test_sta_opus(self):
        pytest.product.sendCtrlCmd("c")
        pytest.product.sendCommand("setprop persist.boot_fail_count 0")
        pytest.product.sendCommand("echo V > /dev/watchdog0")
        ret = pytest.product.sendCommand(
            "opus_ramtest -s 40960 &", "libopus", timeout=20
        )
        time.sleep(1800)
        # pytest.product.sendCommand("reboot", timeout=20)
        pytest.product.reboot()
        assert ret == 0
