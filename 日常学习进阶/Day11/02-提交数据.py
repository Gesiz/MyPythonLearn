import pymysql

# 创建连接对象
conn = pymysql.connect(host='192.168.158.133', user='root', password='mysql', database='jing_dong', charset='utf8')
# 创建游标
cur = conn.cursor()

# 执行sql
sql = "update goods set price=99 where id=1"
cur.execute(sql)
conn.commit()
sql = "select * from goods;"
cur.execute(sql)

# 获取数据 # 元组类型的
data = cur.fetchall()
for i in data:
    print(i)  # 元组类型的 元组中的每一个元素都是一个数据库的总的数据
# 5 关闭
cur.close()
conn.close()
