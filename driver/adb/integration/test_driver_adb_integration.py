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

import asyncio
import filecmp
import logging
import os
import random
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import pexpect
import pytest

pytestmark = [
    pytest.mark.dep_config("CONFIG_ADBD_USB_SERVER"),
    pytest.mark.cmd_check("getprop_main"),
]


# @pytest.mark.repeat(10)
class TestAdb:
    target_adb_dev_id = ""

    def test_adb_devices(self):
        dev_psn = self.get_psn()
        assert dev_psn
        logging.info(f"targe psn: {dev_psn}")

        ret = self.adb_devices(dev_psn)
        assert ret == 0
        TestAdb.target_adb_dev_id = dev_psn

    def test_adb_push_pull(self):
        assert TestAdb.target_adb_dev_id
        current_working_directory = self.get_test_script_dir()
        push_folder_path = current_working_directory + "/adb_test"
        if not os.path.isdir(push_folder_path):
            os.makedirs(push_folder_path)
        push_file_path = push_folder_path + "/" + "file_1M.txt"
        if not os.path.isfile(push_file_path):
            self.gen_random_file(push_file_path, 1024 * 1024)

        logging.info(f"push {push_file_path} to /tmp")
        ret = self.adb_push(push_file_path, "/tmp", TestAdb.target_adb_dev_id, 20)
        assert ret == 0
        logging.info(f"push {push_file_path} to /data")
        ret = self.adb_push(push_file_path, "/data", TestAdb.target_adb_dev_id, 20)
        assert ret == 0
        logging.info(f"push {push_folder_path} to /data")
        ret = self.adb_push(push_folder_path, "/data", TestAdb.target_adb_dev_id, 20)
        assert ret == 0
        logging.info(f"push {push_folder_path} to /tmp")
        ret = self.adb_push(push_folder_path, "/tmp", TestAdb.target_adb_dev_id, 20)
        assert ret == 0

        time.sleep(1)

        pull_folder_path = current_working_directory + "/adb_test_pull"
        if os.path.exists(pull_folder_path):
            shutil.rmtree(pull_folder_path)
        pull_file_path = pull_folder_path + "/file_1M.txt"

        logging.info(f"pull /data/adb_test to {pull_folder_path}")
        ret = self.adb_pull(
            "/data/adb_test", pull_folder_path, TestAdb.target_adb_dev_id, 20
        )
        assert ret == 0
        assert filecmp.cmp(push_file_path, pull_file_path, shallow=False)
        shutil.rmtree(pull_folder_path)

        logging.info(f"pull /tmp/adb_test to {pull_folder_path}")
        ret = self.adb_pull(
            "/tmp/adb_test", pull_folder_path, TestAdb.target_adb_dev_id, 20
        )
        assert ret == 0
        assert filecmp.cmp(push_file_path, pull_file_path, shallow=False)
        os.remove(pull_file_path)

        logging.info(f"pull /data/file_1M.txt to {pull_file_path}")
        ret = self.adb_pull(
            "/data/file_1M.txt", pull_file_path, TestAdb.target_adb_dev_id, 20
        )
        assert ret == 0
        assert filecmp.cmp(push_file_path, pull_file_path, shallow=False)
        os.remove(pull_file_path)

        logging.info(f"pull /tmp/file_1M.txt to {pull_file_path}")
        ret = self.adb_pull(
            "/tmp/file_1M.txt", pull_file_path, TestAdb.target_adb_dev_id, 20
        )
        assert ret == 0
        assert filecmp.cmp(push_file_path, pull_file_path, shallow=False)
        shutil.rmtree(pull_folder_path)

        logging.info("rm /data/file_1M.txt")
        ret = pytest.product.sendCommand("rm /data/file_1M.txt", timeout=5)
        assert ret == 0
        logging.info("rm /tmp/file_1M.txt")
        ret = pytest.product.sendCommand("rm /tmp/file_1M.txt", timeout=5)
        assert ret == 0
        logging.info("rm -r /data/adb_test")
        ret = pytest.product.sendCommand("rm -r /data/adb_test", timeout=5)
        assert ret == 0
        logging.info("rm -r /tmp/adb_test")
        ret = pytest.product.sendCommand("rm -r /tmp/adb_test", timeout=5)
        assert ret == 0

    # input 'adb -s xxx shell' in a term, and then exit adb shell
    def test_adb_shell(self):
        assert TestAdb.target_adb_dev_id
        process = pexpect.spawn(
            "adb -s {} shell".format(TestAdb.target_adb_dev_id), maxread=200000
        )
        time.sleep(1)
        try:
            process.sendline("ls \n")
            process.expect("dev", timeout=3)
            logging.info(process.before)
        except pexpect.TIMEOUT:
            logging.error("error: adb shell cmd failed")
            assert False

        try:
            process.sendline("exit")
            process.expect("@", timeout=3)
        except pexpect.TIMEOUT:
            logging.error("error: adb shell exit timeout")
            assert False
        except pexpect.exceptions.EOF:
            logging.info("adb shell exited normally")
        except pexpect.ExceptionPexpect as e:
            logging.error(f"error: adb shell exit failed: {e}")

    # run adb cmd in 4 term at the same time.
    def test_adb_multi_shell(self):
        assert TestAdb.target_adb_dev_id
        test_script_dir = self.get_test_script_dir()
        test_script = os.path.join(test_script_dir, "adb_shell_ls.sh")
        logging.info(f"find file: {test_script}")

        # start 4 shell
        params = [1, 2, 3, 4]
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(
                    self.run_script, test_script, TestAdb.target_adb_dev_id, para
                )
                for para in params
            ]

            # check all result
            for future in as_completed(futures):
                p_id, script_path, success, message = future.result()
                if success:
                    logging.error(
                        f"success: pid {p_id} Script {script_path} with output: {message}"
                    )
                else:
                    logging.error(
                        f"failed: pid {p_id} Script {script_path} with error: {message}"
                    )
                    assert 0

    @pytest.mark.cmd_check("cmd_reboot")
    def test_adb_reboot(self):
        assert TestAdb.target_adb_dev_id
        # pytest.product.sendCommand('reboot')
        pytest.product.reboot()
        # time.sleep(10)
        ret = self.adb_devices(TestAdb.target_adb_dev_id)
        assert ret == 0

    def get_devices_id(self):
        cmd_result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
        cmd_result.wait()
        devices_info = (
            (str(cmd_result.stdout.read()))
            .replace("\\n", " ")
            .replace("\\t", " ")
            .replace("'", "")
            .replace("List", "")
            .replace("of", "", 1)
            .replace("devices", "")
            .replace("attached", "")
            .replace("device", "")
            .split(" ")
        )
        devices_id_list = []
        logging.info(f"subfunc adb devices {devices_info}")
        for device_info in devices_info:
            if device_info != "" and device_info != "b":
                devices_id_list.append(device_info)
        return devices_id_list

    def adb_push(self, src_path, dst_path, dev, time):
        try:
            ret = subprocess.run(
                "adb -s " + dev + " push " + src_path + " " + dst_path,
                shell=True,
                timeout=time,
            )
            if ret.returncode != 0:
                logging.error(f"error: adb push failed: {ret}")
                return -1
        except subprocess.TimeoutExpired:
            logging.error("error: adb push timeout")
            return -1
        return 0

    def adb_pull(self, src_path, dst_path, dev, time):
        try:
            ret = subprocess.run(
                "adb -s " + dev + " pull " + src_path + " " + dst_path,
                shell=True,
                timeout=time,
            )
            if ret.returncode != 0:
                logging.error(ret)
                logging.error(f"error: adb pull failed: {ret}")
                return -1
        except subprocess.TimeoutExpired:
            logging.error("error: adb pull timeout")
            return -1
        return 0

    def gen_random_file(self, path, file_size):
        file_size_in_bytes = file_size
        with open(path, "wb") as file:
            while file.tell() < file_size_in_bytes:
                random_number = random.randint(0, 2**32 - 1).to_bytes(
                    4, byteorder="little"
                )
                file.write(random_number)

    def get_psn(self):
        pattern = r"(.*\bro\.factory\.psn\b.*)|(.*\bpersist\.sys\.sn\b.*)"
        ret, match, output = pytest.product.sendCommandReadUntilPattern(
            "getprop", pattern, timeout=10
        )
        assert ret == 0
        if match:
            psn_str_b = match.group(1)
            logging.info(f"Matched number: {psn_str_b}")
            psn_str = psn_str_b.decode("utf-8")
            index = psn_str.rfind(" ")
            if index != -1:
                target_adb_dev_id = psn_str[index + 1 :]
                target_id = target_adb_dev_id.replace("\n", "")
                target_id = target_id.replace("\r", "")
                if target_id == "0101":
                    logging.error("error: psn is 0101")
                    return 0
                return target_id
            else:
                logging.error("error: can not find space in psn str")
                return 0
        else:
            logging.error("error: can not find psn")
            return 0

    def adb_devices(self, target_id):
        expect_device_is_find = 0
        for i in range(6):
            devices_id_list = self.get_devices_id()
            if devices_id_list == "" or devices_id_list == []:
                logging.error("error: adb_devices do not find any devices!")
            else:
                for id in devices_id_list:
                    if expect_device_is_find == 1:
                        if id == "offline":
                            logging.error("error: target dev is offline")
                            expect_device_is_find = 0
                        break
                    if id == target_id:
                        expect_device_is_find = 1
                        continue
            if expect_device_is_find == 1:
                logging.info("adb devices finish")
                return 0
            else:
                logging.error(f"error {i}: adb devices do not have expect device")
                time.sleep(10)
        else:
            logging.error("error final: adb devices do not have expect device")
            return -1

    def get_test_script_dir(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        return proDir

    def run_script(self, script_path, dev_id, para):
        logging.info(f"run_script: {script_path} {dev_id} {para}")
        try:
            result = subprocess.run(
                ["bash", script_path, dev_id],
                check=True,
                capture_output=True,
                text=True,
                timeout=720,
            )
            return (para, script_path, True, f"script exec finish")
        except subprocess.CalledProcessError as e:
            return (
                para,
                script_path,
                False,
                f"Failed with return code {e.returncode}: {e.stderr.strip()}",
            )
        except subprocess.TimeoutExpired:
            return (para, script_path, False, "timeout")  # cap timeout
        except Exception as e:
            return (para, script_path, False, str(e))  # cap other exception
