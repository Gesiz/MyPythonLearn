import socket

# 创建电话
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定地址
tcp_server_socket.bind(("", 8080))
# 设置监听
tcp_server_socket.listen(128)

while True:
    # 接受链接请求
    client_socket, addr = tcp_server_socket.accept()
    # 接受数据
    recv_data = client_socket.recv(100000)

    if len(recv_data) == 0:
        print("客户端关闭!!!")
        break

    print(recv_data.decode())

    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "server:py1.0\r\n"
    response_body = "aaa"
    # 响应数据
    response_data = response_line + response_header + "\r\n" + response_body

    # 发送数据
    client_socket.send(response_data.encode())
    client_socket.close()
