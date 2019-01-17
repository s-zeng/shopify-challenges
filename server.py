import socket

host = ''
port = 8000

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.bind((host, port))
main_socket.listen(1)

print("serving http")

while True:
    connection, address = main_socket.accept()
    request = connection.recv(1024)
    print(request)

    response = b"HTTP/1.1 200 OK\r\n\r\nHello!"

    connection.sendall(response)
    connection.close()
