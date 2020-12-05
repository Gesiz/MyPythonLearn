import multiprocessing
import threading
import socket


class my_socket():
    def __init__(self):
        self.clientSocket = None
        self.clientAddr = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)


class tcp_client_socket(my_socket):
    def __init__(self):
        super().__init__()
        self.socket.connect(("192.168.158.129", 8080))

    def sendMsg(self, Msg):
        self.socket.send(Msg.encode("utf-8"))

    def readMsg(self):
        return self.socket.recv(1024).decode()

    def __del__(self):
        self.socket.close()


class tcp_server_socket(my_socket):
    def __init__(self):
        super().__init__()
        self.socket.bind(("", 8080))
        self.socket.listen(128)

    def recvMsg(self):
        while True:
            if len(self.clientSocket.recv(1024).decode()) != 0:
                print("接收消息")
            else:
                print("断开连接")
                print(multiprocessing.current_process())

                break

    def startServer(self):
        while True:
            self.clientSocket, self.clientAddr = self.socket.accept()
            sub_process = multiprocessing.Process(target=self.recvMsg)
            sub_process.start()

    def __del__(self):
        self.clientSocket.close()
        self.socket.close()


if __name__ == '__main__':
    # my_socket1 = tcp_client_socket()
    # my_socket1.sendMsg("666")
    my_socket2 = tcp_server_socket()
    my_socket2.startServer()
