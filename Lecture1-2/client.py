# -----------------------
# Lecture 1–2: Distributed Systems Basics
# Client Side
# -----------------------
# This client connects to the server, receives a message, and exits.

import socket

def run_client(server_host='127.0.0.1', server_port=5000):
    """Connects to the server and receives a welcome message"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    response = client_socket.recv(1024).decode()
    print(f"[Client] Received: {response}")
    client_socket.close()

if __name__ == "__main__":
    run_client()
