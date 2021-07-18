import socket
import logging
import re
from http import HTTPStatus

logging.basicConfig(level=logging.DEBUG)

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        data = str(data.decode("utf-8"))
        print(data)
        code = re.split('\n', data)
        code_two = re.split(' ', code[0])
        code_tree = re.split('=', code_two[1])
        print(code_tree[1])
        sorce_ip = str(addr)
        print(sorce_ip)
        try:
            resp_status = HTTPStatus(int(code_tree[1])).phrase
            data = (" Request Method: GET\n" + " Request Source:" + sorce_ip + "\n" +
                    " Response Status: " + code_tree[1] + HTTPStatus(int(code_tree[1])).phrase + "\n" +
                    " Content-Type: text/html; charset=UTF-8")
            conn.sendall(data.encode("utf-8"))
        except:
            data = (" Request Method: GET\n" + " Request Source:" + sorce_ip + "\n" +
                    " Response Status: 200 OK Content-Type: text/html; charset=UTF-8")
            conn.send(data.encode())