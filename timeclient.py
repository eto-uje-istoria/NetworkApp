#!/usr/bin/env python3

import socket


SERVER_PORT = 1303


def start_client():
    server_ip = input("Enter server IP address: ")

    client_socket = socket.socket()
    client_socket.connect((server_ip, SERVER_PORT))

    data = client_socket.recv(1024).decode()
    print(f"Server response: {data}")

    client_socket.close()
    print("Connection closed")


if __name__ == "__main__":
    try:
        start_client()
    except KeyboardInterrupt:
        print("\nClient terminated by user.")
