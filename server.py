import socket
import threading

c_host = '127.0.0.1'  #localhost
c_port = 55555      # port

# Now you will ask, did I write like this?
# Because they are constant objects

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((c_host, c_port))
server.listen()

clients = []
nick_names = []


def broad_cast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broad_cast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick_name = nick_names[index]
            nick_names.remove(nick_name)

