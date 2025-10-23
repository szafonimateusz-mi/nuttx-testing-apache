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

import pytest

pytestmark = pytest.mark.dep_config("CONFIG_UORB", "CONFIG_UORB_LISTENER")
pytestmark = pytest.mark.cmd_check("uorb_listener_main")


class TestUorbP:
    topicList = []
    topicList1 = []
    topicList2 = []
    topicList3 = []
    topicList4 = []


class TestUorb(TestUorbP):
    def setup_class(self):
        TestUorbP.topicList = ["sensor_accel0", "sensor_gyro0", "sensor_gnss0"]
        TestUorbP.topicList1 = ["sensor_accel0", "sensor_gyro0"]
        TestUorbP.topicList2 = ["sensor_wake_gesture0"]
        # test set batch sensor
        TestUorbP.topicList3 = ["sensor_accel0", "sensor_gyro0"]

        logging.info("TestUorbP.topicList %s" % TestUorbP.topicList)
        logging.info("TestUorbP.topicList1 %s" % TestUorbP.topicList1)
        logging.info("TestUorbP.topicList3%s" % TestUorbP.topicList3)

    def test_uorb_listener_topic1(self):
        # one topic
        for topic in TestUorbP.topicList:
            logging.info("TestUorbP.topicList %s" % TestUorbP.topicList)
            logging.info(f"topic {topic}")
            # one topic, one argument
            ret = pytest.product.sendCommand(
                f"uorb_listener -n 10 {topic}", "Total number of received Message:10/10"
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -n -1 %s" % topic, "Commands:"
            )
            assert ret == 0

            # test rate
            ret = pytest.product.sendCommand(
                "uorb_listener -n 10 -r 25 %s" % topic,
                "Total number of received Message:10/10",
            )
            assert ret == 0
            # str_temp = 'uorb_listener -n 10 -r 25 %s'
            # assertRet(self, p, logFile, pattern, str_temp, str2, 25, TestUorbP.topicList)

            ret = pytest.product.sendCommand(
                "uorb_listener -n 10 -r 50 %s" % topic,
                "Total number of received Message:10/10",
            )
            assert ret == 0
            # assertRet(self, p, logFile, pattern, str_temp, str2, 25, TestUorbP.topicList)
            ret = pytest.product.sendCommand(
                "uorb_listener -n 10 -r 100 %s" % topic,
                "Total number of received Message:10/10",
            )
            assert ret == 0
            # assertRet(self, p, logFile, pattern, str_temp, str2, 25, TestUorbP.topicList)
            ret = pytest.product.sendCommand(
                "uorb_listener -n 10 -r -1 %s" % topic, "Commands:"
            )
            # assertRet(self, p, logFile, pattern, str_temp, str2, 25, TestUorbP.topicList)
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -h -r 1 %s" % topic, "Commands:"
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -r 1 -h %s" % topic, "Commands:"
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -h -n 1 %s" % topic, "Commands:"
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -n 1 -h %s" % topic, "Commands:"
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -h -r 1 -n 10 %s" % topic, "Commands:"
            )
            assert ret == 0

    # two topics
    def test_uorb_listener_topic2(self):
        expect = []
        for topic in TestUorbP.topicList1[:2]:
            topic_name = topic
            combined_string = "Object name:%s" % topic_name
            expect.append(combined_string)
        expect.append("Total number of received Message:10/10")
        # two topics,one argument

        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 %s,%s"
            % (TestUorbP.topicList1[0], TestUorbP.topicList1[1]),
            [expect[1], expect[0], expect[2]],
        )
        assert ret == 0

        # two topics,two argument
        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 -r 25 %s,%s"
            % (TestUorbP.topicList1[0], TestUorbP.topicList1[1]),
            [expect[1], expect[0], expect[2]],
        )
        assert ret == 0

        # two topics,three argument
        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 -r 25 -h %s,%s"
            % (TestUorbP.topicList1[0], TestUorbP.topicList1[1]),
            "Commands:",
        )
        assert ret == 0

    # three topics
    def test_uorb_listener_topic3(self):
        expect = []
        for topic in TestUorbP.topicList3[:2]:
            topic_name = topic
            combined_string = "Object name:%s" % topic_name
            expect.append(combined_string)
        expect.append("Total number of received Message:10/10")
        # two topics,one argument
        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            [expect[1], expect[0], expect[2]],
        )
        logging.info("ret%s" % ret)

        assert ret == 0

        # two topics,two argument
        ret = pytest.product.sendCommand(
            "uorb_listener -r 25 -n 10 %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            [expect[1], expect[0], expect[2]],
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            "uorb_listener -r 50 -n 10 %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            [expect[1], expect[0], expect[2]],
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            "uorb_listener -r 100 -n 10 %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            [expect[1], expect[0], expect[2]],
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            "uorb_listener -r 100 -h %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            "Commands:",
        )
        assert ret == 0

        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 -h %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            "Commands:",
        )

        # three topics,three argument
        ret = pytest.product.sendCommand(
            "uorb_listener -n 10 -h -r 25 %s,%s"
            % (TestUorbP.topicList3[0], TestUorbP.topicList3[1]),
            "Commands:",
        )
        assert ret == 0

    # test a+g sensor
    def test_uorb_listener_ag(self):
        expect = ["Total number of received Message:20/20"]
        for topic in TestUorbP.topicList1:
            ret = pytest.product.sendCommand(
                "uorb_listener -n 20 -r 50 %s" % topic, expect
            )
            assert ret == 0

    # test geure sensor
    def test_uorb_listener_gesture(self):
        expect = ["Total number of received Message:0/0"]
        for topic in TestUorbP.topicList2:
            ret = pytest.product.sendCommand(
                "uorb_listener -t 20 %s" % topic, expect, timeout=60
            )
        assert ret == 0

    # test ppg sensor
    def test_uorb_listener_ppg(self):
        expect = ["Total number of received Message:25/25"]
        for topic in TestUorbP.topicList3:
            ret = pytest.product.sendCommand(
                "uorb_listener -n 25 -r 50 %s" % topic, expect
            )
            assert ret == 0

    # test light sensor
    def test_uorb_listener_light(self):
        expect = ["Total number of received Message:30/30"]
        freq = 25
        for topic in TestUorbP.topicList4:
            ret = pytest.product.sendCommand(
                f"uorb_listener -n 30 -r {freq} {topic}", expect, timeout=20
            )
            assert ret == 0

    # test batch
    def test_uorb_listener_batch1(self):
        expect = ["Total number of received Message:40/40"]
        for topic in TestUorbP.topicList3:
            ret = pytest.product.sendCommand(
                "uorb_listener -b 100000 -n 40 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 120000 -n 40 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 400000 -n 40 %s" % topic, expect
            )
            assert ret == 0

    def test_uorb_listener_batch2(self):
        expect = ["Total number of received Message:50/50"]
        for topic in TestUorbP.topicList3:
            ret = pytest.product.sendCommand(
                "uorb_listener -b 400000 -r 25 -n 50 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 40000 -r 25 -n 50 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 8000 -r 200 -n 50 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 100000 -r 50 -n 50 %s" % topic, expect
            )
            assert ret == 0
            ret = pytest.product.sendCommand(
                "uorb_listener -b 120000 -r 100 -n 50 %s" % topic, expect
            )
            assert ret == 0

    # def assertRet(logFile, pattern, str_temp, str2, rateANDinterance=1, TestUorbP.topicList=['sensor_accel']):
    #     ret_getTimeStamp = 1
    #     for topic in TestUorbP.topicList:
    #         str1 = str_temp % topic
    #         ret = pytest.product.sendCommand(str1, '%s:%s, number:10' % (str2, topic), 60)
    #         if ret == 0:
    #             t = getTimestamp(logFile, str1, str2, pattern)
    #             d = getDif(t, rateANDinterance)
    #             for j in range(len(d)):
    #                 if d[j] > 0.1:
    #                     logging.info('fail' + '->' + ' (next-now)-r/i = ' + str(d[j]))
    #                     break
    #                 ret_getTimeStamp = 0
    #             p.equal('test%s—— ' % (i) + str1, ret_getTimeStamp, 0)
