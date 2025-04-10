# -----------------------
# Lecture 9–10: Storage Node
# Stores actual file contents
# -----------------------

import socket
import sys

def storage_node(port, filename, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', port))
    sock.listen()
    print(f"[StorageNode] Ready with '{filename}' on port {port}")

    while True:
        conn, _ = sock.accept()
        request = conn.recv(1024).decode()
        if request == filename:
            conn.send(content.encode())
        else:
            conn.send(b"NOT FOUND")
        conn.close()

if __name__ == "__main__":
    port = int(sys.argv[1])
    filename = sys.argv[2]
    content = sys.argv[3]
    storage_node(port, filename, content)
