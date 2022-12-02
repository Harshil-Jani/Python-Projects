import socket
ip = "127.0.0.1"
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)

while True: 
    client, address = server.accept()
    print("Connected")
    while True:
        message = client.recv(1024).decode("utf-8")
        print(f'Client {address[1]} : {message}')
        if message == "quit":
            break
        else:
            response = input("Server : ")
            client.send(response.encode())
    print("Closing the Server")
    break