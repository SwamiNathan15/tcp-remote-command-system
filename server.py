import socket
import subprocess

ALLOWED_COMMANDS = {
    "hostname",
    "whoami",
    "date",
    "pwd",
    "ls"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is waiting for a connection...")

client, address = server.accept()

print("Client connected:", address)

while True:

    command = client.recv(1024).decode().strip()

    if not command:
        break

    print("Command received:", command)

    if command == "exit":
        client.send("Connection closed.".encode())
        break

    command_parts = command.split()

    command_name = command_parts[0]

    arguments = command_parts[1:]

    if command_name in ALLOWED_COMMANDS:

        result = subprocess.run(
            [command_name] + arguments,
            capture_output=True,
            text=True
        )

        output = result.stdout

        if result.stderr:
            output = result.stderr

    else:

        output = "ERROR: Command not allowed."

    client.send(output.encode())

client.close()
server.close()

print("Server stopped.")