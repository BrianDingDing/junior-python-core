DROP DATABASE IF EXISTS junior_python_core;
CREATE DATABASE IF NOT EXISTS junior_python_core CHARACTER SET utf8;

USE junior_python_core;
GO

DROP TABLE IF EXISTS pymysql_demo01;
CREATE TABLE IF NOT EXISTS pymysql_demo01(
    id int,
    name char(10)
);

ALTER TABLE pymysql_demo01 add image mediumblob;