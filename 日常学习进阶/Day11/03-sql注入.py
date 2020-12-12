import pymysql

# 创建连接对象
conn = pymysql.connect(host='192.168.158.133', user='root', password='mysql', database='jing_dong', charset='utf8')
# 创建游标
cur = conn.cursor()


# 执行sql
name = input("请输入要查询的物品名称")
# 获取数据
sql = f'select * from goods where name = "{name}";'
# sql = " select * from goods where name = '%s' "% name
print(sql)
# cur.execute(sql,[name])# 防sql注入
cur.execute(sql,[name])

# 获取数据 # 元组类型的
data = cur.fetchall()
print(data)
# for i in data:
#     print(i)  # 元组类型的 元组中的每一个元素都是一个数据库的总的数据
# 5 关闭
cur.close()
conn.close()
