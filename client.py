import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print('conectando-se ao servidor')
print('conectado')
s.connect((host, port))
while True:
    msg = input('Digite a mensagem: ')
    s.send(msg.encode())
    print('Mensagem enviada')

    if msg == 'SAIR':
        print('Desconectado')
        s.close()
        break

    print('Esperando resposta')
    resp = s.recv(1024).decode()
    print(f'Resposta recebida: {resp}')

# s.close()