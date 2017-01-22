CREATE TABLE IF NOT EXISTS `iask_answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `text` text NOT NULL COMMENT '回答内容',
  `question_id` int(18) NOT NULL COMMENT '问题ID',
  `answerer` varchar(255) NOT NULL COMMENT '回答者',
  `date` varchar(255) NOT NULL COMMENT '回答时间',
  `is_good` int(11) NOT NULL COMMENT '是否是最佳答案',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
 
CREATE TABLE IF NOT EXISTS `iask_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '问题ID',
  `text` text NOT NULL COMMENT '问题内容',
  `questioner` varchar(255) NOT NULL COMMENT '提问者',
  `date` date NOT NULL COMMENT '提问时间',
  `ans_num` int(11) NOT NULL COMMENT '回答数量',
  `url` varchar(255) NOT NULL COMMENT '问题链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;