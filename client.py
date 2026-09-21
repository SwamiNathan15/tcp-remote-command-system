import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

while True:

    command = input("Enter command: ")

    client.send(command.encode())

    response = client.recv(4096).decode()

    print("Server response:")
    print(response)

    if command == "exit":
        break

client.close()