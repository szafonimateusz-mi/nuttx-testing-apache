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

pytestmark = [pytest.mark.dep_config("CONFIG_MBEDTLS_TEST")]


@pytest.mark.cmd_check("mbedtls_test_suite_aes_cbc_c_main")
def test_suite_aes_cbc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_cbc_c /data/mbedtls/test_suite_aes.cbc.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aes_cfb_c_main")
def test_suite_aes_cfb():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_cfb_c /data/mbedtls/test_suite_aes.cfb.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aes_ecb_c_main")
def test_suite_aes_ecb():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_ecb_c /data/mbedtls/test_suite_aes.ecb.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aes_ofb_c_main")
def test_suite_aes_ofb():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_ofb_c /data/mbedtls/test_suite_aes.ofb.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aes_rest_c_main")
def test_suite_aes_rest():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_rest_c /data/mbedtls/test_suite_aes.rest.datax",
        "PASSED",
        timeout=60,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aes_xts_c_main")
def test_suite_aes_xts():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aes_xts_c /data/mbedtls/test_suite_aes.xts.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_alignment_c_main")
def test_suite_alignment():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_alignment_c /data/mbedtls/test_suite_alignment.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_aria_c_main")
def test_suite_aria():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_aria_c /data/mbedtls/test_suite_aria.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_asn1parse_c_main")
def test_suite_asn1parse():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_asn1parse_c /data/mbedtls/test_suite_asn1parse.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_asn1write_c_main")
def test_suite_asn1write():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_asn1write_c /data/mbedtls/test_suite_asn1write.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_base64_c_main")
def test_suite_base64():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_base64_c /data/mbedtls/test_suite_base64.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_core_generated_c_main")
def test_suite_bignum_core_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_core_generated_c /data/mbedtls/test_suite_bignum_core.generated.datax",
        "PASSED",
        timeout=60,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_core_misc_c_main")
def test_suite_bignum_core_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_core_misc_c /data/mbedtls/test_suite_bignum_core.misc.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_generated_c_main")
def test_suite_bignum_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_generated_c /data/mbedtls/test_suite_bignum.generated.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_bignum_misc_c_main")
# def test_suite_bignum_misc():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_bignum_misc_c /data/mbedtls/test_suite_bignum.misc.datax', "PASSED", timeout=30)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_mod_generated_c_main")
def test_suite_bignum_mod_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_mod_generated_c /data/mbedtls/test_suite_bignum_mod.generated.datax",
        "PASSED",
        timeout=70,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_mod_misc_c_main")
def test_suite_bignum_mod_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_mod_misc_c /data/mbedtls/test_suite_bignum_mod.misc.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_mod_raw_c_main")
def test_suite_bignum_mod_raw():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_mod_raw_c /data/mbedtls/test_suite_bignum_mod_raw.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_mod_raw_generated_c_main")
def test_suite_bignum_mod_raw_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_mod_raw_generated_c /data/mbedtls/test_suite_bignum_mod_raw.generated.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_bignum_random_c_main")
def test_suite_bignum_random():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_bignum_random_c /data/mbedtls/test_suite_bignum_random.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_camellia_c_main")
def test_suite_camellia():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_camellia_c /data/mbedtls/test_suite_camellia.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ccm_c_main")
def test_suite_ccm():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ccm_c /data/mbedtls/test_suite_ccm.datax",
        "PASSED",
        timeout=300,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_chacha20_c_main")
