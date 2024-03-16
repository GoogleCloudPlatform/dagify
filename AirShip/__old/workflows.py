class Workflow:
    folders = []

    def __init__(self, filename):
        self.filename = filename
        self.folders = []

    def add_folder(self, folder):
        self.folders.append(folder)

    def get_folders(self):
        return self.folders

    def getFolderCount(self):
        return len(self.folders)
