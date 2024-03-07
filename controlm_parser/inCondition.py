class InCondition():
    name = None
    odate = None
    andOr = None
    
    def __init__(self, name=None, odate=None, andOr=None):
        self.name = name
        self.odate = odate
        self.andOr = andOr
    
    def setName(self, name):
        self.name = name
        
    def setOdate(self, odate):
        self.odate = odate
    
    def setAndOr(self, andOr):
        self.andOr = andOr
        
    def getName(self):
        return self.name
    
    def getOdate(self):
        return self.odate
    
    def getAndOr(self):
        return self.andOr
        