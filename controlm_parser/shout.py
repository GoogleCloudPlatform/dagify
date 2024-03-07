class Shout():
    when = None
    urgency = None
    dest = None
    message = None
    
    def __init__(self, when=None, urgency=None, dest=None, message=None):
        self.when = when
        self.urgency = urgency
        self.dest = dest
        self.message = message
    
    def setWhen(self, when):
        self.when = when
    
    def setUrgency(self, urgency):
        self.urgency = urgency
    
    def setDest(self, dest):
        self.dest = dest
    
    def setMessage(self, message):
        self.message = message
    
    def getWhen(self):
        return self.when
    
    def getUrgency(self):
        return self.urgency
    
    def getDest(self):
        return self.dest
    
    def getMessage(self):
        return self.message
 
    