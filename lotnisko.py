class Lotnisko:
    def __init__(self, kraj: str, miasto: str, id: str):
        self.__kraj = kraj
        self.__miasto = miasto
        self.__id = id

    def getKraj(self):
        return self.__kraj

    def getMiasto(self):
        return self.__miasto

    def getId(self):
        return self.__id


