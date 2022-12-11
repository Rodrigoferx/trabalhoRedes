import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9898))

print('Conectado!\n')

nomearquivo = str(input('Digite o arquivo que deseja receber>'))

client.send(nomearquivo.encode())

with open(nomearquivo, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{nomearquivo} Recebido!\n')