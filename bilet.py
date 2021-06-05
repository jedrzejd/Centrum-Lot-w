from datetime import datetime


class Bilet:
    def __init__(self, miejsceOdlotu: str, miejsceDocelowe: str, data: datetime):
        self.__miejsceOdlotu = miejsceOdlotu
        self.__miejsceDocelowe = miejsceDocelowe
        self.__data = data

    def getMiejsceDocelowe(self):
        return self.__miejsceDocelowe

    def getMiejsceOdlotu(self):
        return self.__miejsceOdlotu

    def getData(self):
        return self.__data