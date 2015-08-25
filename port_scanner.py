import socket
from scan_techniques.tcp_full_connect import ScanTechnique, TCPFullConnect


class PortScanner(object):
    """Main Port scanner --- give me a better name

    Attributes:
        scan_techniques (ScanTechnique list): a list of all the available scan techniques
        scan_queue (Scan list): a list of all the scans to process or that have been completed

    """

    def __init__(self):
        self.scan_techniques = [TCPFullConnect]
        self.scan_queue = []

    def enqueue_scan(self, target, scan_technique):
        """Add a scan to the queue of pending scans"""
        self.scan_queue.append(Scan(target, scan_technique))

    def process_scan_queue(self):  # implement multithreading here?
        """Start processing scans in the queue"""
        for scan in self.scan_queue:
            scan.start()


class Scan(object):
    """Port scan

    Attributes:
        target (Target): target server to scan against
        scan_technique (ScanTechnique): scan technique to use against target
    """

    def __init__(self, target, scan_technique):
        self.scan_technique = scan_technique(target)

    def start(self):
        """Start scanning"""
        self.scan_technique.start()

    def stop(self):
        """Stop scanning"""
        self.scan_technique.stop()

    @property
    def results(self):
        """Get scan results"""
        return self.scan_technique.target.results

    @property
    def in_progress(self):
        """Get state of scan"""
        return self.scan_technique.in_progress



class Target(object):
    """The server to scan against

    Attributes:
        ip (str): IPv4 address of the target
        ports (int list): list of ports to scan against
        results (dict): dict of results in the format port:state
    """

    def __init__(self, host, ports):
        self.ip_address = self.translate(host)
        self.ports = ports
        self.results = {p: None for p in self.ports}



class Port(int):
    """Port"""

    def __init__(self, port):
        if not isinstance(port, int):
            raise TypeError("Expected int for port")
        if port > 65535:
            raise ValueError("Port number cannot exceed 65535")
        if port < 1:
            raise ValueError("Port number cannot be less than 1")

        super(int).__init__(int, port)



class Host(str):
    """Host"""

    def __new__(self, hostname):
        return super().__new__(str, self.translate(hostname))

    @classmethod  # allows access to method before the object is set up
    def translate(self, host):
        """Translate a hostname into an IPv4 address

        Translate the given hostname into an IPv4 address
        or keep the hostname the same if it is already an
        IPv4 address.

        Args:
            host (str): the hostname to translate
        Returns:
            ip (str): IPv4 address of the hostname
        Raises:
            socket.gaierror: hostname is invalid
        """

        try:
            ip = socket.gethostbyname(host)
        except socket.gaierror:
            raise

        return ip
