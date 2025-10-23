CREATE TABLE `vela_perf_data_system_osperf` (
  `id` BIGINT(11) NOT NULL AUTO_INCREMENT COMMENT '主键id' PRIMARY KEY,
  `board` varchar(64) DEFAULT '' NOT NULL COMMENT '产品',
  `core` varchar(8) DEFAULT '' NOT NULL COMMENT '核',
  `branch` varchar(32) DEFAULT '' NOT NULL DEFAULT '' COMMENT '测试代码分支',
  `name` varchar(48) DEFAULT '' NOT NULL COMMENT '性能指标名称',
  `engine` varchar(32) DEFAULT '' NOT NULL COMMENT '引擎',
  `size` varchar(16) DEFAULT '' NOT NULL COMMENT '大小',
  `avg` int default 0 NOT NULL comment '平均值',
  `min` int default 0 NOT NULL comment '最小值',
  `max` int default 0 NOT NULL comment '最大值',
  `describe` varchar(24) DEFAULT '' NOT NULL COMMENT '描述',
  `data_sync_task_id` BIGINT(11) DEFAULT 0 NOT NULL COMMENT '数据同步任务id',
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间'
);