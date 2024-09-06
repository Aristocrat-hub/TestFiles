import socket
import ssl

# Указываем ваш домен
host = "feline-master-eagerly.ngrok-free.app"
port = 443  # Порт для HTTPS

# Пользователь вводит сообщение для отправки
user_message = input("Введите ваше сообщение для отправки на сервер: ")

# Формируем HTTP-запрос с пользовательским сообщением в теле
request = "POST / HTTP/1.1\r\n" \
          "Host: {}\r\n" \
          "ngrok-skip-browser-warning: true\r\n" \
          "Content-Type: text/plain\r\n" \
          "Content-Length: {}\r\n" \
          "Connection: close\r\n\r\n{}".format(
    host, len(user_message), user_message
)

# Создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Оборачиваем сокет в SSL-контекст для HTTPS
context = ssl.create_default_context()
ssl_sock = context.wrap_socket(sock, server_hostname=host)

# Подключаемся к серверу
ssl_sock.connect((host, port))

# Отправляем данные (HTTP-запрос)
ssl_sock.sendall(request.encode())

# Получаем ответ от сервера
response = b""
while True:
    data = ssl_sock.recv(4096)
    if not data:
        break
    response += data

# Закрываем соединение
ssl_sock.close()

# Выводим ответ сервера
print("Ответ от сервера:\n", response.decode('utf-8', errors='ignore'))
