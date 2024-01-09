"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""
import socket

# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5555)
server_socket.bind(server_address)
server_socket.listen(1)

print("Ждем подключения клиента...")
connection, client_address = server_socket.accept()

try:
    print("Подключился клиент:", client_address)

    while True:
        data = connection.recv(1024).decode('utf-8')
        print("Клиент:", data)

        if data == "Пока":
            break

        message = input("Сервер: ")
        connection.sendall(message.encode('utf-8'))
        if message == "Пока":
            break

finally:
    connection.close()
