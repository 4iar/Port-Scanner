class ScanTechnique(object):
    """Scan technique to use against the target

    Attributes:
        target (Target): server to scan against
        name (str): name of the scan technqiue
        description (str): a description of how the scan technique works
    """

    def __init__(self, target):
        self.target = target
        self.name = "Name of scan"
        self.description = "Description of scan"
        self.in_progress = False

    def start(self):
        pass

    def stop(self):
        pass
