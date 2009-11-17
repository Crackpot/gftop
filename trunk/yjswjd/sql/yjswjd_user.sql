#用户表
DROP TABLE yjswjd_user;
CREATE TABLE IF NOT EXISTS yjswjd_user (
    user_id INT AUTO_INCREMENT COMMENT '用户ID',
    name VARCHAR(32) NOT NULL COMMENT '姓名',
    password VARCHAR(32) NOT NULL COMMENT '密码',
    gender VARCHAR(1) NOT NULL COMMENT '性别',
    mobile VARCHAR(11) NOT NULL COMMENT '手机号码',
    email VARCHAR(30) NOT NULL COMMENT 'email',
    identification_number VARCHAR(18) NOT NULL COMMENT '身份证号码',
    join_date DATETIME NOT NULL COMMENT '注册日期',
    birthdate DATE NOT NULL COMMENT '生日',
    address VARCHAR(100) COMMENT '地址',
    state VARCHAR(10) COMMENT '国籍',
    PRIMARY KEY (user_id)
);
