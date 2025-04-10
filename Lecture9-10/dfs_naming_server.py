# -----------------------
# Lecture 9–10: Naming Server
# Keeps track of where files are stored
# -----------------------

import socket
import threading

file_registry = {
    'report.txt': ('127.0.0.1', 9001),
    'data.csv': ('127.0.0.1', 9002),
}

def naming_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8500))
    sock.listen()
    print("[NamingServer] Listening on port 8500")

    while True:
        conn, _ = sock.accept()
        filename = conn.recv(1024).decode()
        if filename in file_registry:
            ip, port = file_registry[filename]
            conn.send(f"{ip}:{port}".encode())
        else:
            conn.send(b"NOT FOUND")
        conn.close()

if __name__ == "__main__":
    naming_server()
