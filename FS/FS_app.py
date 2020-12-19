from flask import Flask, request, jsonify
from socket import *

fiboapp = Flask(__name__)

@fiboapp.route('/fibonacci')
def Fib():
    try:     
        n = int(request.args['number'])
        if n==0:
            return 0
        y,x = 0,1
        for i in range(1,n):
            y, x = x, x+y
            fib_num = str(x)
        status_code = "200 - The request was successful"
        output_string = status_code + "  Fibonacci Number = "  +fib_num
        output_final = {"s": output_string} 
        return jsonify(output_final)
        
    except ValueError:
        status_code = "400 - The request failed."
        return(status_code)
        
@fiboapp.route('/register', methods =  ['PUT'])
def register():
    fs_d = request.get_json()
    as_ip = fs_d['as_ip']
    as_port = fs_d['as_port']
    host = fs_d['hostname']
    ip_add = fs_d['ip']

    

    server_name = as_ip
    server_port = int(as_port)

    client_socket = socket(AF_INET, SOCK_DGRAM)
    message = 'TYPE = A \n NAME='+host+'\n VALUE ='+ip_add+ '\n TTL=10'
    client_socket.sendto(message.encode(), (server_name, server_port))

    

    modified_message, server_address = client_socket.recvfrom(2048)

    status_code = str(modified_message.decode())
    s = "status_code is:" + "\t" + status_code +"\n"
    
    client_socket.close()
    return (s)
fiboapp.run(host='0.0.0.0',port=9090,debug=True) 
