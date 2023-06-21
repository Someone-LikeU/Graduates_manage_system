/*
 Navicat Premium Data Transfer

 Source Server         : MY数据库
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : graduatesdb

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 04/01/2021 11:20:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for graduatesjobchange
-- ----------------------------
DROP TABLE IF EXISTS `graduatesjobchange`;
CREATE TABLE `graduatesjobchange`  (
  `ChangeID` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Sname` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Sno` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `SpreComName` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ScurComName` char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `OutPreDate` date NOT NULL,
  `newJobDate` date NOT NULL,
  `isBreak` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ChangeID`) USING BTREE,
  INDEX `Sname`(`Sname`) USING BTREE,
  INDEX `Sno`(`Sno`) USING BTREE,
  INDEX `SpreComName`(`SpreComName`) USING BTREE,
  INDEX `ScurComName`(`ScurComName`) USING BTREE,
  CONSTRAINT `graduatesjobchange_ibfk_1` FOREIGN KEY (`Sname`) REFERENCES `graduates` (`Sname`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `graduatesjobchange_ibfk_2` FOREIGN KEY (`Sno`) REFERENCES `graduates` (`Sno`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `graduatesjobchange_ibfk_3` FOREIGN KEY (`SpreComName`) REFERENCES `company` (`Cname`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `graduatesjobchange_ibfk_4` FOREIGN KEY (`ScurComName`) REFERENCES `company` (`Cname`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of graduatesjobchange
-- ----------------------------
INSERT INTO `graduatesjobchange` VALUES ('0', '蒋几娜', '201700099', '钱磊人力资源管理咨询有限公司', '魏酒艳科技实业有限公司', '2021-01-01', '2021-01-03', 'n');
INSERT INTO `graduatesjobchange` VALUES ('1', '李个', '201700098', '姜个伟地质灾害防治有限公司', '许磊几财税咨询服务有限公司', '2020-12-31', '2021-01-03', 'n');
INSERT INTO `graduatesjobchange` VALUES ('2', '钱叕', '201700095', '武静实业有限责任公司', '潘人广告传媒有限公司', '2020-12-30', '2021-01-03', 'n');
INSERT INTO `graduatesjobchange` VALUES ('3', '韩第艳', '201700092', '郎磊德商贸有限公司', '秦构门窗有限公司', '2020-12-29', '2021-01-02', 'n');
INSERT INTO `graduatesjobchange` VALUES ('4', '杨水伟', '201700093', '魏酒艳科技实业有限公司', '郎吉吉新技术开发有限公司', '2020-12-24', '2021-01-01', 'n');
INSERT INTO `graduatesjobchange` VALUES ('5', '陶秀', '201700082', '郎吉吉新技术开发有限公司', '钱磊人力资源管理咨询有限公司', '2020-12-29', '2021-01-02', 'n');
INSERT INTO `graduatesjobchange` VALUES ('6', '孔第秀', '201700085', '曹构文化传媒有限责任公司', '陈机个科技有限公司', '2020-12-30', '2020-12-31', 'n');

SET FOREIGN_KEY_CHECKS = 1;
