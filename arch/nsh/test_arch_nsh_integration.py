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
import re
import time
from datetime import datetime, timedelta

import pytest

nuttx_directory = "nuttx_dir"


@pytest.mark.cmd_check("cmd_shutdown", "reboot")
@pytest.mark.skip("multi_board")
class TestShutdown:
    def test_shutdown(self):
        ret = pytest.product.sendCommand("shutdown --reboot", "NSH", timeout=60)
        assert ret == 0


@pytest.mark.cmd_check("cmd_cat")
@pytest.mark.dep_config("CONFIG_FS_TMPFS")
class TestCat:
    def test_cat001(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("\n", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile1_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile1_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("echo 123456hello > %s/testfile1_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile1_2" % fs, "123456hello")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile1_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile1_2" % fs, "")
        assert ret == 0

    def test_cat002(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile2", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("cat testfile2", "%s" % "failed")
        assert ret == 0

    def test_cat003(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile3_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile3_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("echo HELLOWORLD > %s/testfile3_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile3_2" % fs, "HELLOWORLD")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile3_1 > %s/testfile3_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile3_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile3_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile3_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile3_2" % fs, "")
        assert ret == 0

    def test_cat004(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo > %s/testfile4_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile4_1" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile4_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile4_2" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile4_1 > %s/testfile4_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile4_1" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile4_2" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile4_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile4_2" % fs, "")
        assert ret == 0

    def test_cat005(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfiel5_1", "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile5_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile5_2" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile5_1 > %s/testfile5_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile5_1" % fs, "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile5_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile5_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile5_2" % fs, "")
        assert ret == 0

    def test_cat006(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile6_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile6_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("echo  > %s/testfile6_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile6_2" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile6_1 > %s/testfile6_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile6_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile6_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile6_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile6_2" % fs, "")
        assert ret == 0

    def test_cat007(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile7_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile7_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile7_2", "failed")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile7_1 > %s/testfile7_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile7_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile7_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile7_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile7_2" % fs, "")
        assert ret == 0

    def test_cat008(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile8_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile8_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("echo HELLOWORLD > %s/testfile8_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile8_2" % fs, "HELLOWORLD")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile8_1  >> %s/testfile8_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile8_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile8_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile8_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile8_2" % fs, "")
        assert ret == 0

    def test_cat009(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo   > %s/testfile9_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile9_1" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile9_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile9_2" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile9_1 >> %s/testfile9_2" % (fs, fs)
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile9_1" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile9_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile9_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile9_2" % fs, "")
        assert ret == 0

    def test_cat010(self, core, switch_to_core):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile10_1", "failed", timeout=10)
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile10_2" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile10_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile10_1 >> %s/testfile10_2" % (fs, fs), "failed"
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile10_1" % fs, "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile10_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile10_2" % fs, " ")
        assert ret == 0

    @pytest.mark.dep_config("CONFIG_ARCH_HAVE_CPUINFO")
    def test_cat011(self, core, switch_to_core):
        ret = pytest.product.sendCommand("cat /proc/cpuinfo", "cpu MHz")
        assert ret == 0


@pytest.mark.cmd_check("cmd_cd")
class TestCd:
    def test_cd001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile11", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile11", "testfile11")
        assert ret == 0
        ret = pytest.product.sendCommand("cd ", "")
        assert ret == 0
        ret = pytest.product.sendCommand("cd %s/testfile11" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "%s/testfile11" % fs)
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir %s/testfile11" % fs, "")
        assert ret == 0

    def test_cd002(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"mkdir {nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir apps", "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"cd {fs}/{nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand("cd %s/apps" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "%s/apps" % fs)
        assert ret == 0
        ret = pytest.product.sendCommand("cd -", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir %s/apps" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"rmdir {fs}/{nuttx_directory}", "")
        assert ret == 0

    def test_cd003(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"mkdir {nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"cd {fs}/{nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand("cd ~", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "/")
        assert ret == 0
        ret = pytest.product.sendCommand(f"rmdir {fs}/{nuttx_directory}", "")
        assert ret == 0

    def test_cd004(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"mkdir {nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"cd {fs}/{nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand("cd", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "/")
        assert ret == 0
        ret = pytest.product.sendCommand(f"rmdir {fs}/{nuttx_directory}", "")
        assert ret == 0

    def test_cd005(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"mkdir {nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"cd {fs}/{nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand("cd ..", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand(f"rmdir {fs}/{nuttx_directory}", "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_echo")
class TestEcho:
    def test_echo001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"mkdir {nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand(f"cd {fs}/{nuttx_directory}", "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", f"{fs}/{nuttx_directory}")
        assert ret == 0
        ret = pytest.product.sendCommand('echo "helloworld"', "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld", "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand(f"rmdir {fs}/{nuttx_directory}", "")
        assert ret == 0

    def test_echo002(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile17_1", "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > testfile17_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat testfile17_1", "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile17_1" % fs, "")
        assert ret == 0

    def test_echo003(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "%s" % fs)
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld >testfile18_1", "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat testfile18_1", "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("echo HELLOWORLD > testfile18_2")
        assert ret == 0
        ret = pytest.product.sendCommand("cat testfile18_2", "HELLOWORLD")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile18_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile18_2" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_help")
class TestHelp:
    def test_help01(self):
        ret = pytest.product.sendCommand("help", "help usage")
        assert ret == 0

    def test_help02(self):
        ret = pytest.product.sendCommand("?", "help usage")
        assert ret == 0

    def test_help_v(self):
        ret = pytest.product.sendCommand("help -v", "NSH command")
        assert ret == 0

    def test_help_cat(self):
        ret = pytest.product.sendCommand("help cat", "cat usage")
        assert ret == 0


@pytest.mark.cmd_check("cmd_ls")
class TestLs:
    def test_ls_l(self):
        ret = pytest.product.sendCommand("ls -l", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "0")
        assert ret == 0

    @pytest.mark.skip("No Ready")
    def test_ls_s(self):
        ret = pytest.product.sendCommand("mkdir test_folder", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -s", "0")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "0")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir test_folder", "")
        assert ret == 0

    def test_ls_R(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("ls -R %s" % fs, fs)
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "0", timeout=10)
        assert ret == 0


@pytest.mark.cmd_check("cmd_rm")
class TestRm:
    def test_rm001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile25_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile25_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile25_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile25_1", "failed")
        assert ret == 0

    def test_rm002(self):
        fs = "tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile26_1", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile26_1" % fs, "failed")
        assert ret == 0


@pytest.mark.cmd_check("cmd_mkdir")
class TestMkdir:
    def test_mkdir001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand(
            "mkdir -p testdir_01/testdir_02/testdir_03", ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand(
            "ls -l testdir_01/testdir_02/testdir_03", "testdir_01/testdir_02/testdir_03"
        )
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testdir_01/testdir_02/testdir_03", "")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testdir_01/testdir_02", "")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testdir_01", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testdir_01", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testdir_01", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testdir_01" % fs, "failed")
        assert ret == 0


@pytest.mark.cmd_check("cmd_rmdir")
class TestRmdir:
    def test_rmdir001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile27_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile27_1", "testfile27_1")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testfile27_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile27_1", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir testfile27_1", "%s" % "failed")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile27_1" % fs, "failed")
        assert ret == 0

    def test_rmdir002(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs, timeout=10)
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile53_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile53_1", "testfile53_1")
        assert ret == 0
        ret = pytest.product.sendCommand("cd testfile53_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile53_2", "")
        assert ret == 0
        ret = pytest.product.sendCommand("cd testfile53_2", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo helloworld > testfile53_3", "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm -r %s/testfile53_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "0")
        assert ret == 0


@pytest.mark.cmd_check("cmd_cp")
class TestCp:
    def test_cp001(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile28_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile28_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("echo HELLOWORLD > %s/testfile28_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile28_2" % fs, "HELLOWORLD")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cp %s/testfile28_1 %s/testfile28_2" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat  %s/testfile28_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat  %s/testfile28_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile28_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile28_2" % fs, "")
        assert ret == 0

    def test_cp002(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo  > %s/testfile29_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile29_1" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("echo HELLOWORLD > %s/testfile29_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile29_2" % fs, "HELLOWORLD", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cp  %s/testfile29_1  %s/testfile29_2" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat  %s/testfile29_2" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile29_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile29_2" % fs, "")
        assert ret == 0

    def test_cp003(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo helloworld > %s/testfile30_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cat %s/testfile30_1" % fs, "helloworld", timeout=10
        )
        assert ret == 0
        ret = pytest.product.sendCommand("echo  > %s/testfile30_2" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile30_2" % fs, " ")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "cp %s/testfile30_1 %s/testfile30_2" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile30_1" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/testfile30_2" % fs, "helloworld")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile30_1" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/testfile30_2" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_ps")
class TestPs:
    def test_ps(self):
        ret = pytest.product.sendCommand("ps", "Waiting")
        assert ret == 0


@pytest.mark.cmd_check("cmd_time")
class TestTime:

    time_pattern = r"5\.\d{4} sec"

    def test_sleep(self):
        ret = pytest.product.sendCommand(
            'time "sleep 5"', TestTime.time_pattern, regexp=True
        )
        assert ret == 0

    def test_usleep(self):
        ret = pytest.product.sendCommand(
            'time "usleep 5000000"', TestTime.time_pattern, regexp=True
        )
        assert ret == 0


@pytest.mark.cmd_check("cmd_set")
class TestSet:
    def test_set(self):
        ret = pytest.product.sendCommand("set name TOM", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $name", "TOM")
        assert ret == 0

    def test_unset(self):
        ret = pytest.product.sendCommand("set name TOM", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $name", "TOM")
        assert ret == 0
        ret = pytest.product.sendCommand("unset name", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $name", " ")
        assert ret == 0


@pytest.mark.cmd_check("cmd_if")
class TestIf:
    def test_false_true(self):
        ret = pytest.product.sendCommand(
            'if false; then echo "false"; else echo "true";fi', "true"
        )
        assert ret == 0


@pytest.mark.cmd_check("cmd_test")
class TestTest:
    def test_test(self):
        ret = pytest.product.sendCommand("test 5 -gt 2", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "0")
        assert ret == 0
        ret = pytest.product.sendCommand("test 1 -gt 2", "")
        assert ret == 0
        ret = pytest.product.sendCommand("echo $?", "1")
        assert ret == 0


@pytest.mark.cmd_check("cmd_dirname")
class TestDirname:
    def test_dirname(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile39_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile39_1", "testfile39_1")
        assert ret == 0
        ret = pytest.product.sendCommand("dirname %s/testfile39_1" % fs, fs)
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir %s/testfile39_1" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_basename")
class TestBasename:
    def test_basename(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", "%s" % fs)
        assert ret == 0
        ret = pytest.product.sendCommand("mkdir testfile40_1", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l testfile40_1", "testfile40_1")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "basename %s/testfile40_1" % fs, "testfile40_1"
        )
        assert ret == 0
        ret = pytest.product.sendCommand("rmdir %s/testfile40_1" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_df")
class TestDf:
    def test_df(self):
        ret = pytest.product.sendCommand("df", "Used")
        assert ret == 0

    def test_df_h(self):
        ret = pytest.product.sendCommand("df -h", "Used")
        assert ret == 0


@pytest.mark.cmd_check("cmd_uname")
class TestUname:
    def test_uname(self):
        ret = pytest.product.sendCommand("uname", "NuttX")
        assert ret == 0

    def test_uname_a(self):
        ret = pytest.product.sendCommand("uname -a", "NuttX")
        assert ret == 0

    def test_uname_s(self):
        ret = pytest.product.sendCommand("uname -s", "NuttX")
        assert ret == 0

    def test_uname_r(self):
        ret = pytest.product.sendCommand("uname -r")
        assert ret == 0

    @pytest.mark.skip("No Ready")
    def test_uname_v(self):
        now_date_obj = datetime.now()
        pre_date_obj = now_date_obj - timedelta(days=1)
        now_day = now_date_obj.strftime("%b %d").replace(" 0", "  ")
        pre_day = pre_date_obj.strftime("%b %d").replace(" 0", "  ")
        ret = pytest.product.sendCommand(
            "uname  -v", [now_day, pre_day], match_all=False
        )
        assert ret >= 0

    @pytest.mark.skip("nosense")
    def test_uname_m(self):
        ret = pytest.product.sendCommand(
            "uname -m", ["sim", "arm", "arm64", "risc-v", "x86_64"], match_all=False
        )
        assert ret == 0

    @pytest.mark.skip("nosense")
    def test_uname_i(self):
        ret = pytest.product.sendCommand("uname -i", ["ap", "miwear"], match_all=False)
        assert ret == 0


@pytest.mark.cmd_check("cmd_dd")
class TestDd:

    def test_dd01(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo hello > %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("dd if=%s/test01 of=%s/test02" % (fs, fs), "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/test02" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test02" % fs, "")
        assert ret == 0

    def test_dd02(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo hello > %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "dd if=%s/test01 of=%s/test02 bs=50" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/test02" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l %s" % fs, "6 test02")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test02" % fs, "")
        assert ret == 0

    def test_dd03(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo hello > %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "dd if=%s/test01 of=%s/test02 bs=2 count=2" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/test02" % fs, "hell", timeout=10)
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l %s" % fs, "4 test02")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test02" % fs, "")
        assert ret == 0

    def test_dd04(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo hello > %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand(
            "dd if=%s/test01 of=%s/test02 bs=1" % (fs, fs), ""
        )
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/test02" % fs, "hello", timeout=10)
        assert ret == 0
        ret = pytest.product.sendCommand("ls -l %s" % fs, "6 test02")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test02" % fs, "")
        assert ret == 0

    @pytest.mark.skip(reason="unsupported")
    @pytest.mark.cmd_check("cmd_time", "cmd_dd", "cmd_rm")
    def test_dd05(self):
        fs = "/tmp"
        pattern = rb"(?P<cost>\d+\.\d{4}) sec"
        cmd = 'time "dd if=/dev/zero of={}/test_dd_10M.img bs=512 count=20000"'.format(
            fs
        )
        ret, match, _ = pytest.product.sendCommandReadUntilPattern(
            cmd, pattern, timeout=60
        )
        assert ret == 0
        tm = match.group("cost").decode("utf-8")
        expect_time = 40
        assert float(tm) <= expect_time
        ret = pytest.product.sendCommand("rm %s/test_dd_10M.img" % fs, timeout=5)
        assert ret == 0


@pytest.mark.cmd_check("cmd_env")
class TestEnv:
    def test_env(self):
        ret = pytest.product.sendCommand("env", "PWD")
        assert ret == 0


@pytest.mark.cmd_check("cmd_mv")
class TestMv:
    def test_mv(self):
        fs = "/tmp"
        pytest.product.sendCommand("echo hello > %s/test01" % fs)
        pytest.product.sendCommand("mv %s/test01 %s/test02" % (fs, fs))
        ret = pytest.product.sendCommand("cat %s/test02" % fs, "hello", timeout=10)
        assert ret == 0
        ret1 = pytest.product.sendCommand("cat %s/test01" % fs, "failed")
        assert ret1 == 0
        pytest.product.sendCommand("rm %s/test01" % fs)
        pytest.product.sendCommand("rm %s/test02" % fs)


@pytest.mark.cmd_check("cmd_pwd")
class TestPwd:
    def test_pwd(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("pwd", "/")
        assert ret == 0
        ret = pytest.product.sendCommand("cd %s" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("pwd", fs)
        assert ret == 0
        ret = pytest.product.sendCommand("cd ~", "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_hexdump")
class TestHexdump:
    def test_hexdump(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand("echo hello > %s/test01" % fs, "")
        assert ret == 0
        ret = pytest.product.sendCommand("cat %s/test01" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("hexdump %s/test01" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_mkrd")
class TestMkrd:
    def test_mkrd(self):
        ret = pytest.product.sendCommand("mkrd -m 10 -s 1 1024", "")
        assert ret == 0
        ret = pytest.product.sendCommand("ls /dev", "ram10")
        assert ret == 0
        ret = pytest.product.sendCommand("rm /dev/ram10", "")
        assert ret == 0


@pytest.mark.skip("unsupported")
class TestMw:
    def test_mw(self):
        ret = pytest.product.sendCommand("mw 20000000=2 1", "0x00000002")
        assert ret == 0


@pytest.mark.cmd_check("cmd_sh")
class TestSh:
    def test_sh(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand(
            'echo "while true; do; echo hello; break;echo world; done" > %s/test01.sh'
            % fs
        )
        assert ret == 0
        ret = pytest.product.sendCommand("sh %s/test01.sh" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("\n", ">")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01.sh" % fs, "")
        assert ret == 0

    def test_exit(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand(
            'echo "while true; do; echo hello; exit;echo world; done" > %s/test01.sh'
            % fs
        )
        assert ret == 0
        ret = pytest.product.sendCommand("sh %s/test01.sh" % fs, "hello")
        assert ret == 0
        ret = pytest.product.sendCommand("\n", ">")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01.sh" % fs, "")
        assert ret == 0


@pytest.mark.cmd_check("cmd_gt")
class TestGt:
    def test_gt(self):
        fs = "/tmp"
        ret = pytest.product.sendCommand(
            'echo "if [ 5 -gt 2 ];then echo true ; else echo false ; fi" > %s/test01.sh'
            % fs
        )
        assert ret == 0
        ret = pytest.product.sendCommand("sh %s/test01.sh" % fs, "true")
        assert ret == 0
        ret = pytest.product.sendCommand("rm %s/test01.sh" % fs, "")
        assert ret == 0


@pytest.mark.skip(reason="unsupported")
class TestExec:
    def getaddr(self, logfile):
        with open(logfile, "rb") as f:
            lines = [l.decode("utf8", "ignore") for l in f.readlines()]
        for line in lines:
            if "addr is" in line:
                obj = re.findall("0x[0-9a-fA-F]+", line)
                return obj[0]

    def test_exec(self, p):
        ret = pytest.product.sendCommand("exectest", "addr")
        assert ret == 0
        ex = self.getaddr(p.log)
        ret = pytest.product.sendCommand("exec %s" % ex, "exec_test")
        assert ret == 0


@pytest.mark.cmd_check("cmd_date", "cmd_reboot", "cmd_uname")
class TestDate:
    def test_date(self):
        dt = datetime.now().strftime("%b %d %H:%M:%S %Y")
        pytest.product.sendCommand(f'date -s "{dt}"', timeout=5)
        time.sleep(3)
        ret0 = pytest.product.sendCommand(
            "uname -m", "arm", match_all=False, timeout=10
        )
        if ret0 == 0:
            # pytest.product.sendCommand("reboot", "NSH", timeout=pytest.product.uptime)
            pytest.product.reboot()
            time.sleep(pytest.product.uptime)
            dt = datetime.now().strftime("%b %d")
            ret = pytest.product.sendCommand("date", dt, timeout=5)
            assert ret == 0
