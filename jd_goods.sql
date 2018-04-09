
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jd_goods
-- ----------------------------
DROP TABLE IF EXISTS `jd_goods`;
CREATE TABLE `jd_goods` (
  `ID` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `frontResol` varchar(255) DEFAULT NULL,
  `backResol` varchar(255) DEFAULT NULL,
  `rom` varchar(255) DEFAULT NULL,
  `battery` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

