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

TEST_CASES = [
    pytest.param(
        "test_nuttx_fs_creat01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_create_operations",
    ),
    pytest.param(
        "test_nuttx_fs_dup01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_dup_operations",
    ),
    pytest.param(
        "test_nuttx_fs_fcntl01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_fcntl_controls",
    ),
    pytest.param(
        "test_nuttx_fs_fstat01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_status",
    ),
    pytest.param(
        "test_nuttx_fs_fstatfs01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_filesystem_status",
    ),
    pytest.param(
        "test_nuttx_fs_fsync01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_sync_operations01",
    ),
    pytest.param(
        "test_nuttx_fs_fsync02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_sync_operations02",
    ),
    pytest.param(
        "test_nuttx_fs_file_get01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_pointer_get",
    ),
    pytest.param(
        "test_nuttx_fs_mkdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_operations",
    ),
    pytest.param(
        "test_nuttx_fs_open01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_opening01",
    ),
    pytest.param(
        "test_nuttx_fs_open02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_opening02",
    ),
    pytest.param(
        "test_nuttx_fs_opendir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_opening01",
    ),
    pytest.param(
        "test_nuttx_fs_opendir02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_opening02",
    ),
    pytest.param(
        "test_nuttx_fs_pread01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_reading",
    ),
    pytest.param(
        "test_nuttx_fs_pwrite01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_writing",
    ),
    pytest.param(
        "test_nuttx_fs_readdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_reading",
    ),
    pytest.param(
        "test_nuttx_fs_readlink01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_symlink_reading",
    ),
    pytest.param(
        "test_nuttx_fs_rename01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_renaming1",
    ),
    pytest.param(
        "test_nuttx_fs_rename02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_renaming2",
    ),
    pytest.param(
        "test_nuttx_fs_rewinddir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_rewinding",
    ),
    pytest.param(
        "test_nuttx_fs_rmdir01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_removal01",
    ),
    pytest.param(
        "test_nuttx_fs_rmdir02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_removal02",
    ),
    pytest.param(
        "test_nuttx_fs_rmdir03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_directory_removal03",
    ),
    pytest.param(
        "test_nuttx_fs_seek01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_seeking01",
    ),
    pytest.param(
        "test_nuttx_fs_seek02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_seeking02",
    ),
    pytest.param(
        "test_nuttx_fs_statfs01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_filesystem_status",
    ),
    pytest.param(
        "test_nuttx_fs_symlink01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_symlink_creation",
    ),
    pytest.param(
        "test_nuttx_fs_truncate01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_truncation",
    ),
    pytest.param(
        "test_nuttx_fs_unlink01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_deletion",
    ),
    pytest.param(
        "test_nuttx_fs_write01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_writing01",
    ),
    pytest.param(
        "test_nuttx_fs_write02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_writing02",
    ),
    pytest.param(
        "test_nuttx_fs_write03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_writing03",
    ),
    pytest.param(
        "test_nuttx_fs_append01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_append",
    ),
    pytest.param(
        "test_nuttx_fs_sendfile01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_send01",
    ),
    pytest.param(
        "test_nuttx_fs_sendfile02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_file_send02",
    ),
    pytest.param(
        "test_nuttx_fs_stream01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_stream_operations01",
    ),
    pytest.param(
        "test_nuttx_fs_stream02",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_stream_operations02",
    ),
    pytest.param(
        "test_nuttx_fs_stream03",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_stream_operations03",
    ),
    pytest.param(
        "test_nuttx_fs_stream04",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_stream_operations04",
    ),
    pytest.param(
        "test_nuttx_fs_eventfd",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_eventfd_operations",
    ),
    pytest.param(
        "test_nuttx_fs_poll01",
        ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"],
        id="fs_poll_operations",
    ),
]


@pytest.mark.cmd_check("cmocka", "cmocka_fs_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_FS_TEST")
@pytest.mark.parametrize("case, expected_list", TEST_CASES)
def test_fs_integration(case, expected_list, switch_to_core) -> None:
    """Execute fs integration tests"""

    BASE_CMD = "cmocka_fs_test"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=200)
    assert ret == 0


@pytest.mark.skip(reason="Not Ready for Simulator")
@pytest.mark.cmd_check("cmocka", "cmocka_fs_test")
@pytest.mark.dep_config("CONFIG_TESTS_TESTSUITES", "CONFIG_CM_FS_TEST")
class TestFSTestIntegration:
    BASE_CMD = "cmocka_fs_test"
    expected_list = ["[  PASSED  ] 1 test(s).", "Cmocka Test Completed"]

    def test_fs_fcntl_02(self):
        case = "test_nuttx_fs_fcntl02"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.expected_list, timeout=15)
        assert ret == 0

    def test_fs_fcntl_03(self):
        case = "test_nuttx_fs_fcntl03"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.expected_list, timeout=15)
        assert ret == 0

    def test_fs_fstat_02(self):
        case = "test_nuttx_fs_fstat02"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.expected_list, timeout=15)
        assert ret == 0

    def test_fs_read_01(self):
        case = "test_nuttx_fs_read01"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.expected_list, timeout=15)
        assert ret == 0

    def test_fs_stat_01(self):
        case = "test_nuttx_fs_stat01"
        cmd = f"cmocka -s {self.BASE_CMD} -t {case}"

        ret = pytest.product.sendCommand(cmd, self.expected_list, timeout=15)
        assert ret == 0


@pytest.mark.dep_config("CONFIG_TESTING_FSTEST")
@pytest.mark.cmd_check("fstest_main")
def test_fs_test():
    fs = "tmp"
    core = "ap"
    fstest_dir = "{}/{}_fstest".format(fs, core)

    # rmdir fstest first
    pytest.product.sendCommand("rm -r %s" % fstest_dir, "")
    pytest.product.sendCommand("mkdir %s" % fstest_dir, "")

    ret = pytest.product.sendCommand(
        "fstest -n 1 -m %s" % fstest_dir, "Final memory usage", timeout=40
    )

    pytest.product.sendCommand("ls %s" % fstest_dir, "")
    pytest.product.sendCommand("rm -r %s" % fstest_dir, "", timeout=60)

    assert ret == 0
