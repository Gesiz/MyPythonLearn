# coding="utf-8"

# redis 基本命令 String
# set(name,value,ex=None,nx=False,xx=False)

# 在Redis 中设置值 默认 不存在则创建 存在则修改

# ex 过期时间 秒
# px 过期事件 毫秒
# nx 如果为True 则只有name 不存在时 当前set操作才执行
# xx 如果为True 则只有name 存在时 当前set操作才执行

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# r.set('food', 'mutton', ex=3)  # ex 设置过期事件 三秒
# r.set('food', 'mutton', px=3)  # ex 设置过期事件 三毫秒
# print(r.set('food', 'mutton', nx=True)) # 存在返回值 如果返回值 为True 则不存在 正常添加
# print(r.set('food', 'mutton_reload', px=True))  # 存在返回值 如果返回值 为True 则存在该键 正常添加
# print(r.get('food'))

# setnx setex psetex 具体功能同上


import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# r.mset({'k1': 'v1', 'k2': 'v2'}) # 需要传输字典
# print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
# print(r.mget("k1"))

# print(r.mget('k1', 'k2'))
# print(r.mget(['k1', 'k2']))
# print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))  # 将目前redis缓存中的键对应的值批量取出来
# [None, None, None, 'v1', 'v2'] 不存在的数据 将会返回 None
# print(r.getset("food", "barbecue"))  # key value 设置的新值是barbecue 设置前的值是beef


# getrange(key,start,end)
# 获取子序列 (根据字节 获取 非字符)
# key - Redis 的 key
# start 起止位置 字节
# end 结束位置 字节
# 3 字节 = 1 汉字
# 1 字节 = 1 英文

# r.set("cn_name", "军惜大大")  # 汉字
# print(r.getrange("cn_name", 0, 2))  # 0 1 2 取得三位直接
# r.set("en_name","junxi") # 字母
# print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
# print(r.getrange("en_name", 0, -1)) # 取所有的字节 junxi 切片操作
# setrange(name,offset,value)
# 修改字符串内容 从指定字符串索引开始 向后替换
# r.setrange("en_name", 1, "ccc")
# print(r.get("en_name"))

# incr(self,name,amount=1)
# 自增name 对应的值 当name 不存在时 则创建 amount 否则 则自增

# r.set("foo",123)
# print(r.mget("foo", "foo1", "foo2", "k1", "k2"))
# r.incr("foo", amount=2)
# print(r.mget("foo", "foo1", "foo2", "k1", "k2"))

# decr(eslf,name,amount=1)

# 自减
# r.decr("foo4", amount=3) # 递减3
# r.decr("foo1", amount=1) # 递减1
# print(r.mget("foo1", "foo4"))

# #应用场景 – 页面点击数
# 假定我们对一系列页面需要记录点击次数。例如论坛的每个帖子都要记录点击次数，而点击次数比回帖的次数的多得多
# 如果使用关系数据库来存储点击，可能存在大量的行级锁争用。所以，点击数的增加使用redis的INCR命令最好不过了。
# 当redis服务器启动时，可以从关系数据库读入点击数的初始值（12306这个页面被访问了34634次）

# 追加 字符串 append(key,value)
r.append("name", "haha")    # 在name对应的值junxi后面追加字符串haha
print(r.mget("name"))