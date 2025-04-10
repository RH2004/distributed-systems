# -----------------------
# Lecture 1–2: Distributed Systems Basics
# Server Side
# -----------------------
# This server listens on a port and handles each client using a separate thread.
# It’s stateless: doesn’t remember the client between requests.

import socket
import threading

def handle_client(conn, addr):
    """Handles one client connection"""
    print(f"[+] New connection from {addr}")
    conn.sendall(b"Hello from the server!\n")
    conn.close()
    print(f"[-] Connection to {addr} closed")

def start_server(host='127.0.0.1', port=5000):
    """Starts a threaded TCP server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"[Server] Listening on {host}:{port} ...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
