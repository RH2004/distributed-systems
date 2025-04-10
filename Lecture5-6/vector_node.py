# -----------------------
# Lecture 5–6: Vector Clocks
# Single node implementation (run in each terminal)
# -----------------------

import socket
import threading
import pickle
import sys
import time

class VectorClock:
    def __init__(self, pid, total):
        self.clock = [0] * total
        self.pid = pid

    def tick(self):
        self.clock[self.pid] += 1

    def update(self, other):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], other[i])
        self.tick()  # Tick after merging

    def __str__(self):
        return str(self.clock)

# Handles incoming messages
def receive_messages(sock, vc):
    while True:
        conn, addr = sock.accept()
        data = conn.recv(4096)
        other_clock = pickle.loads(data)
        print(f"[{vc.pid}] Received VC: {other_clock} from {addr}")
        vc.update(other_clock)
        print(f"[{vc.pid}] Updated VC: {vc}")
        conn.close()

def send_message(target_port, vc):
    vc.tick()  # Local event before sending
    data = pickle.dumps(vc.clock)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', target_port))
    sock.send(data)
    sock.close()
    print(f"[{vc.pid}] Sent VC: {vc} to port {target_port}")

def start_vector_node(my_port, pid, total_processes):
    vc = VectorClock(pid, total_processes)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', my_port))
    server.listen()
    threading.Thread(target=receive_messages, args=(server, vc), daemon=True).start()

    print(f"[{pid}] Vector clock node running on port {my_port}.")
    print(f"Type 'send <port>' to send vector clock.")
    print("Type 'tick' to simulate local event.\n")

    while True:
        cmd = input("> ").strip()
        if cmd.startswith("send"):
            _, port = cmd.split()
            send_message(int(port), vc)
        elif cmd == "tick":
            vc.tick()
            print(f"[{vc.pid}] Local tick: {vc}")
