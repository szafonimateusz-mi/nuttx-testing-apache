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
from datetime import datetime, timedelta

import pytest
import pytz


@pytest.fixture(scope="function")
def timezone_pre_post():
    logging.info("Exec timezone_pre")
    pytest.product.sendCommand("set TZ Asia/Shanghai", timeout=2)
    shanghai_datetime = datetime.now()
    shanghai_datetime_str = shanghai_datetime.strftime("%b %d %H:%M:%S %Y")
    logging.info(f'Set Shanghai ime: date -s "{shanghai_datetime_str}"')
    pytest.product.sendCommand(f'date -s "{shanghai_datetime_str}"', timeout=2)

    expect_shanghai_datetime_list = []
    logging.info(":")
    for i in range(6):
        shanghai_datetime_tmp = shanghai_datetime + timedelta(seconds=i)

        shanghai_year = shanghai_datetime_tmp.strftime("%Y")
        shanghai_month = shanghai_datetime_tmp.strftime("%b")
        shanghai_day = shanghai_datetime_tmp.strftime("%d").zfill(2)
        shanghai_week = shanghai_datetime_tmp.strftime("%a")
        shanghai_hour = shanghai_datetime_tmp.strftime("%H").zfill(2)
        shanghai_minute = shanghai_datetime_tmp.strftime("%M").zfill(2)
        shanghai_second = shanghai_datetime_tmp.strftime("%S").zfill(2)
        expect_shanghai_datetime = "{}, {} {} {}:{}:{} {}".format(
            shanghai_week,
            shanghai_month,
            shanghai_day,
            shanghai_hour,
            shanghai_minute,
            shanghai_second,
            shanghai_year,
        )
        # 上海时间
        expect_shanghai_datetime_list.append(expect_shanghai_datetime)
        logging.info(f"{expect_shanghai_datetime}")

    ret = pytest.product.sendCommand(
        "date", expect_shanghai_datetime_list, match_all=False
    )
    (
        logging.info(f"Match[{ret}], Set Shanghai time success")
        if ret >= 0
        else logging.info("Set Shanghai time fail")
    )
    assert ret >= 0

    yield shanghai_datetime

    logging.info("Exec timezone_post")
    pytest.product.sendCommand("set TZ Asia/Shanghai", timeout=2)
    ret = pytest.product.sendCommand(
        "date", expect_shanghai_datetime_list, match_all=False
    )
    (
        logging.info(f"Match Shanghai time[{ret}]")
        if ret >= 0
        else logging.info("Match Shanghai time fail")
    )
    assert ret >= 0


def time_zone_test(area: str, tz: str, base_time, match_accuracy=5):
    target_area_time_zone = pytz.timezone(tz)
    target_area_datetime = base_time.astimezone(target_area_time_zone)
    expect_target_area_datetime_list = []

    pytest.product.sendCommand(f"set TZ :{tz}", timeout=2)
    logging.info(f"Change{area}time zone")

    logging.info(f"Expect{area}time:")
    for i in range(match_accuracy + 1):
        target_datetime = target_area_datetime + timedelta(seconds=i)
        # logging.info(f"{area}时间: {target_datetime.strftime('%b %d %H:%M:%S %Y')}")
        target_area_year = target_datetime.strftime("%Y")
        target_area_month = target_datetime.strftime("%b")
        target_area_day = target_datetime.strftime("%d").zfill(2)
        target_area_week = target_datetime.strftime("%a")
        target_area_hour = target_datetime.strftime("%H").zfill(2)
        target_area_minute = target_datetime.strftime("%M").zfill(2)
        target_area_second = target_datetime.strftime("%S").zfill(2)
        expect_target_area_time = "{}, {} {} {}:{}:{} {}".format(
            target_area_week,
            target_area_month,
            target_area_day,
            target_area_hour,
            target_area_minute,
            target_area_second,
            target_area_year,
        )
        expect_target_area_datetime_list.append(expect_target_area_time)
        logging.info(f"{expect_target_area_time}")

    ret = pytest.product.sendCommand(
        "date", expect_target_area_datetime_list, match_all=False
    )
    (
        logging.info(f"Match[{ret}],{area}time success")
        if ret >= 0
        else logging.info(f"Match {area}time fail")
    )
    assert ret >= 0


@pytest.mark.dep_config("CONFIG_LIBC_LOCALTIME", "CONFIG_RTC_RPMSG_SERVER")
@pytest.mark.cmd_check("cmd_date", "cmd_set")
class TestTimeZone:

    def test_newyork_time_zone(self, timezone_pre_post):
        # pattern = br"(?P<week>[MTWFS][a-z]{2,3}), (?P<month>[A-Z][a-z]{2,3}) (?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}) (?P<year>\d{4})"
        time_zone_test("美国纽约", "America/New_York", timezone_pre_post)

    def test_auckland_time_zone(self, timezone_pre_post):
        # 新西兰 奥克兰 时间
        time_zone_test("新西兰奥克兰", "Pacific/Auckland", timezone_pre_post)

    def test_waitangi_time_zone(self, timezone_pre_post):
        # 新西兰 Waitangi 时间
        time_zone_test("新西兰Waitangi", "Pacific/Chatham", timezone_pre_post)
