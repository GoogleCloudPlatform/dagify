class Config():
    
    converters = {
        "CONTROLM": {
            "id": "CONTROLM",
            "enabled": True,
            "name": "Control-M",
            "description": "Control-M (BCM Software)",
        },
        "UC4": {
            "id": "UC4",
            "enabled": False,
            "name": "UC4",
            "description": "UC4 (Automic)",
        }
    }
    
    def __init__(self):
        pass
    
    def getConverters(self): 
        return self.converters