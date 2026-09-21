# Remote Command Execution System

A Computer Networks mini-project demonstrating TCP client-server communication and controlled remote command execution using Python sockets.

## Current Features

- TCP client-server communication
- Persistent client-server connection
- Command validation using an allowlist
- Execution of permitted Linux commands
- Command output returned to the client
- Graceful connection termination

## Currently Allowed Commands

- `ls`
- `pwd`
- `hostname`
- `whoami`
- `date`

## Architecture

Client → TCP Socket → Server → Command Validation → OS → Server → Client

## Technologies

- Python
- TCP/IP
- Socket Programming
- subprocess
- Linux
