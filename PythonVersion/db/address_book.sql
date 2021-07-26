# 清空数据
TRUNCATE TABLE IF EXISTS `sex`;
TRUNCATE TABLE IF EXISTS `address_book`;

# 删除表
DROP TABLE IF EXISTS `address_book`;
DROP TABLE IF EXISTS `sex`;

# 创建表 `sex`
CREATE TABLE IF NOT EXISTS `sex`(
	id INT PRIMARY KEY,
	gender CHAR(3)
);
# 创建表 `address_book`
CREATE TABLE IF NOT EXISTS `address_book`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(20) NOT NULL,
	`gender` INT DEFAULT "1",
	`age` INT DEFAULT -1,
	`phone` CHAR(11) DEFAULT "xxxxxxxxxxx",
	`address` VARCHAR(128) DEFAULT "地府",
	CONSTRAINT `address_book` FOREIGN KEY(`gender`) REFERENCES `sex`(`id`)
	
);


