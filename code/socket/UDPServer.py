import socket
import logging
from utils.Logger import Logger

logyyx = Logger('yyx.log',logging.DEBUG,logging.DEBUG)
# Logutil = logging.getLogger("testLog")
# Logutil.basicConfig(level=Logutil.WARNING,
#                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S')
# Logutil.setLevel(logging.INFO)

host = "127.0.0.1"
port  = 12345
addr = (host, port)

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(addr)
# udpServer.settimeout(3)
print("server is recving...")
logyyx.info("server is recving...")
recvData = udpServer.recv(1024)
print("in udpServer, recvData is:",recvData.decode())
logyyx.debug("in udpServer, recvData is:" + recvData.decode())
