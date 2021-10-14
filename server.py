import socket as s
import sys

my_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
my_socket.bind((sys.argv[1], int(sys.argv[2])))
my_socket.listen()

count = 0

while 1:
    
    conn, addr =  my_socket.accept()
    
    if count <= 0:
        print(f'client {addr[0]} conectado')
        count += 1
   
    print('Aguadando cliente...')
    data  = conn.recv(1024)

    print('Mensagem: ', data.decode('utf-8'))

    print('server')
    msg = input()

    conn.sendall(bytes(msg, encoding='utf-8'))
   
    conn.close()
