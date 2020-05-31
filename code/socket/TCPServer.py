import socket

host = "127.0.0.1"
port = 12345
addr = (host, port)
serverListenCount = 5

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(serverListenCount)

while True:
    print("正在等待客户端接入...")
    clientSock, clientAddr = tcpServer.accept()
    print("客户端连接成功，地址为：", clientAddr)
    while True:
        recvDatas = clientSock.recv(2048)
        if not recvDatas:
            break
        print(recvDatas.decode())
        response = "hello client, I have received you data: " + recvDatas.decode()
        clientSock.send(response.encode())
    clientSock.close()
tcpServer.close()