def test_suite_chacha20():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_chacha20_c /data/mbedtls/test_suite_chacha20.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_chachapoly_c_main")
def test_suite_chachapoly():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_chachapoly_c /data/mbedtls/test_suite_chachapoly.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_aes_c_main")
def test_suite_cipher_aes():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_aes_c /data/mbedtls/test_suite_cipher.aes.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_aria_c_main")
def test_suite_cipher_aria():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_aria_c /data/mbedtls/test_suite_cipher.aria.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_camellia_c_main")
def test_suite_cipher_camellia():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_camellia_c /data/mbedtls/test_suite_cipher.camellia.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_ccm_c_main")
def test_suite_cipher_ccm():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_ccm_c /data/mbedtls/test_suite_cipher.ccm.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_chacha20_c_main")
def test_suite_cipher_chacha20():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_chacha20_c /data/mbedtls/test_suite_cipher.chacha20.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_chachapoly_c_main")
def test_suite_cipher_chachapoly():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_chachapoly_c /data/mbedtls/test_suite_cipher.chachapoly.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_des_c_main")
def test_suite_cipher_des():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_des_c /data/mbedtls/test_suite_cipher.des.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_gcm_c_main")
def test_suite_cipher_gcm():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_gcm_c /data/mbedtls/test_suite_cipher.gcm.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_misc_c_main")
def test_suite_cipher_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_misc_c /data/mbedtls/test_suite_cipher.misc.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_nist_kw_c_main")
def test_suite_cipher_nist_kw():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_nist_kw_c /data/mbedtls/test_suite_cipher.nist_kw.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_null_c_main")
def test_suite_cipher_null():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_null_c /data/mbedtls/test_suite_cipher.null.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cipher_padding_c_main")
def test_suite_cipher_padding():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cipher_padding_c /data/mbedtls/test_suite_cipher.padding.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_cmac_c_main")
def test_suite_cmac():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_cmac_c /data/mbedtls/test_suite_cmac.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_common_c_main")
def test_suite_common():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_common_c /data/mbedtls/test_suite_common.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_constant_time_c_main")
def test_suite_constant_time():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_constant_time_c /data/mbedtls/test_suite_constant_time.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_constant_time_hmac_c_main")
def test_suite_constant_time_hmac():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_constant_time_hmac_c /data/mbedtls/test_suite_constant_time_hmac.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_ctr_drbg_c_main")
# def test_suite_ctr_drbg():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_ctr_drbg_c /data/mbedtls/test_suite_ctr_drbg.datax', "PASSED", timeout=120)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_debug_c_main")
def test_suite_debug():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_debug_c /data/mbedtls/test_suite_debug.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_des_c_main")
def test_suite_des():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_des_c /data/mbedtls/test_suite_des.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_dhm_c_main")
# def test_suite_dhm():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_dhm_c /data/mbedtls/test_suite_dhm.datax', "PASSED", timeout=20)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ecdh_c_main")
def test_suite_ecdh():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ecdh_c /data/mbedtls/test_suite_ecdh.datax",
        "PASSED",
        timeout=60,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ecdsa_c_main")
def test_suite_ecdsa():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ecdsa_c /data/mbedtls/test_suite_ecdsa.datax",
        "PASSED",
        timeout=80,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ecjpake_c_main")
def test_suite_ecjpake():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ecjpake_c /data/mbedtls/test_suite_ecjpake.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ecp_c_main")
def test_suite_ecp():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ecp_c /data/mbedtls/test_suite_ecp.datax",
        "PASSED",
        timeout=240,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_ecp_generated_c_main")
def test_suite_ecp_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_ecp_generated_c /data/mbedtls/test_suite_ecp.generated.datax",
        "PASSED",
        timeout=120,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_entropy_c_main")
def test_suite_entropy():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_entropy_c /data/mbedtls/test_suite_entropy.datax",
        "PASSED",
        timeout=120,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_error_c_main")
def test_suite_error():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_error_c /data/mbedtls/test_suite_error.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes128_de_c_main")
def test_suite_gcm_aes128_de():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes128_de_c /data/mbedtls/test_suite_gcm.aes128_de.datax",
        "PASSED",
        timeout=600,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes128_en_c_main")
def test_suite_gcm_aes128_en():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes128_en_c /data/mbedtls/test_suite_gcm.aes128_en.datax",
        "PASSED",
        timeout=900,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes192_de_c_main")
def test_suite_gcm_aes192_de():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes192_de_c /data/mbedtls/test_suite_gcm.aes192_de.datax",
        "PASSED",
        timeout=300,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes192_en_c_main")
def test_suite_gcm_aes192_en():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes192_en_c /data/mbedtls/test_suite_gcm.aes192_en.datax",
        "PASSED",
        timeout=600,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes256_de_c_main")
def test_suite_gcm_aes256_de():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes256_de_c /data/mbedtls/test_suite_gcm.aes256_de.datax",
        "PASSED",
        timeout=300,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_aes256_en_c_main")
def test_suite_gcm_aes256_en():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_aes256_en_c /data/mbedtls/test_suite_gcm.aes256_en.datax",
        "PASSED",
        timeout=450,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_camellia_c_main")
def test_suite_gcm_camellia():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_camellia_c /data/mbedtls/test_suite_gcm.camellia.datax",
        "PASSED",
        timeout=120,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_gcm_misc_c_main")
def test_suite_gcm_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_gcm_misc_c /data/mbedtls/test_suite_gcm.misc.datax",
        "PASSED",
        timeout=120,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_hkdf_c_main")
def test_suite_hkdf():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_hkdf_c /data/mbedtls/test_suite_hkdf.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_hmac_drbg_misc_c_main")
# def test_suite_hmac_drbg_misc():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_hmac_drbg_misc_c /data/mbedtls/test_suite_hmac_drbg.misc.datax', "PASSED", timeout=20)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_hmac_drbg_nopr_c_main")
def test_suite_hmac_drbg_nopr():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_hmac_drbg_nopr_c /data/mbedtls/test_suite_hmac_drbg.nopr.datax",
        "PASSED",
        timeout=30,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_hmac_drbg_no_reseed_c_main")
