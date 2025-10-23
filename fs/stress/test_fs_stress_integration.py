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


@pytest.mark.skip("Not Ready for multiple core")
@pytest.mark.dep_config("CONFIG_TESTING_FSTEST")
@pytest.mark.cmd_check("fstest_main")
def test_fs_fstest():
    pytest.sendCommand("mkdir /data/fstest")
    ret = pytest.product.sendCommand(
        "fstest -n 100 -m /data", "Final memory usage", timeout=3600
    )
    pytest.sendCommand("ls -l /data/fstest")
    pytest.sendCommand("rm -rf /data/fstest")
    assert ret == 0


@pytest.mark.dep_config("CONFIG_FS_TEST_STABILITY", "CONFIG_TESTS_TESTCASES")
class TestFsStressIntegration:
    BASE_CMD = "vela_fs_"
    TEST_DIR = "/data"
    EXPECTED_LIST = ["TEST PASSED"]

    @pytest.mark.cmd_check("vela_fs_stress_write_speed_main")
    def test_fs_stress_write_speed(self):
        case = "stress_write_speed"
        count = 500
        cmd = f"{self.BASE_CMD}{case} -d {self.TEST_DIR} -c {count}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=200)
        assert ret == 0

    @pytest.mark.skip(reason="Not Ready for Goldfish")
    @pytest.mark.cmd_check("vela_fs_stress_loop_create_delete_file_test_main")
    def test_fs_stress_loop_create_delete_file_test(self):
        case = "stress_loop_create_delete_file_test"
        cmd = f"{self.BASE_CMD}{case} {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=20)
        assert ret == 0

    @pytest.mark.skip(reason="Not Ready for Goldfish")
    @pytest.mark.cmd_check("vela_fs_stress_maximum_file_name_test")
    def test_vela_fs_stress_maximum_file_name_test(self):
        case = "stress_maximum_file_name_test"
        cmd = f"{self.BASE_CMD}{case} {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=20)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_stress_maximum_number_of_open_file_test_main")
    def test_vela_fs_stress_maximum_number_of_open_file_test(self):
        case = "stress_maximum_number_of_open_file_test"
        cmd = f"{self.BASE_CMD}{case} {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=200)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_stress_read_and_write_loops_test_main")
    def test_vela_fs_stress_read_and_write_loops_test(self):
        case = "stress_read_and_write_loops_test"
        cmd = f"{self.BASE_CMD}{case} {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=20)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_random_read_and_write_test_main")
    def test_vela_fs_random_read_and_write_test(self):
        case = "random_read_and_write_test"
        cmd = f"{self.BASE_CMD}{case} mountPath={self.TEST_DIR} writeCount=100 readCount=100"

        ret = pytest.product.sendCommand(
            cmd, "The test is complete, the data list is as follows", timeout=200
        )
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_multi_thread_read_test_main")
    def test_vela_fs_multi_thread_read_test(self):
        case = "multi_thread_read_test"
        cmd = f"{self.BASE_CMD}{case} testPath={self.TEST_DIR} dataLen=100"

        ret = pytest.product.sendCommand(cmd, "TEST PASS", timeout=20)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_multi_thread_write_test_main")
    def test_vela_fs_multi_thread_write_test(self):
        case = "multi_thread_write_test"
        cmd = f"{self.BASE_CMD}{case} -d {self.TEST_DIR} -l 100"

        ret = pytest.product.sendCommand(cmd, "TEST PASS", timeout=20)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_multi_thread_read_write_test_main")
    def test_vela_fs_multi_thread_read_write_test(self):
        case = "multi_thread_read_write_test"
        cmd = f"{self.BASE_CMD}{case} -d {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, "TEST PASS", timeout=1000)
        assert ret == 0

    @pytest.mark.cmd_check("vela_fs_file_pressure_test_main")
    def test_vela_fs_file_pressure_test(self):
        case = "file_pressure_test"
        cmd = f"{self.BASE_CMD}{case} -d {self.TEST_DIR} -c 3"

        ret = pytest.product.sendCommand(cmd, self.EXPECTED_LIST, timeout=200)
        assert ret == 0

    @pytest.mark.cmd_check("performance_test_main")
    def test_performance_test(self):
        case = "performance_test"
        cmd = f"{case} -d {self.TEST_DIR}"

        ret = pytest.product.sendCommand(cmd, "performance_test finish", timeout=20)
        assert ret == 0

    @pytest.mark.skip(reason="Not ready")
    @pytest.mark.cmd_check("vela_fs_stress_write_full_file_main")
    def test_stress_write_full_file(self):
        ret = pytest.product.sendCommand(
            "vela_fs_stress_write_full_file /tmp", self.EXPECTED_LIST, timeout=120 * 60
        )
        assert ret == 0
