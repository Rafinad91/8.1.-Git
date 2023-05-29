# Домашнее задание к занятию 12.01 Базы данных - `Христинин Артем Олегович`

## Задание 1
 
 - CREATE USER 'sys_temp' IDENTIFIED WITH mysql_native_password BY '****';
 - Select user, host from mysql.user;
 - GRANT ALL PRIVILEGES ON *.* TO 'sys_temp';
 - show grants for sys_temp;
 - mysql -u sys_temp -p
 - mysql -u sys_temp -p sakila < /tmp/sakila-db/sakila-schema.sql
 - mysql -u sys_temp -p sakila < /tmp/sakila-db/sakila-data.sql 
 - show databases; use sakila; show tables;

 ![alt text]()

 ![alt text]()

 ![alt text]()

 ## Задание 2

 - show databases;
 - use sakila;
 - show tables;

![alt text]()

