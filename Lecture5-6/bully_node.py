# -----------------------
# Lecture 5–6: Bully Election Algorithm
# Run each node in a separate terminal
# -----------------------

import socket
import threading
import sys
import time

class BullyNode:
    def __init__(self, my_id, all_ids, my_port, port_map):
        self.my_id = my_id
        self.all_ids = all_ids
        self.my_port = my_port
        self.port_map = port_map
        self.coordinator = None
        self.alive = True

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', self.my_port))
        server.listen()

        while True:
            conn, _ = server.accept()
            data = conn.recv(1024).decode()
            if data == "ELECTION":
                print(f"[{self.my_id}] Received ELECTION, replying OK")
                conn.send(b"OK")
                self.start_election()
            elif data.startswith("COORDINATOR"):
                _, cid = data.split()
                self.coordinator = int(cid)
                print(f"[{self.my_id}] Coordinator is now {self.coordinator}")
            conn.close()

    def send_message(self, target_id, msg):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('127.0.0.1', self.port_map[target_id]))
            sock.send(msg.encode())
            sock.settimeout(2)
            reply = sock.recv(1024).decode()
            sock.close()
            return reply
        except:
            return None

    def start_election(self):
        print(f"[{self.my_id}] Starting election...")
        higher = [nid for nid in self.all_ids if nid > self.my_id]
        got_reply = False
        for nid in higher:
            reply = self.send_message(nid, "ELECTION")
            if reply == "OK":
                got_reply = True

        if not got_reply:
            self.coordinator = self.my_id
            print(f"[{self.my_id}] I am the new coordinator")
            for nid in self.all_ids:
                if nid != self.my_id:
                    self.send_message(nid, f"COORDINATOR {self.my_id}")

    def run(self):
        threading.Thread(target=self.start_server, daemon=True).start()
        print(f"[{self.my_id}] Bully node running on port {self.my_port}")
        while True:
            cmd = input("> ").strip()
            if cmd == "election":
                self.start_election()
