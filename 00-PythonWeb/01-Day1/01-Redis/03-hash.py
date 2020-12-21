# redis 基本命令 hash
# 1 单个增加 -- 修改 (单个去除) 没有就新增 有的话就修改
# hset(name,key,value)

# db name --
#           |key1-
#                 |value1
#                 |value2
#           |key2-
#                 |value1
#                 |value2
import redis
import time
pool = redis.ConnectionPool(host='lo')