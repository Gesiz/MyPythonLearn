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
    recv_data = client_socket.recv(1000000)

    if len(recv_data) == 0:
        print("客户端关闭!!!")
        break

    # 解码
    recv_data = recv_data.decode()
    print("请求报文!!!:", recv_data)

    # 对请求报文进行切割
    path_list = recv_data.split(" ")
    print("列表!!!", path_list)

    # 请求资源路径 /index.html /index2.html
    request_path = path_list[1]

    # 设置主页
    if request_path == "/":
        request_path = "/index.html"

    # 打开资源文件
    f = open("./static" + request_path, "rb")
    # 存放了图片资源
    file_data = f.read()
    f.close()

    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "server:py1.0\r\n"
    response_body = file_data
    # 响应数据
    response_data = (response_line + response_header + "\r\n").encode() + response_body

    # 发送数据
    client_socket.send(response_data)
    client_socket.close()
