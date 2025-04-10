# -----------------------
# Client to talk to primary replica
# -----------------------
import socket

def send_increment(value):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8000))  # Primary's port
    sock.send(f"inc {value}".encode())
    result = sock.recv(1024).decode()
    print("[Client]", result)
    sock.close()

if __name__ == "__main__":
    send_increment(10)
