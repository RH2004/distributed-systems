# -----------------------
# DFS Client
# First contacts naming server, then fetches from storage node
# -----------------------

import socket

def dfs_client(filename):
    # Ask naming server
    ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ns.connect(('127.0.0.1', 8500))
    ns.send(filename.encode())
    response = ns.recv(1024).decode()
    ns.close()

    if response == "NOT FOUND":
        print("[Client] File not found.")
        return

    ip, port = response.split(":")
    port = int(port)

    # Ask actual storage node
    sn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sn.connect((ip, port))
    sn.send(filename.encode())
    filedata = sn.recv(4096).decode()
    sn.close()

    print(f"[Client] Received file content: {filedata}")

if __name__ == "__main__":
    dfs_client("report.txt")
