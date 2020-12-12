####  数据库: 本质上就是一种特殊的文件

​	数据库指的实际上是一个很多功能的整体:

​	1 数据库是由数据表组成的

​	2 数据表是用来存储数据的

​	3 存储一类相同信息的一列: 字段

​	4 存储莫个人或者事务的详细描述信息的一行: 记录

​	5 能够标识唯一一行记录的字段:主键(不能为空 不能重复)

​	6 表和表之间具有一定的关联的数据库:关系型数据库

​	7 所有的客户端服务端数据库文件共同组成了一个关系性数据库系统: RDBMS

#### 数据库相关操作:

​	1 查看所有的数据库: show databases;

​	2 创建数据库: create database 数据库名字 charset="utf8";

​	3 删除数据库: drop database xxx;

​	4 查看字符集: show create database xxx;

​	5 使用数据库: use xxx;

#### 数据表相关操作:

​	1 查看所有的数据表: show tables;

​	2 创建数据表: create table xxx(字段名 数据类型 约束);

​	3 删除数据表: drop table xxx;

​	4 查看字符集: show create table xxx;

​	5 查看数据表结构: desc xxx;

#### 	数据表字段的相关操作

​	1 增加: alter table xxx add 字段名 数据类型 约束;

​	2 修改: alter table xxx change 老的字段名 新的字段名 数据类型 约束;

​	3 删除: alter table xxx drop 字段名;

#### 数据的操作

#### 	增加数据

​	1 单行插入: insert into 表 values(值);

​	2 部分插入: insert into 表(要插入的字段名)  values (字段的值); 

​		注意:如果字段not null 必须插入数据 

​	3 多行插入: insert into 表 values(值),(值);

#### 	修改数据

​	1 update xxx set 字段 where;

#### 	删除数据

​	1 delete from where 条件;

​	2 逻辑删除: is_delete字段表示(1就是删除了 0 就是没删除)

#### 	查询数据

​	1 查询所有数据 : select * from xxx;

​	2 别名: select name as yyy from xxx;

#### 	比较运算符

​	1 判断相等 =

​	2 判断不等于 <>

#### 	逻辑运算符

​	1 and or 

​	2 not 取反的时候需要把条件用 () 

#### 	模糊查询

​	1 select * from xxx where name like "_%";

​	2 _ 代表一个字符

​	3 %代表任意多个字符

#### 	范围查询	

​	1 非连续性的范围查询: select * from xxx where age in (18,19,30);

​	2 连续性的范围查询: select * from xxx where age between 18 and 34;

​	3 连续性的范围查询: select * from xxx where age not between 18 and 34;

#### 	排序查询

​	1 select * from xxx where age > 18 order by age;

​	2 升序asc 从小到大(默认的)

​	3 降序desc 从大到小

​	4 数据相同的时候按照其他字段排序:

​		select * from xxx where age > 18 order by age,height desc;