# -----------------------
# Lecture 3–4: Lamport Logical Clocks
# Client
# -----------------------
# This client sends a logical clock value to a server and receives its updated value.

import socket

class LamportClock:
    def __init__(self):
        self.time = 0

    def tick(self):
        """Advance local clock by one"""
        self.time += 1

def run_lamport_client(server_port):
    clock = LamportClock()
    clock.tick()  # simulate local event

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', server_port))

    print(f"[Lamport Client] Sending local clock value: {clock.time}")
    client_socket.send(str(clock.time).encode())

    updated_time = client_socket.recv(1024).decode()
    print(f"[Lamport Client] Received updated time from server: {updated_time}")
    client_socket.close()

if __name__ == "__main__":
    run_lamport_client(server_port=6000)
