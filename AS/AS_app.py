from socket import *
import sys
server_port = 53533


server_socket = socket(AF_INET, SOCK_DGRAM)


server_socket.bind(('', server_port))

print('Server is now ready to receive messages...')
while True:

message, client_address = server_socket.recvfrom(2048)
as_d = message.decode()


if 'VALUE' and 'TTL' in as_d:
    file = open('file.txt','w')
    file.write(as_d)
    file.close()

    modified_message = '201'
    server_socket.sendto(modified_message.encode(), client_address)
        
    
else:
    TY1, Name = as_d.split('\n')
    Host = Name.strip().split('=')[1]
    TY2 = TY1.strip().split('=')[1]
    file = open('file.txt', 'r')
    filedata = file.read()
        
    TY3, Name_2, Value, TTL = filedata.split('\n')
    if 'A' in TY3 and Host in Name_2 :
        modified_message = str(filedata)
        server_socket.sendto(modified_message.encode(), client_address)