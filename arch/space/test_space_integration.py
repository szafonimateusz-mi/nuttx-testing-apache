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

import csv
import os
import re
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../../")
import logging

import pytest


def gen_csv(head, data, kind):
    csv_file = os.path.join(pytest.result_dir, kind + "_data.csv")
    with open(csv_file, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(head)
        # write the data
        writer.writerows(data)


def getSpace(type="free"):
    if type == "free":
        pattern = r"\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+Umem"
        status, matches, data = pytest.product.sendCommandReadUntilPattern(
            "free", pattern, timeout=1
        )
        if status == 0 and matches is not None:
            for i in data.split("\n"):
                if "Umem" in i:
                    logging.info(i)
                    logging.info(i.split())
                    return i.split()[:4]
        else:
            return []
    elif type == "df -h":
        _, _, data = pytest.product.sendCommandReadUntilPattern("df -h", timeout=1)
        return data


@pytest.mark.cmd_check("cmd_free")
def test_free(core, switch_to_core):
    csv_head = ["Board", "Core", "Name", "Total", "Used", "Free", "Largest"]
    csv_datas = []
    csv_data = []
    contend = getSpace()
    if contend == []:
        logging.info("free command output is null")
    else:
        csv_data.append("free_start")
        csv_data += contend
        csv_datas.append(csv_data)
        gen_csv(csv_head, csv_datas, kind="free")


@pytest.mark.cmd_check("cmd_df")
def test_df(core, switch_to_core):
    contend = getSpace("df -h")
    csv_head = ["Mounted", "Size", "Available", "Filesystem"]
    csv_datas = []
    for i in contend.split("\n"):
        if "Mounted" in i:
            continue
        csv_data = []
        if len(i.split()) > 2:
            csv_data = i.split()
        else:
            continue
        csv_datas.append(csv_data)
    gen_csv(csv_head, csv_datas, kind="df")
