import threading
import socket
# from queue import Queue

target = "127.0.0.1"
# queue = Queue()
# open_ports = []

def portscan(port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((target,port))
        return True
    except: 
        return False

for port in range(0,9000):
    result = portscan(port)
    if result:
        print(f'Port {port} is open')

# def fill_queue(port_list):
#     for port in port_list:
#         queue.put(port)

# def worker():
#     while not queue.empty():
#         port = queue.get()
#         if portscan(port):
#             print(f'Port {port} is open')
#             open_ports.append(port)

# port_list = range(1,1024)
# fill_queue(port_list)

# thread_list = []
# for t in range(10):
#     thread = threading.Thread(target=worker)
#     thread_list.append(thread)

# for thread in thread_list:
#     thread.start()

# for thread in thread_list:
#     thread.join()

# print("Open ports are : ",open_ports)