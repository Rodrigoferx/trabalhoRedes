import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9898))

print('Estabelecendo conexão...\n')

server.listen(1)

conexao, endereco = server.accept()

nomearquivo = conexao.recv(1024).decode()

with open(nomearquivo, 'rb') as file:
    for data in file.readlines():
        conexao.send(data)

    print('Arquivo enviado')    