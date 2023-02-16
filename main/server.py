import socket

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 5000  # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print('Server listening on port', PORT)
    connection, address = server_socket.accept()
    print('Connected by', address)

    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)

    connection.close()
