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

pytestmark = [
    pytest.mark.dep_config("CONFIG_CRYPTO_CRYPTODEV_SOFTWARE"),
    pytest.mark.cmd_check("cmocka"),
]


@pytest.mark.cmd_check("cmocka_aescbc")
def test_crypto_aescbc_integration():

    cmd = f"cmocka -s cmocka_aescbc -t test_aescbc"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_aescmac")
def test_crypto_aescmac_integration():

    cmd = f"cmocka -s cmocka_aescmac -t test_aescmac"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_aesctr")
def test_crypto_aesctr_integration():

    cmd = f"cmocka -s cmocka_aesctr -t test_aesctr"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_aesxts")
def test_crypto_aesxts_integration():

    cmd = f"cmocka -s cmocka_aesxts -t test_aesxts"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_crc32")
def test_crypto_crc32_integration():

    cmd = f"cmocka -s cmocka_crc32 -t test_crc32"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_des3cbc")
def test_crypto_des3cbc_integration():

    cmd = f"cmocka -s cmocka_des3cbc -t test_3descbc"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


@pytest.mark.cmd_check("cmocka_dhm")
def test_crypto_dhm_integration():

    cmd = f"cmocka -s cmocka_dhm -t test_dhm"
    EXPECTED_LIST = ["[  PASSED  ]", "Cmocka Test Completed"]

    ret = pytest.product.sendCommand(cmd, EXPECTED_LIST, timeout=15)
    assert ret == 0


TEST_CASES_HASH = [
    pytest.param(
        "test_hash_md5",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hash_md5",
    ),
    pytest.param(
        "test_hash_sha1",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hash_sha1",
    ),
    pytest.param(
        "test_hash_sha256",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hash_sha256",
    ),
    pytest.param(
        "test_hash_sha512",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hash_sha512",
    ),
]


@pytest.mark.cmd_check("cmocka_hash")
@pytest.mark.parametrize("case, expected_list", TEST_CASES_HASH)
def test_crypto_hash_integration(case, expected_list) -> None:
    """Execute crypto hash integration tests"""

    BASE_CMD = "cmocka_hash"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=15)
    assert ret == 0


TEST_CASES_HAMC = [
    pytest.param(
        "test_hmac_md5",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hmac_md5",
    ),
    pytest.param(
        "test_hmac_sha1",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hmac_sha1",
    ),
    pytest.param(
        "test_hmac_sha256",
        ["[  PASSED  ]", "Cmocka Test Completed"],
        id="test_hmac_sha256",
    ),
]


@pytest.mark.cmd_check("cmocka_hmac")
@pytest.mark.parametrize("case, expected_list", TEST_CASES_HAMC)
def test_crypto_hmac_integration(case, expected_list) -> None:
    """Execute crypto hmac integration tests"""

    BASE_CMD = "cmocka_hmac"
    cmd = f"cmocka -s {BASE_CMD} -t {case}"

    ret = pytest.product.sendCommand(cmd, expected_list, timeout=15)
    assert ret == 0
