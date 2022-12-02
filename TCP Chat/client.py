import socket
ip = "127.0.0.1"
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip,port))

while True:
    string = input ("Client : ")
    server.send(bytes(string,'utf-8'))
    response = server.recv(1024).decode("utf-8")
    if string == "quit":
        break
    print(f'Server : {response}')