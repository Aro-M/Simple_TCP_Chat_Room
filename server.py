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
            broad_cast(f"f {nick_name} left the chat".encode('ascii'))
            nick_names.remove(nick_name)
            break

def receive():
    while True:
        client ,address = server.accept()
        print(f'Connected with {str(address)}')

        client.send("Nick".encode('ascii'))
        nick_name = client.recv(1024).decode('ascii')
        nick_names.append(nick_name)
        clients.append(client)

        print(f"Nickname of the client is {nick_name}")
        broad_cast(f" {nick_name} joined the chat ".encode('ascii'))
        client.send("Connected to the server!" .encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

print("Server is  listening...")
receive()