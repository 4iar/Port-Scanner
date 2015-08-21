import socket


class PortScanner(object):
    """Main Port scanner --- give me a better name

    Attributes:
        scan_techniques (ScanTechnique list): a list of all the available scan techniques

        --- think
    """

    def __init__(self):
        pass



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
        return self.scan_technique.results



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

class ScanTechnique(object):
    """Scan technique to use against the target

    Attributes:
        target (Target): server to scan against
        name (str): name of the scan technqiue
        description (str): a description of how the scan technique works
    """

    def __init__(self, target):
        self.results = "yay"
        pass

