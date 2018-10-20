class Executer:
    def __init__(self, tcpServer):
        self.andRaspTCP = tcpServer
 
    def startCommand(self, command):
        if command != None:
            self.andRaspTCP.sendAll(command)
        else:
            pass