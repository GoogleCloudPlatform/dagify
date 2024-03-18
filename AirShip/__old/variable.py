class Variable():
    name = None
    value = None

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value
