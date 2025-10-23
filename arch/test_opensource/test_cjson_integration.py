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


@pytest.mark.dep_config("CONFIG_NETUTILS_CJSON_TEST", "CONFIG_TESTING_UNITY")
class TestCjson:
    @pytest.mark.cmd_check("cjson_parse_object_main")
    def test_cjson_parse_object(self):
        ret = pytest.product.sendCommand("cjson_parse_object", "OK")
        assert ret == 0

    @pytest.mark.skip(reason="fail")
    def test_cjson_parse_number(self):
        ret = pytest.product.sendCommand("cjson_parse_number", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_print_string_main")
    def test_cjson_print_string(self):
        ret = pytest.product.sendCommand("cjson_print_string", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_misc_utils_tests")
    def test_cjson_misc_utils_tests(self):
        ret = pytest.product.sendCommand("cjson_misc_utils_tests", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_parse_with_opts_main")
    def test_cjson_parse_with_opts(self):
        ret = pytest.product.sendCommand("cjson_parse_with_opts", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_old_utils_tests_main")
    def test_cjson_old_utils_tests(self):
        ret = pytest.product.sendCommand("cjson_old_utils_tests", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_parse_string_main")
    def test_cjson_parse_string(self):
        ret = pytest.product.sendCommand("cjson_parse_string", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_minify_tests_main")
    def test_cjson_minify_tests(self):
        ret = pytest.product.sendCommand("cjson_minify_tests", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_parse_array_main")
    def test_cjson_parse_array(self):
        ret = pytest.product.sendCommand("cjson_parse_array", "OK")
        assert ret == 0

    @pytest.mark.skip(reason="not have file")
    def test_cjson_parse_examples(self):
        ret = pytest.product.sendCommand("cjson_parse_examples", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_print_array_main")
    def test_cjson_print_array(self):
        ret = pytest.product.sendCommand("cjson_print_array", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_parse_value_main")
    def test_cjson_parse_value(self):
        ret = pytest.product.sendCommand("cjson_parse_value", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_compare_tests_main")
    def test_cjson_compare_tests(self):
        ret = pytest.product.sendCommand("cjson_compare_tests", "OK")
        assert ret == 0

    @pytest.mark.skip(reason="not have file")
    def test_cjson_json_patch_tests(self):
        ret = pytest.product.sendCommand("cjson_json_patch_tests", "OK")
        assert ret == 0

    @pytest.mark.skip(reason="fail")
    def test_cjson_print_number(self):
        ret = pytest.product.sendCommand("cjson_print_number", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_cjson_add_main")
    def test_cjson_cjson_add(self):
        ret = pytest.product.sendCommand("cjson_cjson_add", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_print_object_main")
    def test_cjson_print_object(self):
        ret = pytest.product.sendCommand("cjson_print_object", "OK")
        assert ret == 0

    @pytest.mark.skip(reason="fail")
    def test_cjson_misc_tests(self):
        ret = pytest.product.sendCommand("cjson_misc_tests", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_parse_hex4_main")
    def test_cjson_parse_hex4(self):
        ret = pytest.product.sendCommand("cjson_parse_hex4", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_readme_examples_main")
    def test_cjson_readme_examples(self):
        ret = pytest.product.sendCommand("cjson_readme_examples", "OK")
        assert ret == 0

    @pytest.mark.cmd_check("cjson_test_main")
    def test_cjson_test(self):
        ret = pytest.product.sendCommand("cjson_test", "Monday")
        assert ret == 0
