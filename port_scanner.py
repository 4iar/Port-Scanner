

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

    def __init__(self):
        pass


class Target(object):
    """The server to scan against

    Attributes:
        ip (str): IPv4 address of the target
        ports (int list): list of ports to scan against
        results (dict): dict of results in the format port:state
    """

    def __init__(self):
        pass

class ScanTechnique(object):
    """Scan technique to use against the target

    Attributes:
        target (Target): server to scan against
        name (str): name of the scan technqiue
        description (str): a description of how the scan technique works
    """

    def __init__(self, target):
        pass

