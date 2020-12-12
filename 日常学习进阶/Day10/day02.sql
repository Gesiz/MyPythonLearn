-- 聚合函数
	-- 总数
	-- count
	-- 查询男性有多少人，女性有多少人
	select count(*) from students where gender=1;
	select count(*) from students where gender=2;

	-- 最大值
	-- max
	-- 查询最大的年龄
	select max(age) from students;
	

	-- 查询女性的最高 身高
	select max(height) from students where gender=2;

	-- 最小值
	-- min
	select min(height) from students where gender=2;
	
	-- 求和
	-- sum
	-- 计算所有人的年龄总和
	-- sum(age)里面是字段 求得就是字段的数据总和
	select sum(age) from students;
	
	-- sum(age<15)里面是表达式 求得就是满足条件的数据的总个数
	select sum(age<15) from students;
	
	-- 平均值
	-- avg
	-- 计算平均年龄
	select avg(age) from students;

	-- 计算平均年龄 sum(age)/count(*)
	select sum(age)/count(*) from students;

	-- 四舍五入 round(123.23 , 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
	select round(avg(age),2) from students;

	-- 计算男性的平均身高 保留2位小数
	select round(avg(height),2) from students where gender=1;
	

-- 分组(重点)

	-- group by
	-- 按照性别分组,查询所有的性别
	-- 按照字段分组 就可以直接查询什么字段
	select gender from students group by gender;
	
	
	select name,gender from students group by gender;错误
	-- select name,gender from students group by gender;
	-- 失败select * from students group by gender;

	-- 计算每种性别中的人数
	select gender,count(*) from students group by gender;
	
	
	-- group_concat(...)
	-- 查询同种性别中的姓名
	select gender,group_concat(name) from students group by gender;
	
	-- 查询每组性别的平均年龄
	select gender,avg(age) from students group by gender;
	
	
	-- 查询平均年龄超过30岁的性别，以及姓名 having avg(age) > 30(重点)
	-- having是对每个组中的数据进行筛选和group by联合使用
	-- where是对所有的数据进行筛选
	select gender,group_concat(name) from students group by gender having avg(age)>30;
	
	-- 查询每种性别的平均年龄和名字
	select gender,avg(age),group_concat(name) from students group by gender;
	
	-- 查询每种性别中的人数多于2个的性别和姓名（重点）
	select gender,group_concat(name) from students group by gender having count(*)>2;
	

	-- with rollup 汇总的作用(了解)
	select gender,count(*) from students group by gender with rollup;

-- 分页
	-- limit start, count
	start:(页数-1)*每一页数量
	-- 限制查询出来的数据个数
	-- 查询前5个数据
	select * from students limit 5;
	
	-- 每页显示2个，第1个页面
	select * from students limit 0,2;

	-- 每页显示2个，第2个页面
	select * from students limit 2,2;

	-- 每页显示2个，第3个页面
	select * from students limit 4,2;

	-- 每页显示2个，第4个页面
	select * from students limit 6,2;

	-- 每页显示2个，显示第6页的信息,按照年龄从小到大排序
	select * from students order by age asc limit 10,2;
	
	
	
	错误1 select * from students limit 10,2 order by age asc;
	
	-- 错误的写法
	错误2 select * from students limit 2*(6-1),2;
	
	-- limit 放在最后面(注意)
	 


-- 连接查询(重点)
	-- inner join ... on
	-- select ... from 表A inner join 表B;
	select * from students inner join classes;
	
	-- 查询 有能够对应班级的学生以及班级信息
	select * from students inner join classes on students.cls_id=classes.id;
	

	-- 按照要求显示姓名、班级
	select students.name,classes.name from students inner join classes on students.cls_id=classes.id;

	-- 给数据表起名字
	select s.name,c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询 有能够对应班级的学生以及班级信息，显示学生的所有信息 students.*，只显示班级名称 classes.name.
	select students.*,classes.name from students inner join classes on students.cls_id=classes.id;
		
	-- 在以上的查询中，将班级姓名显示在第1列
	select classes.name,students.* from students inner join classes on students.cls_id=classes.id;
	

	-- 查询 有能够对应班级的学生以及班级信息, 按照班级进行排序
	-- select c.xxx s.xxx from students as s inner join clssses as c on .... order by ....;
	select classes.name,students.* from students inner join classes on students.cls_id=classes.id order by classes.name;
	
	-- 当时同一个班级的时候，按照学生的id进行从小到大排序
	select classes.name,students.* from students inner join classes on students.cls_id=classes.id order by classes.name,students.id;
	
	
	

	-- left join
	-- 查询每位学生对应的班级信息
	select * from students inner join classes on students.cls_id=classes.id;
	select * from students left join classes on students.cls_id=classes.id;
	
	-- select * from students right join classes on students.cls_id = classes.id;

	-- 查询没有对应班级信息的学生
	-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having .....
	select * from students left join classes on students.cls_id=classes.id where classes.name is null;
	
	(注意)不建议使用 select * from students left join classes on students.cls_id=classes.id having classes.id is null;
	
	-- right join   on
	-- 将数据表名字互换位置，用left join完成


	

-- 子查询
	-- 标量子查询: 子查询返回的结果是一个数据(一行一列)
	-- 列子查询: 返回的结果是一列(一列多行)
	-- 行子查询: 返回的结果是一行(一行多列)
	
	-- 查询出高于平均身高的信息(height)
	-- 1 查出平均身高
	select avg(height) from students;
	-- 2 查出高于平均身高的信息
	select * from students where height>(select avg(height) from students);
	
	
	-- 查询学生的班级号能够对应的 学生名字
	-- select name from students where cls_id in (select id from classes);
	-- 1 查出所有的班级id
	select id from classes;
	(1,2,3)
	-- 2 查出能够对应上班级号的学生信息
	select * from students where cls_id in (select id from classes);
	
	
	
select c.*
from 
areas as c 
inner join 
areas as p on 
c.pid = p.id 
where p.title = '北京市';








