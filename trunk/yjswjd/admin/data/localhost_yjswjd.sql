-- phpMyAdmin SQL Dump
-- version 3.2.0
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2009 年 11 月 24 日 03:18
-- 服务器版本: 5.1.36
-- PHP 版本: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `yj`
--

-- --------------------------------------------------------

--
-- 表的结构 `yj_administrator`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_administrator`;
CREATE TABLE IF NOT EXISTS `yj_administrator` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `user_name` varchar(8) CHARACTER SET utf8 NOT NULL COMMENT '管理员名称',
  `name` varchar(8) COLLATE utf8_unicode_ci NOT NULL COMMENT '用户姓名',
  `password` varchar(20) COLLATE utf8_unicode_ci NOT NULL COMMENT '密码',
  `email` varchar(30) COLLATE utf8_unicode_ci NOT NULL COMMENT 'email',
  `group_id` int(11) NOT NULL COMMENT '管理员所属组',
  `storefront` int(1) NOT NULL COMMENT '所属店面',
  `activated` tinyint(1) NOT NULL COMMENT '是否激活',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `administrator_name` (`user_name`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='管理员表' AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `yj_administrator`
--

INSERT INTO `yj_administrator` (`user_id`, `user_name`, `name`, `password`, `email`, `group_id`, `storefront`, `activated`) VALUES
(1, 'crackpot', '高飞', 'hacker15263748', 'crackpot@localhost.site', 1, 0, 1);

-- --------------------------------------------------------

--
-- 表的结构 `yj_administrator_group`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_administrator_group`;
CREATE TABLE IF NOT EXISTS `yj_administrator_group` (
  `group_id` int(2) NOT NULL AUTO_INCREMENT COMMENT '管理员组',
  `group_name` varchar(8) NOT NULL COMMENT '管理员类型',
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `name` (`group_name`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='管理员表' AUTO_INCREMENT=13 ;

--
-- 转存表中的数据 `yj_administrator_group`
--

INSERT INTO `yj_administrator_group` (`group_id`, `group_name`) VALUES
(1, '系统操作员'),
(4, '酒店管理'),
(2, '前台接待收银'),
(3, '营销经理'),
(5, '日审'),
(6, '餐厅'),
(7, '领班'),
(8, '宾客关系'),
(9, '总经理'),
(10, '电脑房'),
(11, '外勤销售组'),
(12, '前厅管理');

-- --------------------------------------------------------

--
-- 表的结构 `yj_room`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_room`;
CREATE TABLE IF NOT EXISTS `yj_room` (
  `room_id` int(4) NOT NULL COMMENT '房间号码',
  `grade` int(1) NOT NULL COMMENT '房间等级',
  PRIMARY KEY (`room_id`),
  UNIQUE KEY `grade` (`grade`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `yj_room`
--


-- --------------------------------------------------------

--
-- 表的结构 `yj_room_grade`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_room_grade`;
CREATE TABLE IF NOT EXISTS `yj_room_grade` (
  `grade_id` int(2) NOT NULL AUTO_INCREMENT COMMENT '房间等级id',
  `grade` varchar(20) COLLATE utf8_unicode_ci NOT NULL COMMENT '房间等级名称',
  `price` int(11) NOT NULL COMMENT '房间价格',
  UNIQUE KEY `grade_id` (`grade_id`),
  UNIQUE KEY `grade` (`grade`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='房间等级' AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `yj_room_grade`
--

INSERT INTO `yj_room_grade` (`grade_id`, `grade`, `price`) VALUES
(1, '标准', 100),
(2, '三人间', 160);

-- --------------------------------------------------------

--
-- 表的结构 `yj_storefront`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_storefront`;
CREATE TABLE IF NOT EXISTS `yj_storefront` (
  `storefront_id` int(1) NOT NULL AUTO_INCREMENT COMMENT '店面id',
  `storefront_name` varchar(20) COLLATE utf8_unicode_ci NOT NULL COMMENT '店面名称',
  PRIMARY KEY (`storefront_id`),
  UNIQUE KEY `storefront_name` (`storefront_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='店面' AUTO_INCREMENT=1 ;

--
-- 转存表中的数据 `yj_storefront`
--


-- --------------------------------------------------------

--
-- 表的结构 `yj_user`
--
-- 创建时间: 2009 年 11 月 24 日 03:18
-- 最后更新: 2009 年 11 月 24 日 03:18
--

DROP TABLE IF EXISTS `yj_user`;
CREATE TABLE IF NOT EXISTS `yj_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `name` varchar(32) COLLATE utf8_unicode_ci NOT NULL COMMENT '姓名',
  `password` varchar(32) COLLATE utf8_unicode_ci NOT NULL COMMENT '密码',
  `gender` varchar(1) COLLATE utf8_unicode_ci NOT NULL COMMENT '性别',
  `mobile` varchar(11) COLLATE utf8_unicode_ci NOT NULL COMMENT '手机号码',
  `email` varchar(30) COLLATE utf8_unicode_ci NOT NULL COMMENT 'email',
  `identification_number` varchar(18) COLLATE utf8_unicode_ci NOT NULL COMMENT '身份证号码',
  `join_date` datetime NOT NULL COMMENT '注册日期',
  `birthdate` date NOT NULL COMMENT '生日',
  `address` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '地址',
  `state` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '国籍',
  `random_password` tinyint(1) NOT NULL COMMENT '随机密码否',
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `yj_user`
--

INSERT INTO `yj_user` (`user_id`, `name`, `password`, `gender`, `mobile`, `email`, `identification_number`, `join_date`, `birthdate`, `address`, `state`, `random_password`) VALUES
(1, '高飞', 'hacker15263748', '1', '15979122400', 'crackpot@localhost.site', '142401198707094512', '2009-11-21 03:50:50', '1987-07-09', NULL, NULL, 1),
(2, '张飞', 'kXW$i_h_7g', '2', '18979125096', 'gaofeitop@gmail.com', '111111111111111111', '2009-11-21 21:57:13', '1111-11-11', NULL, NULL, 0),
(3, '花俊昆', 'RVothf8x+p', '1', '13870871895', '989806059@qq.com', '362502198801220616', '2009-11-21 23:12:18', '1988-01-22', NULL, NULL, 0);
