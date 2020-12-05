import socket


def tcp_client_socket():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.158.128", 8080))
    tcp_client_socket.send("asd".encode())
    print(tcp_client_socket.recv(1024).decode())
    tcp_client_socket.close()


def tcp_server_socket():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)
    socket_server, addr = tcp_server_socket.accept()
    print(socket_server.recv(1024).decode())
    socket_server.send("555".encode())
    socket_server.close()
    tcp_server_socket.close()