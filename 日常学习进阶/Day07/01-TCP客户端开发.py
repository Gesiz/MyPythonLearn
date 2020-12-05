import socket

# 1 创建客户端套接字对象(买电话)

# 参数 1: ipv4(ip协议的版本)

# 参数 2 : 选择协议(SOCK_STREAM ==> tcp协议)
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 和服务端套接字建立连接 (打电话)
# 参数 元组(有两个元素)
# 元素 1 服务器的IP地址(字符串)
# 元素 2 服务器的端口号(数字)
tcp_client_socket.connect(("192.168.158.129", 8080))
# 3 发送数据(说话)
tcp_client_socket.send("123".encode("utf-8"))
# 4 接收数据(聆听)
# 注意 recv 会阻塞等待数据的到来
recv_data = tcp_client_socket.recv(1024)
print(recv_data)

# 5 关闭客户端套接字
tcp_client_socket.close()
# import socket
#
# tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# tcp_client_socket.connect(("192.168.158.128",8080))
#
# tcp_client_socket.send("123123".encode("utf-8"))
#
# tcp_msg = tcp_client_socket.recv(1024)
# print(tcp_msg)
#
# tcp_client_socket.close()
