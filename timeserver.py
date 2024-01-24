#!/usr/bin/env python3

import socket
import datetime


SERVER_IP = '0.0.0.0'
SERVER_PORT = 1303


def start_server():
    server_socket = socket.socket()
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print("Server listening on port 1303...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        current_time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        client_socket.sendall(current_time.encode())

        client_socket.close()
        print(f"Connection with {client_address} closed")


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer terminated by user.")