def test_suite_hmac_drbg_no_reseed():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_hmac_drbg_no_reseed_c /data/mbedtls/test_suite_hmac_drbg.no_reseed.datax",
        "PASSED",
        timeout=180,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_hmac_drbg_pr_c_main")
def test_suite_hmac_drbg_pr():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_hmac_drbg_pr_c /data/mbedtls/test_suite_hmac_drbg.pr.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_lmots_c_main")
def test_suite_lmots():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_lmots_c /data/mbedtls/test_suite_lmots.datax",
        "PASSED",
        timeout=260,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_lms_c_main")
def test_suite_lms():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_lms_c /data/mbedtls/test_suite_lms.datax",
        "PASSED",
        timeout=360,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_md_c_main")
# def test_suite_md():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_md_c /data/mbedtls/test_suite_md.datax', "PASSED", timeout=60)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_mdx_c_main")
def test_suite_mdx():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_mdx_c /data/mbedtls/test_suite_mdx.datax",
        "PASSED",
        timeout=120,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_memory_buffer_alloc_c_main")
def test_suite_memory_buffer_alloc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_memory_buffer_alloc_c /data/mbedtls/test_suite_memory_buffer_alloc.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_mps_c_main")
def test_suite_mps():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_mps_c /data/mbedtls/test_suite_mps.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_net_c_main")
# def test_suite_net():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_net_c /data/mbedtls/test_suite_net.datax', "PASSED", timeout=175)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_nist_kw_c_main")
def test_suite_nist_kw():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_nist_kw_c /data/mbedtls/test_suite_nist_kw.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_oid_c_main")
def test_suite_oid():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_oid_c /data/mbedtls/test_suite_oid.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_pem_c_main")
def test_suite_pem():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_pem_c /data/mbedtls/test_suite_pem.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_pk_c_main")
def test_suite_pk():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_pk_c /data/mbedtls/test_suite_pkcs12.datax",
        "PASSED",
        timeout=20,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_pkcs12_c_main")
# def test_suite_pkcs12():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkcs12_c /data/mbedtls/test_suite_pkcs1_v15.datax', "PASSED", timeout=75)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkcs1_v15_c_main")
# def test_suite_pkcs1_v15():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkcs1_v15_c /data/mbedtls/test_suite_pkcs1_v21.datax', "PASSED", timeout=75)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkcs1_v21_c_main")
# def test_suite_pkcs1_v21():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkcs1_v21_c /data/mbedtls/test_suite_pkcs5.datax', "PASSED", timeout=75)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkcs5_c_main")
# def test_suite_pkcs5():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkcs5_c /data/mbedtls/test_suite_pkcs7.datax', "PASSED", timeout=75)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkcs7_c_main")
# def test_suite_pkcs7():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkcs7_c /data/mbedtls/test_suite_pk.datax', "PASSED", timeout=20)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkparse_c_main")
# def test_suite_pkparse():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkparse_c /data/mbedtls/test_suite_pkparse.datax', "PASSED", timeout=20)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_pkwrite_c_main")
# def test_suite_pkwrite():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_pkwrite_c /data/mbedtls/test_suite_pkwrite.datax', "PASSED", timeout=20)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_platform_util_c_main")
def test_suite_platform_util():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_platform_util_c /data/mbedtls/test_suite_platform_util.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_poly1305_c_main")
def test_suite_poly1305():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_poly1305_c /data/mbedtls/test_suite_poly1305.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_attributes_c_main")
def test_suite_psa_crypto_attributes():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_attributes_c /data/mbedtls/test_suite_psa_crypto_attributes.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_c_main")
# def test_suite_psa_crypto():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_c /data/mbedtls/test_suite_psa_crypto.datax', "PASSED", timeout=20)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_driver_wrappers_c_main")
def test_suite_psa_crypto_driver_wrappers():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_driver_wrappers_c /data/mbedtls/test_suite_psa_crypto_driver_wrappers.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_entropy_c_main")
def test_suite_psa_crypto_entropy():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_entropy_c /data/mbedtls/test_suite_psa_crypto_entropy.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_generate_key_generated_c_main")
def test_suite_psa_crypto_generate_key_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_generate_key_generated_c /data/mbedtls/test_suite_psa_crypto_generate_key.generated.datax",
        "PASSED",
        timeout=180,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_hash_c_main")
