# TCP Remote Command Execution System

A Python-based client-server application that demonstrates TCP socket communication and controlled remote command execution on a Linux system.

The system allows a client to send predefined Linux commands to a server over a TCP connection. The server validates the requested command, executes it in a controlled manner, and sends the command output back to the client.

---

## 1. Project Overview

The TCP Remote Command Execution System is a Computer Networks mini-project designed to demonstrate practical concepts of:

- TCP client-server communication
- Socket programming
- Request and response communication
- TCP message framing
- Remote command execution
- Command validation
- Process management
- File and directory operations
- Network diagnostics
- Server-side logging

The project consists of two Python programs:

- `server.py` — accepts client connections, validates commands, executes them, and returns responses.
- `client.py` — connects to the server, sends commands, and displays server responses.

---

## 2. Objectives

The main objectives of this project are:

1. To understand TCP socket programming using Python.
2. To implement client-server communication.
3. To understand how TCP data is transmitted as a byte stream.
4. To implement application-level message framing.
5. To execute predefined Linux commands remotely.
6. To validate commands using an allowlist.
7. To handle command arguments safely without using a shell.
8. To maintain the client's current working directory on the server.
9. To implement basic process-management functionality.
10. To maintain server-side activity logs.

---

## 3. System Architecture

```text
                    TCP Connection
        ┌─────────────────────────────────┐
        │                                 │
        ▼                                 │
┌───────────────┐                  ┌───────────────┐
│     Client    │                  │     Server    │
│   client.py   │                  │   server.py   │
└───────┬───────┘                  └───────┬───────┘
        │                                  │
        │      Command + Length Prefix     │
        ├─────────────────────────────────►│
        │                                  │
        │                           Validate command
        │                                  │
        │                           Execute command
        │                                  │
        │      Response + Length Prefix     │
        │◄─────────────────────────────────┤
        │                                  │
        ▼                                  ▼
 Display response                    server.log
