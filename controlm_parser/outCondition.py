class OutCondition():
    name = None
    odate = None
    sign = None
    
    def __init__(self, name=None, odate=None, sign=None):
        self.name = name
        self.odate = odate
        self.sign = sign
    
    def set_name(self, name):
        self.name = name
        
    def set_odate(self, odate):
        self.odate = odate
    
    def setSign(self, sign):
        self.sign = sign
        
    def get_name(self):
        return self.name
    
    def get_odate(self):
        return self.odate
    
    def getSign(self):
        return self.sign