
class EventConfig(object): 
    def __init__(self):
        self.name = None 
        self.desc = None
        self.start = None 
        self.end = None
        self.rootDir = None    
        self.redFolder = None 
        self.blueFolder = None
        self.whiteFolder = None
        self.lead = None 
        self.leadIp = None 
        self.connections = None 
    
    def setName(self, name):
        self.name = name

    def setDesc(self, desc): 
        self.desc = desc

    def setStart(self, start): 
        self.start = start

    def setEnd(self, end): 
        self.end = end

    def setRootDir(self, rootDir): 
        self.rootDir = rootDir

    def setRed(self, red):
        self.redFolder = red

    def setBlue(self, blue): 
        self.blueFolder = blue

    def setWhite(self, white):
        self.whiteFolder = white

    def setLead(self, lead): 
        self.lead = lead

    def setLeadIp(self, ip):
        self.leadIp = ip

    def setConnections(self, conn):
        self.connections = conn     
    

    
