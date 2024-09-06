# python3
import json
import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 80))
serv_sock.listen(10)
data = ''

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        request_data = client_sock.recv(1024).decode('utf-8')

        if "\r\n\r\n" in request_data:
            request_body = request_data.split("\r\n\r\n")[1]

            try:
                json_data = json.loads(request_body)
                if "data_input" in json_data:
                    data = json_data['data_input']
                    print(data)
                    client_sock.sendall(data.encode('utf-8'))
                else:
                    print("Ключ 'data_input' не найден в JSON")
            except json.JSONDecodeError:
                print("Ошибка парсинга JSON")
        else:
            # клиент не отправил запрос
            break

    client_sock.close()

