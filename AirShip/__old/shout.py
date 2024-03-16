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

    def set_when(self, when):
        self.when = when

    def set_urgency(self, urgency):
        self.urgency = urgency

    def set_dest(self, dest):
        self.dest = dest

    def set_message(self, message):
        self.message = message

    def get_when(self):
        return self.when

    def getUrgency(self):
        return self.urgency

    def get_dest(self):
        return self.dest

    def get_message(self):
        return self.message
