# -----------------------
# Lecture 7–8: Primary-Backup Replication
# One process is primary, others backup. Only primary handles clients.
# -----------------------

import socket
import threading
import time
import sys

state = 0
is_primary = False
backups = [('127.0.0.1', 8001), ('127.0.0.1', 8002)]

def broadcast_state(new_state):
    """Send updated state to all backups"""
    for host, port in backups:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.send(str(new_state).encode())
            sock.close()
        except Exception:
            pass  # Backup might be down

def primary_server():
    global state
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    print("[Primary] Listening on port 8000")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode()
        if data.startswith("inc"):
            _, value = data.split()
            state += int(value)
            print(f"[Primary] New state: {state}")
            broadcast_state(state)
            conn.send(f"OK. State is now {state}".encode())
        conn.close()

def backup_server(port):
    global state
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', port))
    server.listen()
    print(f"[Backup] Listening on port {port}")
    while True:
        conn, _ = server.accept()
        data = conn.recv(1024).decode()
        state = int(data)
        print(f"[Backup] Updated state: {state}")
        conn.close()

if __name__ == "__main__":
    role = sys.argv[1]  # 'primary' or 'backup'
    if role == 'primary':
        is_primary = True
        primary_server()
    elif role == 'backup':
        port = int(sys.argv[2])
        backup_server(port)
