import socket
import  threading

nickname = input("Choose a nickname  ")

c_host = '127.0.0.1'
c_port = 55555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((c_host, c_port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if nickname == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Error occurred")
            client.close()
            break


def write():
    while True:
        message = f'{ nickname }{input("")}'
        client.send(message.encode('ascii'))






receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

