class Workflow: 
    folders = []

    def __init__(self, filename):
        self.filename = filename
        self.folders = []

    def addFolder(self, folder):
        self.folders.append(folder)
    
    def getFolders(self):
        return self.folders
    
    def getFolderCount(self):
        return len(self.folders)
    