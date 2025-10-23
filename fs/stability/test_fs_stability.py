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

pytestmark = pytest.mark.skip(reason="Not ready")


@pytest.mark.dep_config("CONFIG_FS_TEST_STRESS")
class TestFs:

    @pytest.mark.cmd_check("vela_fs_stress_multi_thread_file_operate_test_main")
    def test_stress_multi_thread_file_operate_test(self):
        fs = "tmp"
        ret = pytest.product.sendCommand(
            "vela_fs_stress_multi_thread_file_operate_test {}".format(fs),
            "TEST PASSED",
        )
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_stress_loop_create_delete_file_test_main")
    def test_stress_loop_create_delete_file_test(self):
        fs = "tmp"
        ret = pytest.product.sendCommand(
            "vela_fs_stress_loop_create_delete_file_test {}".format(fs),
            "TEST PASSED",
            timeout=50,
        )
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_random_read_and_write_test_main")
    def test_random_read_and_write_test(self):
        fs = "tmp"
        ret = pytest.product.sendCommand(
            "vela_fs_random_read_and_write_test writeCount={} readCount={} mountPath={}".format(
                5, 5, fs
            )
        )
        assert ret == 0

    @pytest.mark.cmd_check("test_stress_read_and_write_loops_test_main")
    def test_stress_read_and_write_loops_test(self):
        fs = "tmp"
        testnum = 10000
        ret = pytest.product.sendCommand(
            "vela_fs_stress_read_and_write_loops_test {} {}".format(fs, testnum),
            "TEST PASSED",
            timeout=10 * 60,
        )
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_multi_thread_read_write_test_main")
    def test_multi_thread_read_write_test(self):
        fs = "tmp"
        ret = pytest.product.sendCommand(
            "vela_fs_multi_thread_read_write_test -d {}".format(fs),
            "TEST PASS",
            timeout=50 * 60,
        )
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_file_pressure_test_main")
    def test_file_pressure_test(self):
        fs = "tmp"
        testnum = 1000
        ret = pytest.product.sendCommand(
            "vela_fs_file_pressure_test -d {} -c {}".format(fs, testnum),
            "TEST NO.{}".format(testnum),
            timeout=10 * testnum,
        )
        assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_FSTEST")
@pytest.mark.cmd_check("fstest_main")
def test_fstest(self):
    fs = "tmp"
    core = "ap"
    testnum = 1000
    fstest_dir = "{}/{}_fstest".format(fs, core)
    pytest.product.sendCommand("rm -r %s" % fstest_dir, "")
    pytest.product.sendCommand("mkdir %s" % fstest_dir, "")
    ret = pytest.product.sendCommand(
        "fstest -n {} -m {}".format(testnum, fstest_dir),
        "Final memory usage",
        timeout=60 * testnum,
    )
    pytest.product.sendCommand("ls %s" % fstest_dir, "")
    pytest.product.sendCommand("rm -r %s" % fstest_dir, "")

    assert ret == 0


@pytest.mark.dep_config("CONFIG_FS_TEST_STABILITY")
@pytest.mark.cmd_check("vela_fs_stability_test01_main")
def test_stability_test01(self):
    fs = "tmp"
    testtime = 1
    fstest_dir = "{}/stab_test_dir".format(fs)
    pytest.product.sendCommand("rm -r {}".format(fstest_dir), "")
    ret = pytest.product.sendCommand(
        "vela_fs_stability_test01 -d {} -t {}".format(fs, testtime),
        "TEST PASSED",
        timeout=70 * 60 * testtime,
    )
    assert ret == 0


@pytest.mark.dep_config("CONFIG_FS_TEST_STABILITY")
@pytest.mark.cmd_check("vela_fs_stability_test03_main")
def test_stability_test03(self):
    pytest.product.sendCommand(
        "vela_fs_stability_test03 mode=crash", "TEST PASS", timeout=120
    )
    ret = pytest.product.sendCommand("vela_fs_stability_test03 mode=crash", "TEST PASS")
    assert ret == 0
    pytest.product.sendCommand(
        "vela_fs_stability_test03 mode=reboot", "TEST PASS", timeout=120
    )
    ret = pytest.product.sendCommand(
        "vela_fs_stability_test03 mode=reboot", "TEST PASS"
    )
    assert ret == 0


@pytest.mark.dep_config("CONFIG_FS_TEST_STABILITY")
@pytest.mark.cmd_check("vela_fs_stability_test04_main")
def test_stability_test04(self):
    pytest.product.sendCommand("vela_fs_stability_test04", "TEST PASSED", timeout=180)
    ret = pytest.product.sendCommand(
        "vela_fs_stability_test04", "TEST PASSED", timeout=20
    )
    assert ret == 0
