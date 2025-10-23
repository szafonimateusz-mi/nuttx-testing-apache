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


class TestUorb:

    @pytest.mark.dep_config("CONFIG_UORB", "CONFIG_UORB_TESTS")
    @pytest.mark.cmd_check("uorb_unit_test_main")
    def test_api(self):
        ret = pytest.product.sendCommand("uorb_unit_test", "TEST PASS")
        assert ret == 0
        # ret = pytest.product.sendCommand('uorb_multi_test', 'TEST PASS')
        # assert ret == 0

    @pytest.mark.dep_config("CONFIG_UORB", "CONFIG_UORB_LISTENER")
    @pytest.mark.cmd_check("uorb_listener_main")
    def test_uorb_listener_help(self):
        ret = pytest.product.sendCommand("uorb_listener -h", "Commands:")
        assert ret == 0
        ret = pytest.product.sendCommand("uorb_listener -help", "Commands:")
        assert ret == 0

    @pytest.mark.dep_config(
        "CONFIG_UORB_TEST",
        "CONFIG_UORB_ADVERTISE_DEMO",
        "CONFIG_UORB_CASE_TEST",
        "CONFIG_BOARDCTL_RESET",
    )
    @pytest.mark.cmd_check("uorb_advertise_demo_main", "reboot")
    def test_uORB(self):

        uorb_dic = {"ap": ["cp", "audio"], "cp": ["ap", "audio"], "audio": ["ap", "cp"]}

        for item in uorb_dic:
            # switch to server core
            pytest.product.device._child.sendcontrol("c")
            if item != "ap":
                ret = pytest.product.sendCommand(
                    "cu -l /dev/tty%s\n" % item.upper(), "%s>" % item, flag="%s>" % item
                )
                assert ret == 0
            # start the orb advertise: sensor_rgb
            ret = pytest.product.sendCommand(
                "uorb_advertise_demo &", "orb advertise", flag="%s>" % item
            )
            assert ret == 0

            for client in uorb_dic[item]:
                # switch to client core
                pytest.product.device._child.sendcontrol("c")
                if client != "ap":
                    ret = pytest.product.sendCommand(
                        "cu -l /dev/tty%s\n" % client.upper(),
                        "%s>" % client,
                        flag="%s>" % client,
                    )
                    assert ret == 0
                # listen the orb advertise
                ret = pytest.product.sendCommand(
                    "uorb_listener -n 5 sensor_rgb",
                    "Total number of received Message:5/5",
                    flag="%s>" % client,
                )
                assert ret == 0

            # pytest.product.sendCommand("reboot", "ap>", timeout=60)
            pytest.product.reboot()
