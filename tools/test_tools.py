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

import logging
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest
from elftools.elf.elffile import ELFFile


def get_compile_paths(elf_file) -> str:
    with open(elf_file, "rb") as f:
        elf = ELFFile(f)
        if not elf.has_dwarf_info():
            return None

        dwarf_info = elf.get_dwarf_info()
        for CU in dwarf_info.iter_CUs():
            top_DIE = CU.get_top_DIE()
            if top_DIE and "DW_AT_comp_dir" in top_DIE.attributes:
                path = top_DIE.attributes["DW_AT_comp_dir"].value.decode()
                if "out" in path:
                    return path.split("cmake_out")[0]

    return None


def run_command_in_subprocess(command):
    return subprocess.Popen(
        command,
        shell=True,
        text=True,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    )


@pytest.mark.dep_config("CONFIG_SYSTEM_GCOV", "CONFIG_FS_TMPFS")
@pytest.mark.cmd_check("gcov_main")
@pytest.mark.run(order=-2)
def test_gcov():
    gcov_conf = pytest.task.get("gcov", {})
    gcov_enable = gcov_conf.get("enable", False)
    gcov_path = gcov_conf.get("gcov_path", "")
    code_path = gcov_conf.get("code_path", "")
    result_path = gcov_conf.get("result_path", "")
    device_conf = pytest.task.get("device", {})
    core_conf = pytest.task.get("cores", {})
    main_core_conf = core_conf.get("core0", {})
    elf_path = main_core_conf.get("elf_path", "")

    """ Dump gcov data to the device_conf["9pfs_path"]/gcda directory """

    if not gcov_enable:
        pytest.skip("Gcov not enable")

    if not os.path.exists(gcov_path):
        pytest.skip(f"Gcov: gcov_path {gcov_path} no exits")

    dump_path = "/tmp/gcda"
    gcda_dir = []
    if device_conf["product"] == "sim":
        compile_path = get_compile_paths(elf_path)
        if compile_path == None:
            pytest.skip("CI Package can't parse compile path")

        gcda_dir.append(compile_path)
    else:
        dump_path = "/share/gcda"
        gcda_dir.append("{}/gcda".format(device_conf["9pfs_path"]))
        for dir in os.listdir(device_conf["9pfs_path"]):
            if dir.startswith("gcov_"):
                gcda_dir.append("{}/{}".format(device_conf["9pfs_path"], dir))

    ret = pytest.product.sendCommand(f"echo > {dump_path}")
    assert ret == 0

    pytest.product.sendCommand(f"gcov -d {dump_path}", "Gcov dump complete")

    gcovTimeout = 0
    ret = 0
    while gcovTimeout < 1200:  # Wait for 20 minutes
        ret = pytest.product.sendCommand(f"ls {dump_path}", "gcda")
        if ret == 0:
            break
        time.sleep(30)
        gcovTimeout += 30

    if ret != 0:
        print("Gcov dump may contain errors")

    """ Use gcov.sh to analyse gcda,gcno file """

    os.makedirs(gcov_conf["result_path"], exist_ok=True)
    command = "{}/gcov.py -t {} -s {}/gcno -o {} --delete ".format(
        gcov_conf["gcov_path"],
        gcov_conf["toolchain"],
        gcov_conf["gcov_path"],
        gcov_conf["result_path"],
    )

    command += "-a "
    for i in gcda_dir:
        command += i + " "

    print(f"Executing: {command}")

    # Spawn the gcov script process

    process = run_command_in_subprocess(command)
    while process.poll() is None:
        pytest.product.sendCommand("hello")
        time.sleep(10)

    assert process.wait() == 0

    if device_conf["product"] == "sim":
        shutil.rmtree(compile_path)


@pytest.mark.run(order=-1)
def test_system_mmleak():
    gdb_conf = pytest.task.get("gdb", {})
    if not gdb_conf or not gdb_conf["enable"] or not gdb_conf["enable_nxplugin"]:
        pytest.skip("GDB Test No Enable")

    def has_mmleak(dir):
        mmleak = list(Path(dir).rglob("nuttx.mmleak"))
        if mmleak:
            logging.warning(f"Found mmleak files: {[str(f) for f in mmleak]}")
            return False
        return True

    logging.info("GDB Check System Mmleak")
    assert has_mmleak(gdb_conf["result"])
