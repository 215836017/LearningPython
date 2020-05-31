import socket

host = "127.0.0.1"
port  = 12345
addr = (host, port)

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpClient.sendto("hi, I am udpClient".encode(), addr)


# Yellowbrick -- 可视化诊断工具集
