class Lotnisko:
    def __init__(self, kraj: str, miasto: str, id: str):
        self.kraj = kraj
        self.miasto = miasto
        self.id = id
    def getKraj(self):
        return self.kraj
    def getMiasto(self):
        return self.miasto
    def getId(self):
        return self.id


