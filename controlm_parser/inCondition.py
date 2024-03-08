class InCondition():
    name = None
    odate = None
    and_or = None

    def __init__(self, name=None, odate=None, and_or=None):
        self.name = name
        self.odate = odate
        self.and_or = and_or

    def set_name(self, name):
        self.name = name

    def set_odate(self, odate):
        self.odate = odate

    def set_and_or(self, and_or):
        self.and_or = and_or

    def get_name(self):
        return self.name

    def get_odate(self):
        return self.odate

    def get_and_or(self):
        return self.and_or
