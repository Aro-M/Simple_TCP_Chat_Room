import socket
import  threading

c_host = '127.0.0.1'
c_port = 55555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((c_host, c_port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                pass
            else:
                print(message)
        except:
            print("Error occurred")
            client.close()
            break