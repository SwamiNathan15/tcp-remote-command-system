import socket


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


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

while True:

    command = input("Enter command: ")

    send_message(client, command)

    response = receive_message(client)

    if response is None:
        break

    print("Server response:")
    print(response)

    if command == "exit":
        break

client.close()