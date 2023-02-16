import socket
from packet import Packet
import struct

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Create a new Packet object and set the data field
    packet = Packet()
    packet.data = 1234
    packet.formatter = '!I'

    # Pack the integer message into a 4-byte string and send to the server
    packed_message = packet.pack()
    client_socket.sendall(packed_message)

    # Receive the server's response and unpack it into an integer
    response = client_socket.recv(1024)
    unpacked_response = struct.unpack(packet.formatter, response)[0]
    print('Received:', unpacked_response)