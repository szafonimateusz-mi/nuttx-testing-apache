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

core_lst = ["CP", "AUDIO"]


@pytest.mark.skip(reason="Not ready")
@pytest.mark.dep_config("CONFIG_NETUTILS_REXEC")
@pytest.mark.cmd_check("rexec_main")
def test_rpmsg_uart(p, do_reboot):
    for item in core_lst:
        ret = pytest.product.sendCommand("cat /dev/tty%s &" % item)
        assert ret == 0

        ret = pytest.product.sendCommand(
            'rexec -H %s -r "cat /dev/tty%s > /dev/tty%s &"'
            % (item.lower(), item, item)
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            'echo "uname -a" > /dev/tty%s' % item, item.lower()
        )
        assert ret == 0
