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

import time

import pytest

pytestmark = pytest.mark.dep_config("CONFIG_LIBUV_UTILS_TEST")
pytestmark = pytest.mark.cmd_check("uv_run_tests_main")


class TestLibuvSystem:
    def test_close_order(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests close_order", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_run_once(self):
        ret = pytest.product.sendCommand("uv_run_tests run_once", "ok 1 -", timeout=30)
        assert ret == 0

    def test_run_nowait(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests run_nowait", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_alive(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_alive", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_close", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_instant_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_instant_close", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_stop(self):
        ret = pytest.product.sendCommand("uv_run_tests loop_stop", "ok 1 -", timeout=30)
        assert ret == 0

    def test_loop_update_time(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_update_time", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_backend_timeout(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_backend_timeout", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_configure(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_configure", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_default_loop_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests default_loop_close", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_barrier_1(self):
        ret = pytest.product.sendCommand("uv_run_tests barrier_1", "ok 1 -", timeout=30)
        assert ret == 0

    def test_barrier_2(self):
        ret = pytest.product.sendCommand("uv_run_tests barrier_2", "ok 1 -", timeout=30)
        assert ret == 0

    def test_barrier_3(self):
        ret = pytest.product.sendCommand("uv_run_tests barrier_3", "ok 1 -", timeout=30)
        assert ret == 0

    def test_barrier_serial_thread(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests barrier_serial_thread", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_barrier_serial_thread_single(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests barrier_serial_thread_single",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_condvar_1(self):
        ret = pytest.product.sendCommand("uv_run_tests condvar_1", "ok 1 -", timeout=30)
        assert ret == 0

    def test_condvar_2(self):
        ret = pytest.product.sendCommand("uv_run_tests condvar_2", "ok 1 -", timeout=30)
        assert ret == 0

    def test_condvar_3(self):
        ret = pytest.product.sendCommand("uv_run_tests condvar_3", "ok 1 -", timeout=30)
        assert ret == 0

    def test_condvar_4(self):
        ret = pytest.product.sendCommand("uv_run_tests condvar_4", "ok 1 -", timeout=30)
        assert ret == 0

    def test_condvar_5(self):
        ret = pytest.product.sendCommand("uv_run_tests condvar_5", "ok 1 -", timeout=30)
        assert ret == 0

    def test_semaphore_1(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests semaphore_1", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_semaphore_2(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests semaphore_2", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_semaphore_3(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests semaphore_3", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_tty(self):
        ret = pytest.product.sendCommand("uv_run_tests tty", "ok 1 -", timeout=30)
        assert ret == 0

    def test_tty_file(self):
        ret = pytest.product.sendCommand("uv_run_tests tty_file", "ok 1 -", timeout=30)
        assert ret == 0

    def test_tty_pty(self):
        ret = pytest.product.sendCommand("uv_run_tests tty_pty", "ok 1 -", timeout=30)
        assert ret == 0

    def test_pipe_bind_error_inval(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_bind_error_inval", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_pipe_connect_close_multiple(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_connect_close_multiple",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_pipe_bind_or_listen_error_after_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_bind_or_listen_error_after_close",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_pipe_overlong_path(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_overlong_path", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_pipe_connect_bad_name(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_connect_bad_name", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_pipe_connect_on_prepare(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_connect_on_prepare", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_pipe_getsockname_abstract(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_getsockname_abstract",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_pipe_getsockname_blocking(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_getsockname_blocking",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_pipe_pending_instances(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests pipe_pending_instances", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_sys_error(self):
        ret = pytest.product.sendCommand("uv_run_tests sys_error", "ok 1 -", timeout=30)
        assert ret == 0

    def test_timer(self):
        ret = pytest.product.sendCommand("uv_run_tests timer", "ok 1 -", timeout=30)
        assert ret == 0

    def test_timer_init(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_init", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_again(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_again", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_start_twice(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_start_twice", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_order(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_order", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_huge_timeout(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_huge_timeout", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_huge_repeat(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_huge_repeat", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_run_once(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_run_once", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_from_check(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_from_check", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_is_closing(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_is_closing", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_null_callback(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_null_callback", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_early_check(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_early_check", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_no_double_call_once(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_no_double_call_once",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_timer_no_run_on_unref(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_no_run_on_unref", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_idle_starvation(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests idle_starvation", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_loop_handles(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests loop_handles", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_get_loadavg(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests get_loadavg", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_walk_handles(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests walk_handles", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_idle_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests idle_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_async_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests async_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_prepare_ref(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests prepare_ref", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_check_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests check_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_unref_in_prepare_cb(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests unref_in_prepare_cb", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_timer_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests timer_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_timer_ref2(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests timer_ref2", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_event_ref(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_ref", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_pipe_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests pipe_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_pipe_ref2(self):
        ret = pytest.product.sendCommand("uv_run_tests pipe_ref2", "ok 1 -", timeout=30)
        assert ret == 0

    def test_process_ref(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests process_ref", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_has_ref(self):
        ret = pytest.product.sendCommand("uv_run_tests has_ref", "ok 1 -", timeout=30)
        assert ret == 0

    def test_active(self):
        ret = pytest.product.sendCommand("uv_run_tests active", "ok 1 -", timeout=30)
        assert ret == 0

    def test_process_title_big_argv(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests process_title_big_argv", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_cwd_and_chdir(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests cwd_and_chdir", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_get_passwd(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests get_passwd", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_get_passwd2(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests get_passwd2", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_get_group(self):
        ret = pytest.product.sendCommand("uv_run_tests get_group", "ok 1 -", timeout=30)
        assert ret == 0

    def test_homedir(self):
        ret = pytest.product.sendCommand("uv_run_tests homedir", "ok 1 -", timeout=30)
        assert ret == 0

    def test_tmpdir(self):
        ret = pytest.product.sendCommand("uv_run_tests tmpdir", "ok 1 -", timeout=30)
        assert ret == 0

    def test_hrtime(self):
        ret = pytest.product.sendCommand("uv_run_tests hrtime", "ok 1 -", timeout=30)
        assert ret == 0

    def test_clock_gettime(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests clock_gettime", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_gettimeofday(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests gettimeofday", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_test_macros(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests test_macros", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_spawn_fails(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests spawn_fails", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_spawn_quoted_path(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests spawn_quoted_path", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_poll_getpath(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_poll_getpath", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_poll_close_request(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_poll_close_request", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_kill_invalid_signum(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests kill_invalid_signum", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_file_noent(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_file_noent", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_fstat_stdio(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_fstat_stdio", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_realpath(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_realpath", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_stat_missing_path(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_stat_missing_path", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_event_watch_dir_recursive(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_watch_dir_recursive",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_event_immediate_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_immediate_close",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_event_start_and_close(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_start_and_close",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_event_error_reporting(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_error_reporting",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_event_getpath(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_event_getpath", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_scandir_empty_dir(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_scandir_empty_dir", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_scandir_non_existent_dir(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_scandir_non_existent_dir",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_readdir_empty_dir(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_readdir_empty_dir", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_readdir_non_existing_dir(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_readdir_non_existing_dir",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0

    def test_fs_partial_read(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_partial_read", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_null_req(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_null_req", "ok 1 -", timeout=30
        )
        assert ret == 0

    def test_fs_get_system_error(self):
        pytest.product.sendCommand("cd /", "")
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_get_system_error", "ok 1 -", timeout=30
        )
        pytest.product.sendCommand("cd -")
        assert ret == 0
        time.sleep(0.5)

    def test_strscpy(self):
        ret = pytest.product.sendCommand("uv_run_tests strscpy", "ok 1 -", timeout=30)
        assert ret == 0
        time.sleep(0.5)

    def test_strtok(self):
        ret = pytest.product.sendCommand("uv_run_tests strtok", "ok 1 -", timeout=30)
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_queue_work_simple(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_queue_work_simple",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_queue_work_einval(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_queue_work_einval",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_getaddrinfo(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_getaddrinfo",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_getnameinfo(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_getnameinfo",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_random(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_random",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_work(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_work", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_fs(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_fs", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_threadpool_cancel_single(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests threadpool_cancel_single",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_local_storage(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_local_storage", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_stack_size(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_stack_size", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_stack_size_explicit(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_stack_size_explicit",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_mutex(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_mutex", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_mutex_recursive(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_mutex_recursive", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_rwlock(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_rwlock", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_rwlock_trylock(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_rwlock_trylock", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_create(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_create", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_equal(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_equal", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_thread_affinity(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests thread_affinity", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_close_fd(self):
        ret = pytest.product.sendCommand("uv_run_tests close_fd", "ok 1 -", timeout=30)
        assert ret == 0
        time.sleep(0.5)

    def test_we_get_signal(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests we_get_signal", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_we_get_signals(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests we_get_signals", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_we_get_signal_one_shot(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests we_get_signal_one_shot", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_we_get_signals_mixed(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests we_get_signals_mixed", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_signal_close_loop_alive(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests signal_close_loop_alive", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_queue_foreach_delete(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests queue_foreach_delete", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_random_async(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests random_async", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_random_sync(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests random_sync", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_handle_type_name(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests handle_type_name", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_req_type_name(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests req_type_name", "ok 1 -", timeout=30
        )
        assert ret == 0
        time.sleep(0.5)

    def test_fs_read(self):
        ret = pytest.product.sendCommand(
            "uv_run_tests fs_read_write_null_arguments",
            "ok 1 -",
            timeout=30,
        )
        assert ret == 0
        time.sleep(0.5)
