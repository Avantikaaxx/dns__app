from flask import Flask, request, jsonify
import requests
from werkzeug.exceptions import HTTPException
from socket import *
fiboapp = Flask(__name__)

@fiboapp.route('/fibonacci')
def parameter():
    try:
        host = request.args['hostname']
        fs_port = request.args['fs_port']
        number = request.args['number']
        as_ip = request.args['as_ip']
        as_port = request.args['as_port']
        
        
        autho_ip = as_ip
        autho_port = int(as_port)

        us_socket = socket(AF_INET, SOCK_DGRAM)
        message = 'TYPE=A \n NAME='+host
        us_socket.sendto(message.encode(), (autho_ip, autho_port))

        
        modified_message, server_address = us_socket.recvfrom(2048)
        msg = modified_message.decode('utf-8')
        Type, Name, Value, TTL = msg.split('\n')
        IP = Value.strip().split('=')[-1]

        path_fib = 'http://'+IP+':'+fs_port+'/fibonacci?number='+number

        fibo_json = requests.get(url = path_fib)
        params = fibo_json.json()
        fibo_num = params['s']
        dnum = fibo_num.split("=")[-1]
        print(dnum)
        
        status_code = "200 - The request was successful"
        output_string = status_code + "  Fibonacci Number = "  +dnum 
        return output_string
       
        us_socket.close()

    except HTTPException:
       http_code = "400 - The request failed."
       return(http_code)

fiboapp.run(host='0.0.0.0',port=8080,debug=True)