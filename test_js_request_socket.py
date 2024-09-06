import socket
import requests
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('https://feline-master-eagerly.ngrok-free.app', 4040))

print('Client start')
message = str(input('Input message: '))

url = "https://feline-master-eagerly.ngrok-free.app"
headers = {
    'Content-type': 'application/json',
    "ngrok-skip-browser-warning": 'true',
    'Accept': 'text/plain',
    'Content-Encoding': 'utf-8'}
data = {'data_input': message}
answer = requests.post(url, data=json.dumps(data), headers=headers)
print('Status: ', requests.get(url=url, headers=headers))
print('Text: ', message)


