import socket


def handler_client_request(client_socket):
    """和浏览器进行数据交互的函数和"""

    # 接受数据
    recv_data = client_socket.recv(1000000)

    if len(recv_data) == 0:
        print("客户端关闭!!!")
        return

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

    # 异常捕获(防止出现异常的时候 服务器直接崩溃)
    try:
        # 打开资源文件
        f = open("./static" + request_path, "rb")
        # 存放了图片资源
        file_data = f.read()
        f.close()
    except Exception as e:
        # 浏览器访问的网址里的资源不存在的情况下
        # 证明:文件不存在
        print("异常信息:", e)
        # 访问不成功的情况下的响应报文
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header = "Content-Type: text/html; charset=UTF-8\r\n"
        response_body = "对不起 你访问的页面不存在!!!"
        # 把没有找到相应的文件的这个信息发给浏览器
        response_data = response_line + response_header + "\r\n" + response_body
        client_socket.send(response_data.encode())
        client_socket.close()
    else:
        # 浏览器访问的网址里的资源存在的情况下
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "server:py1.0\r\n"
        response_body = file_data
        # 响应数据
        response_data = (response_line + response_header + "\r\n").encode() + response_body

        # 发送数据
        client_socket.send(response_data)
        client_socket.close()


def main():
    """
    控制整个服务器流程的函数
       tcp_server_socket: 用来就收链接的socket
       client_socket: 用来处理和浏览器之间的数据交流的socket
    """

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

        # 调用处理浏览器请求的函数
        handler_client_request(client_socket)


if __name__ == '__main__':
    main()
