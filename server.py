import socket
import subprocess
import os 
import shlex
import logging

current_directory = os.getcwd()
server_pid = os.getpid()

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def receive_message(sock):
    data = b""

    while len(data) < 4:
        chunk = sock.recv(4 - len(data))
        if not chunk:
            return None
        data += chunk

    message_length = int.from_bytes(data, byteorder="big")

    data = b""

    while len(data) < message_length:
        chunk = sock.recv(message_length - len(data))
        if not chunk:
            return None
        data += chunk

    return data.decode()


def send_message(sock, message):
    data = message.encode()

    message_length = len(data)

    sock.sendall(
        message_length.to_bytes(4, byteorder="big") + data
    )


ALLOWED_COMMANDS = {
    "pwd",
    "ls",
    "cd",
    "mkdir",
    "touch",
    "cp",
    "mv",
    "rm",
    "cat",
    "less",
    "head",
    "tail",
    "find",
    "grep",
    "which",
    "ps",
    "kill",
    "df",
    "free",
    "ip",
    "ping",
    "ss",
    "curl",
    "git",
    "whoami",
    "date"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is waiting for a connection...")

client, address = server.accept()

print("Client connected:", address)
logging.info("Client connected: %s", address)

while True:

    command = receive_message(client)
    
    if command is None:
        break
    
    command = command.strip()

    if not command:
        break

    print("Command received:", command)
    logging.info("Command received: %s", command)

    if command == "exit":
        send_message(client, "Connection closed.")
        break

    command_parts = shlex.split(command)

    command_name = command_parts[0]

    arguments = command_parts[1:]
    
    if command_name == "cd":

        if len(arguments) != 1:
            output = "ERROR: cd requires exactly one directory."

        else:
            new_directory = os.path.abspath(
            os.path.join(current_directory, arguments[0])
        )

            if os.path.isdir(new_directory):
                current_directory = new_directory
                output = "Directory changed successfully."
            else:
                output = "ERROR: Directory does not exist."
                
    elif command_name == "kill":

        if len(arguments) != 1:
            output = "ERROR: kill requires exactly one PID."

        else:
            try:
                pid = int(arguments[0])

                if pid == server_pid:
                    output = "ERROR: Cannot kill the command server itself."

                else:
                    result = subprocess.run(
                        ["kill", str(pid)],
                        capture_output=True,
                        text=True
                    )

                    if result.stderr:
                        output = result.stderr
                    else:
                        output = "Process terminated successfully."

            except ValueError:
                output = "ERROR: PID must be a number."

    elif command_name in ALLOWED_COMMANDS:

        result = subprocess.run(
            [command_name] + arguments,
            capture_output=True,
            text=True,
            cwd=current_directory
        )

        output = result.stdout

        if result.stderr:
            output = result.stderr

        if not output:
            output = "Command executed successfully."

    else:

        output = "ERROR: Command not allowed."

    send_message(client, output)
    
logging.info("Client disconnected")

client.close()
server.close()

print("Server stopped.")