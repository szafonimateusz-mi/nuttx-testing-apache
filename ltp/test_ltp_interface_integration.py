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
import time

import pytest


def test_ltp_integration(ltp_case, ltp_expected, timeout):
    logging.info(f"case:{ltp_case} expect:{ltp_expected} timeout:{timeout}")
    ret = pytest.product.sendCommand(
        ltp_case, ltp_expected, timeout=timeout, match_all=False
    )
    assert ret == 0
    ret = pytest.product.sendCommand("echo $?", "0", timeout=5)
    assert ret == 0
