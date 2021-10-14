import socket as s
import sys

while 1:

    my_socket  =  s.socket(s.AF_INET, s.SOCK_STREAM)
    my_socket.connect((sys.argv[1], int(sys.argv[2])))
   
    print('client: ')
    msg = input()
    my_socket.sendall( bytes(msg, encoding='utf-8' ))

    print('Aguardando servidor: ')
    data = my_socket.recv(1024)
    print('Mensagem: ', data.decode('utf-8')) 

    my_socket.close()
