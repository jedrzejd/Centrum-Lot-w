from lotnisko import Lotnisko


class Trasa:
    def __init__(self, dystans: float, czas: float, lotniska: list, id: str):
        self.__dystans = dystans
        self.__czas = czas
        self.__lotniska = lotniska
        self.__id = id

    def getDystans(self):
        return self.__dystans

    def getLotniska(self):
        return self.__lotniska

    def dodajLotnisko(self, lotnisko: Lotnisko):
        self.__lotniska.append(lotnisko)

    def usunLotnisko(self):
        self.__lotniska.pop()

    def getCzas(self):
        return self.__czas

    def getID(self):
        return self.__id