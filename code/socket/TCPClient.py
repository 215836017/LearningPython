import socket

host = "127.0.0.1"
port = 12345
addr = (host, port)
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSock.connect(addr)
while True:
    msg = input("please input:")
    if not msg:
        break
    clientSock.send(msg.encode())
    recvData = clientSock.recv(2048)
    if recvData:
        print("recvData:", recvData.decode())
clientSock.close()