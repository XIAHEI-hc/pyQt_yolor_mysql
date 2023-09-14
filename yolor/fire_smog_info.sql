/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80028
Source Host           : localhost:3306
Source Database       : fire_smog_info

Target Server Type    : MYSQL
Target Server Version : 80028
File Encoding         : 65001

Date: 2022-04-28 13:04:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for info_record
-- ----------------------------
DROP TABLE IF EXISTS `info_record`;
CREATE TABLE `info_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location` varchar(20) DEFAULT NULL,
  `cam_id` varchar(20) DEFAULT NULL,
  `loc_pos` varchar(20) DEFAULT NULL,
  `logs` varchar(50) DEFAULT NULL,
  `log_date` date DEFAULT NULL,
  `log_time` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of info_record
-- ----------------------------
INSERT INTO `info_record` VALUES ('1', '地区B', 'cam_2', '天河小区2号', '无火灾有烟雾,请快速核查', '2022-03-02', '08:30:00');
INSERT INTO `info_record` VALUES ('2', '地区A', 'cam_2', '花园小区2号', '无火灾无烟雾,正常', '2022-03-05', '08:00:00');
INSERT INTO `info_record` VALUES ('3', '地区C', 'cam_1', '滨海小区1号', '无火灾无烟雾,正常', '2022-03-01', '08:00:00');
INSERT INTO `info_record` VALUES ('4', '地区A', 'cam_2', '花园小区2号', '无火灾有烟雾,请快速核查', '2022-03-05', '08:10:00');
INSERT INTO `info_record` VALUES ('5', '地区B', 'cam_1', '天河小区1号', '无火灾无烟雾,正常', '2022-03-05', '10:30:00');
INSERT INTO `info_record` VALUES ('6', '地区A', 'cam_1', '花园小区1号', '无火灾无烟雾,正常', '2022-03-05', '10:30:52');
INSERT INTO `info_record` VALUES ('7', '地区A', 'cam_2', '花园小区2号', '有火灾有烟雾,请快速联系消防员', '2022-03-05', '08:15:00');
INSERT INTO `info_record` VALUES ('8', '地区B', 'cam_1', '天河小区1号', '无火灾无烟雾,正常', '2022-03-05', '10:40:00');
INSERT INTO `info_record` VALUES ('9', '地区C', 'cam_2', '滨海小区2号', '无火灾无烟雾,正常', '2022-03-01', '08:10:00');
INSERT INTO `info_record` VALUES ('10', '地区C', 'cam_1', '滨海小区1号', '无火灾无烟雾,正常', '2022-03-01', '08:20:00');
INSERT INTO `info_record` VALUES ('11', '地区A', 'cam_2', '花园小区2号', '无火灾有烟雾,请快速核查', '2022-03-05', '10:30:00');
INSERT INTO `info_record` VALUES ('12', '地区B', 'cam_2', '天河小区2号', '无火灾无烟雾,正常', '2022-03-05', '10:50:06');
INSERT INTO `info_record` VALUES ('13', '地区A', 'cam_1', '花园小区1号', '无火灾无烟雾,正常', '2022-03-05', '08:00:52');
INSERT INTO `info_record` VALUES ('14', '地区A', 'cam_1', '花园小区1号', '无火灾无烟雾,正常', '2022-03-05', '08:10:52');
INSERT INTO `info_record` VALUES ('15', '地区B', 'cam_2', '天河小区2号', '无火灾有烟雾,请快速核查', '2022-03-05', '11:00:00');
INSERT INTO `info_record` VALUES ('16', '地区A', 'cam_2', '花园小区2号', '无火灾无烟雾,正常', '2022-03-05', '08:40:06');
INSERT INTO `info_record` VALUES ('17', '地区B', 'cam_1', '天河小区1号', '有火灾有烟雾,请快速联系消防员', '2022-03-05', '11:05:52');
INSERT INTO `info_record` VALUES ('18', '地区A', 'cam_3', '花园小区3号', '无火灾无烟雾,正常', '2022-03-02', '10:26:52');
INSERT INTO `info_record` VALUES ('19', '地区C', 'cam_1', '滨海小区1号', '无火灾有烟雾,请快速核查', '2022-03-01', '08:28:52');
INSERT INTO `info_record` VALUES ('20', '地区A', 'cam_2', '滨海小区2号', '无火灾无烟雾,正常', '2022-03-01', '10:30:52');
INSERT INTO `info_record` VALUES ('21', '地区C', 'cam_1', '滨海小区1号', '无火灾有烟雾,请快速核查', '2022-03-01', '10:30:52');
INSERT INTO `info_record` VALUES ('22', '地区B', 'cam_2', '天河小区2号', '无火灾无烟雾,正常', '2022-03-06', '07:30:00');
