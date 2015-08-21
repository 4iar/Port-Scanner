from port_scanner import ScanTechnique
import socket

class TCPFullConnect(ScanTechnique):

    def __init__(self, target):
        super(TCPFullConnectScan, self).__init__(target)
        self.name = "TCP Full Connect"
        self.description = "soon"

    def start(self):
        self.in_progress = True
        for p in self.target.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.target.ip_address, p))
            except:  # add more advanced error handling - not all errors mean s is closed
                self.target.results[p] = "closed"
            else:
                self.target.results[p] = "open"

        self.in_progress = False

    def stop(self):
        self.in_progress = False
