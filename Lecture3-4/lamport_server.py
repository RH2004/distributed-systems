# -----------------------
# Lecture 3–4: Lamport Logical Clocks
# Server
# -----------------------
# This server receives logical clock values and updates its own clock accordingly.

import socket

class LamportClock:
    def __init__(self):
        self.time = 0

    def tick(self):
        """Advance local clock by one"""
        self.time += 1

    def update(self, received_time):
        """Update local clock using max rule"""
        self.time = max(self.time, received_time) + 1

def run_lamport_server(port):
    clock = LamportClock()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen()

    print(f"[Lamport Server] Listening on port {port} ...")

    while True:
        conn, addr = server_socket.accept()
        data = conn.recv(1024).decode()
        received_time = int(data)
        print(f"[Lamport Server] Received time {received_time} from {addr}")
        clock.update(received_time)
        print(f"[Lamport Server] Updated local time to {clock.time}")
        conn.send(str(clock.time).encode())
        conn.close()

if __name__ == "__main__":
    run_lamport_server(port=6000)
