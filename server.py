from ctypes import resize
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

print('Esperando conexão...')
c, addr = s.accept()
print('Conectado')

while True:
    print('Esperando mensagem')
    data = c.recv(1024).decode()
    print(f'Mensagem recebida: {data}')

    if data == 'SAIR':
        print('Conexão encerrada')
        c.close()
        break

    resp = input('Digite resposta: ')
    c.send(resp.encode())
    print('Resposta enviada')
    
    # c.close()
