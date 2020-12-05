import socket

# 1 创建服务端套接字对象
# 参数 1 ipv4
# 参数 2 tcp协议
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 一旦服务关闭 端口立马释放
# 端口复用操作
# 参数 1 socket 选项列表
# 参数 2 地址复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# 2 绑定端口号
# 参数 元组(两个元素)
# 参数: 元组(两个元素) 元素1:IP地址(字符串) 元素 2 端口号(数字)
# 不写就是默认回环地址
tcp_server_socket.bind(("", 8080))

# 3 设置监听
# 参数: 最大监听个数(排队处理的最大等待数量)
# tcp_server_socket 从主动套接字变为了被动套接字
tcp_server_socket.listen(128)

# 4 等待接收客户端的连接请求
client_socket, client_addr = tcp_server_socket.accept()

# 返回值是一个月租(有两个元素): 元素 1 和客户端进行同学的socket 元素2 客户端地址信息 IP PORT
# 5 接收数据
while True:
    client_data = client_socket.recv(1024).decode()
    if len(client_data) == 0:
        print("客户端关闭了")
        break
    print(client_data)
    # 6 发送数据
    client_socket.send(client_data.encode())
# 7 关闭套接字
client_socket.close()
tcp_server_socket.close()