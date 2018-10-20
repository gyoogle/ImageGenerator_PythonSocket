# Server main file

import tcpServer

andRaspTCP = tcpServer.TCPServer("", 5000)
andRaspTCP.start()