# def test_suite_psa_crypto_hash():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_hash_c /data/mbedtls/test_suite_psa_crypto_hash.datax', "PASSED", timeout=25)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_init_c_main")
def test_suite_psa_crypto_init():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_init_c /data/mbedtls/test_suite_psa_crypto_init.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_metadata_c_main")
def test_suite_psa_crypto_metadata():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_metadata_c /data/mbedtls/test_suite_psa_crypto_metadata.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_not_supported_generated_c_main")
def test_suite_psa_crypto_not_supported_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_not_supported_generated_c /data/mbedtls/test_suite_psa_crypto_not_supported.generated.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_not_supported_misc_c_main")
def test_suite_psa_crypto_not_supported_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_not_supported_misc_c /data/mbedtls/test_suite_psa_crypto_not_supported.misc.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_op_fail_generated_c_main")
def test_suite_psa_crypto_op_fail_generated():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_op_fail_generated_c /data/mbedtls/test_suite_psa_crypto_op_fail.generated.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_op_fail_misc_c_main")
def test_suite_psa_crypto_op_fail_misc():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_op_fail_misc_c /data/mbedtls/test_suite_psa_crypto_op_fail.misc.datax",
        "PASSED",
        timeout=175,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_pake_c_main")
def test_suite_psa_crypto_pake():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_pake_c /data/mbedtls/test_suite_psa_crypto_pake.datax",
        "PASSED",
        timeout=240,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_persistent_key_c_main")
# def test_suite_psa_crypto_persistent_key():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_persistent_key_c /data/mbedtls/test_suite_psa_crypto_persistent_key.datax', "PASSED", timeout=25)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_se_driver_hal_c_main")
def test_suite_psa_crypto_se_driver_hal():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_se_driver_hal_c /data/mbedtls/test_suite_psa_crypto_se_driver_hal.datax",
        "PASSED",
        timeout=130,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_se_driver_hal_mocks_c_main")
def test_suite_psa_crypto_se_driver_hal_mocks():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_psa_crypto_se_driver_hal_mocks_c /data/mbedtls/test_suite_psa_crypto_se_driver_hal_mocks.datax",
        "PASSED",
        timeout=155,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_slot_management_c_main")
# def test_suite_psa_crypto_slot_management():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_slot_management_c /data/mbedtls/test_suite_psa_crypto_slot_management.datax', "PASSED", timeout=25)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_storage_format_current_c_main")
# def test_suite_psa_crypto_storage_format_current():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_storage_format_current_c /data/mbedtls/test_suite_psa_crypto_storage_format.current.datax', "PASSED", timeout=75)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_storage_format_misc_c_main")
# def test_suite_psa_crypto_storage_format_misc():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_storage_format_misc_c /data/mbedtls/test_suite_psa_crypto_storage_format.misc.datax', "PASSED", timeout=25)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_psa_crypto_storage_format_v0_c_main")
# def test_suite_psa_crypto_storage_format_v0():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_crypto_storage_format_v0_c /data/mbedtls/test_suite_psa_crypto_storage_format.v0.datax', "PASSED", timeout=20)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_psa_its_c_main")
# def test_suite_psa_its():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_psa_its_c /data/mbedtls/test_suite_psa_its.datax', "PASSED", timeout=25)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_random_c_main")
def test_suite_random():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_random_c /data/mbedtls/test_suite_random.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_rsa_c_main")
# def test_suite_rsa():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_rsa_c /data/mbedtls/test_suite_rsa.datax', "PASSED", timeout=25)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_shax_c_main")
# def test_suite_shax():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_shax_c /data/mbedtls/test_suite_shax.datax', "PASSED", timeout=25)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_ssl_c_main")
# def test_suite_ssl():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_ssl_c /data/mbedtls/test_suite_ssl.datax', "PASSED", timeout=20)
# 	assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_timing_c_main")
def test_suite_timing():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_timing_c /data/mbedtls/test_suite_timing.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


@pytest.mark.cmd_check("mbedtls_test_suite_version_c_main")
def test_suite_version():
    ret = pytest.product.sendCommand(
        "mbedtls_test_suite_version_c /data/mbedtls/test_suite_version.datax",
        "PASSED",
        timeout=125,
    )
    assert ret == 0


# @pytest.mark.cmd_check("mbedtls_test_suite_x509parse_c_main")
# def test_suite_x509parse():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_x509parse_c /data/mbedtls/test_suite_x509parse.datax', "PASSED", timeout=20)
# 	assert ret == 0

# @pytest.mark.cmd_check("mbedtls_test_suite_x509write_c_main")
# def test_suite_x509write():
# 	ret = pytest.product.sendCommand('mbedtls_test_suite_x509write_c /data/mbedtls/test_suite_x509write.datax', "PASSED", timeout=20)
# 	assert ret == 0
