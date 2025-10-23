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

import pytest
from ntfc.lib.performance.perf_data_process import ProcessPerfData


# @pytest.mark.skip("skip performance demo testc case")
@pytest.mark.cmd_check("osperf_main")
def test_osperf():
    """This is a performance test case for osperf.
    First: preapre processing
        1. Remove low power consumption
        2. Restart
        3. Close the upper layer application
        4. Log level
    Second: execute get performance osperf value code
        1. Traverse define.json list
        2. Get metric_name and domain
        3. Generate csv file
        4. Parse log and get performance value
    Third: post processing
        1. Close log level
        2. Remove low power consumption
        3. Restart
        4. Close the upper layer application
    """
    conf_path = os.path.join(os.path.dirname(__file__), ".conf")

    """Step-1: Prepare processing —— To Do """
    logging.info(f"Step-1: execute prepare code")
    # if pytest.product.board == "esp32c3-devkit":
    #     pytest.skip("unsupported at {} {}".format(pytest.product.board, pytest.product.core))
    # if pytest.product.board == "n60" and pytest.product.core == "audio":
    #     pytest.skip("unsupported at {} {}".format(pytest.product.board, pytest.product.core))
    # time.sleep(10)
    # pytest.product.sendCommand('setlogmask r', timeout=120)

    """Step-2: Processing performance indicators 01：osperf """
    logging.info(f"Step-2: execute get performance osperf value code")
    # get data from define.json
    process_data = ProcessPerfData()
    json_data = process_data.read_json_file(os.path.join(conf_path, "define.json"))

    for metric_dic in json_data:
        metric_name, domain = metric_dic["metric_name"], metric_dic["domain"]
        if metric_name == "osperf":

            ret, match, output = pytest.product.sendCommandReadUntilPattern(
                cmd="osperf"
            )
            output_li = output.splitlines()
            assert ret == 0, "osperf command execute failed"

            """step-3: Analyze logs and generate CSV files based on performance metrics data"""
            logging.info(f"Step-3: create performance csv file")

            result_val = os.path.join(pytest.result_dir, "test_osperf.console.txt")
            logging.info(f"result_val: {pytest.result_dir}")
            if process_data._wait_for_file(result_val):

                prod_board = os.getenv("VTF_TEST_BOARD_NAME", "")
                prod_branch = os.getenv("VTF_TEST_BRANCH_NAME", "")
                logging.info(f"product board: {prod_board}")
                logging.info(f"product core: {pytest.product.cur_core}")
                logging.info(f"product branch: {prod_branch}")

                # M01: generate csv of simple scene
                process_data.generate_csv_of_simple_scene(
                    output_li,
                    prod_board,
                    pytest.product.cur_core,
                    prod_branch,
                    pytest.result_dir,
                    domain,
                    metric_name,
                )

                # M02: generate csv of complex scene
                # head_list = ["board", "core", "branch", "Describe", "Max", "Min", "Avg"]
                # data_list = [['', 'ap', '', 'pthread-create', '387716', '183970', '227435'], ['', 'ap', '', 'pthread-switch', '19569', '2416', '3537'], ['', 'ap', '', 'context-switch', '11744', '1745', '2039'], ['', 'ap', '', 'hpwork', '20447', '2267', '2697'], ['', 'ap', '', 'poll-write', '427701', '31247', '41309'], ['', 'ap', '', 'semwait', '19369', '643', '891'], ['', 'ap', '', 'sempost', '679', '537', '567']]
                # process_data.generate_csv_in_the_specified_dir(
                #     ReportDir=pytest.result_dir, Domain=domain, MetricName=metric_name, CsvHeadList=head_list, CsvDataList=data_list
                # )

    """ Post processing —— To Do """
    # e.g. Turn off log level
    # pytest.product.sendCommand('setlogmask 0', timeout=120)
