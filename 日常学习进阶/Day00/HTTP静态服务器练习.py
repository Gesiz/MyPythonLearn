import threading, sys, socket


class WebServer:

    def __init__(self, port=8080):
        # 设置IPV4 创建 网际(AF_INET) 字节流(SOCK_STREAM) 套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置Socket 描述符号选项 LEVEL 级别设置为 SOL_SOCKET SO_REUSEADDR 打开地址复用功能 默认为关闭
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 对套接字进行地址及端口的绑定
        self.tcp_server_socket.bind(("", port))
        # listen 函数使用主动链接变为被链接套接口 使一个进程可以接受其他进程的请求 从而成为一个服务器进程
        self.tcp_server_socket.listen(128)

    def startServer(self):
        while True:
            connection_socket, connection_addr = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.recvData, args=(connection_socket,))
            sub_thread.start()

    def recvData(self, connection_socket):

        recv_data = connection_socket.recv(1024).decode()
        recv_data = recv_data.split(" ")
        request_line = "HTTP/1.1 400 OK\r\n"
        request_head = "Server:Python3.9\r\n\r\n"
        request_body = b"\r\n"
        try:
            with open(f"./static{recv_data[1]}", "rb") as f:
                request_body = f.read()

        except Exception as e:
            print(e)
            request_line = "HTTP/1.1 404 NOT FOUND\r\n"

        request_data = (request_line + request_head).encode() + request_body

        connection_socket.send(request_data)

        connection_socket.close()



if __name__ == '__main__':
    A = WebServer()
    A.startServer()
