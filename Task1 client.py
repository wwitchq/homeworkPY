import socket

# Создаем клиентский сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
client_socket.connect(server_address)

try:
    while True:
        message = input("Клиент: ")
        client_socket.sendall(message.encode('utf-8'))

        if message == "Пока":
            break

        data = client_socket.recv(1024).decode('utf-8')
        print("Сервер:", data)

        if data == "Пока":
            break

finally:
    client_socket.close()
