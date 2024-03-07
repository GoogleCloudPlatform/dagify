class OutCondition():
    name = None
    odate = None
    sign = None
    
    def __init__(self, name=None, odate=None, sign=None):
        self.name = name
        self.odate = odate
        self.sign = sign
    
    def setName(self, name):
        self.name = name
        
    def setOdate(self, odate):
        self.odate = odate
    
    def setSign(self, sign):
        self.sign = sign
        
    def getName(self):
        return self.name
    
    def getOdate(self):
        return self.odate
    
    def getSign(self):
        return self.sign