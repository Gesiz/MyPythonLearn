# # # 1 导入
# from redis import Redis
# #
# # redis 提供两个类来实现官方大部分指令
# # redis 取出的默认结果是字节  我们可以设定
# # decode_responses=True 来修改为字符串
# #
# #
# # 2 通过创建 客户端来来连接 redis-server
# client = Redis(host='localhost', port=6379,
#                db=0, decode_responses=True)
#
# client.set(name='address', value='uk')
#
# print(client.get('address'))

# 连接池

# redis-py 使用 connection pool 来管理对一个 redis server的所有 连接
# 避免每次连接 建立 释放连接的 开销
# 默认 每个 Redis 实例都会维护一个 自己的连接池
# 可以直接 建立一个连接池 然后 作为 参数 Redis 这样可以实现多个Redis 实例
# 共享一个连接池

# import redis
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool, decode_responses=True)
# r.set('name', 'Gesiz')
# print(r.get('name'))
