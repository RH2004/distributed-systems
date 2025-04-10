

---

```markdown
# 💻 Distributed Systems Lab – (Helsinki Uni)

This repository includes hands-on, terminal-based simulations of **key distributed algorithms and protocols** as taught by **Tiina Niklander** in the University of Helsinki’s Distributed Systems course. Based on *Distributed Systems: Principles and Paradigms* by **van Steen & Tanenbaum**, each example is built to reflect real-world distributed systems behavior across processes.

## 📌 Key Features

- ✅ Ready-to-run code for each lecture topic
- 📦 Organized per topic and lecture pair
- 🧠 Educational, fully-commented code
- 🧪 Multi-terminal, real-process testing

---

## 📚 Topics Covered

| Lecture Range | Topics Implemented |
|--------------:|--------------------|
| 1–2           | Client-Server Architecture, Threads, TCP Sockets |
| 3–4           | Remote Procedure Call Simulation, Lamport Logical Clocks |
| 5–6           | Vector Clocks, Totally Ordered Multicast, Bully Election Algorithm |
| 7–8           | Primary-Backup Replication, State Synchronization |
| 9–10          | Naming Services, Distributed File System |
| 11+           | 🚧 Coming Soon: Consistency Models, Transactions, Kafka |

---

## 🚀 Running the Code

Each example must be run in **multiple terminals**, simulating independent nodes.

---

### ▶️ Lecture 1–2: Client-Server Model

**Terminal 1:**
```bash
python server.py
```

**Terminal 2:**
```bash
python client.py
```

---

### ▶️ Lecture 3–4: Lamport Logical Clocks

**Terminal 1:**
```bash
python lamport_server.py
```

**Terminal 2:**
```bash
python lamport_client.py
```

---

### ▶️ Lecture 5–6: Vector Clock Simulation

**Run in 3 separate terminals:**
```bash
python vector_node.py 6000 0 3
python vector_node.py 6001 1 3
python vector_node.py 6002 2 3
```

**In any terminal:**
```
send 6001
tick
send 6002
```

---

### ▶️ Lecture 5–6: Bully Leader Election

**Start 3 terminals:**
```bash
python bully_node.py 0
python bully_node.py 1
python bully_node.py 2
```

**Trigger election in any node:**
```
election
```

---

### ▶️ Lecture 7–8: Primary-Backup Replication

**Terminals:**
```bash
python primary_backup.py primary
python primary_backup.py backup 8001
python primary_backup.py backup 8002
```

**Client Terminal:**
```bash
python replica_client.py
```

---

### ▶️ Lecture 9–10: Distributed File System with Naming Server

**Start 4 terminals:**
```bash
python dfs_naming_server.py
python dfs_storage_node.py 9001 report.txt "Hello from report"
python dfs_storage_node.py 9002 data.csv "42,69,1337"
python dfs_client.py
```

---

## 📁 Suggested Folder Structure

```
distributed-systems-lab/
├── lecture1_2/
│   ├── server.py
│   └── client.py
├── lecture3_4/
│   ├── lamport_server.py
│   └── lamport_client.py
├── lecture5_6/
│   ├── vector_node.py
│   └── bully_node.py
├── lecture7_8/
│   ├── primary_backup.py
│   └── replica_client.py
├── lecture9_10/
│   ├── dfs_naming_server.py
│   ├── dfs_storage_node.py
│   └── dfs_client.py
└── README.md
```

---

## ⚙️ Requirements

- Python 3.6 or above
- Run in separate terminals (or use tmux/terminal multiplexer)
- Localhost IP assumed (`127.0.0.1`)
- Use `CTRL+C` to cleanly terminate processes

---

## ✅ To-Do (Upcoming Lectures)

- [ ] Two-Phase Commit (2PC)
- [ ] Consistency Models: Strong, Causal, Eventual
- [ ] Kafka Pub-Sub, Virtualization via Docker
- [ ] Final Mini Distributed System Project

---

## 📚 References

- Tiina Niklander – Distributed Systems (University of Helsinki)
- A.S. Tanenbaum & M. van Steen – *Distributed Systems: Principles and Paradigms*

---

## 🔓 License

MIT License – Use, learn, remix freely. Credit where credit's due. 💙

---

Happy coding & keep the nodes talking 🧵🛰️  
```

---
