import socket
import static
import os
import multiprocessing
import threading

class WebServer:
    def __init__(self,port=8080):
        # 创建电话
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 端口复用
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 绑定地址
        self.tcp_server_socket.bind(("", port))

        # 设置监听
        self.tcp_server_socket.listen(128)

    def handler_client_socket(client_socket):
        """和浏览器进行交互的函数"""
        recv_data = client_socket.recv(102400000)
        if len(recv_data) == 0:
            print("客户端关闭")
            return
        recv_data = recv_data.decode()
        path_list = recv_data.split(" ")
        print(f"列表：{path_list}")

        # 请求资源路径
        request_path = path_list[1]

        # 响应行
        # if len(request_path) == 0:
        #     request_path = "/index.html"

        # 异常捕获 (防止出现异常的时候 服务器直接崩溃)

        # 打开资源文件
        try:
            f = open(f"./static{request_path}", "rb")
            # 存放图片资源
            file_data = f.read()
            f.close()
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "server:py1.0\r\n"
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            client_socket.send(response_data)
        except Exception as e:
            # 浏览器访问的网址里的资源不存在的情况下
            # 证明 文件不存在
            print("异常信息: ", e)
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "server:py1.0\r\n" \
                              "Content-Type:text/html;charset:utf-8\r\n"

            response_body = "兄弟找不到啊"
            response_data = (response_line + response_header + "\r\n") + response_body
            client_socket.send(response_data.encode())

        # 响应数据

        # 发送数据

        client_socket.close()

    def start(self):
        """控制整个我们服务器流程的函数
            tcp_server_socket 用来接受的链接的socket
        """

        while True:
            # 接受链接请求
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 创建多进程
            # 调用处理浏览器请求的函数

            sub_process = threading.Thread(target=self.handler_client_socket, args=(client_socket,))
            # handler_client_socket(client_socket)
            sub_process.start()

import sys
if __name__ == '__main__':
    port = sys.argv[1]
    webserver = WebServer(int(port))
    webserver.start()
