import socket
import logging
import re
from http import HTTPStatus

logging.basicConfig(level=logging.DEBUG)

HOST = "127.0.0.1"
PORT = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Binding server on {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:

        conn.send("Hello, I am server!".encode("utf-8"))

        while True:

            data = conn.recv(1024)
            # print("Received Inna", data, "from", addr)

            if not data or data == b"close":
                print("Got termination signal", data, "and closed connection")
                conn.close()

            # Get message and revert it and send it back
            data = str(data.decode("utf-8"))
            one_list = re.split(' ', data)
            code = re.split('=', one_list[1])
            sorce_ip = str(addr)
            try:
                resp_status = HTTPStatus(int(code[1])).phrase
                print("Request Method: " + one_list[0] + " Request Source:" + sorce_ip +
                      " Response Status: " + code[1] + HTTPStatus(int(code[1])).phrase +
                      " User-Agent:" + one_list[14], one_list[14], one_list[14], one_list[14])
            except ValueError:
                print("Request Method: " + one_list[0] + " Request Source:" + sorce_ip +
                      " Response Status: 200 OK User-Agent:" + one_list[14], one_list[14], one_list[14], one_list[14])