from lotnisko import Lotnisko


class Samolot:
    def __init__(self, zasieg:float, id:str, liczbamiejsc:int):
        self.__zasieg = zasieg
        self.__id = id
        self.__liczbamiejsc = liczbamiejsc
    def getZasieg(self):
        return self.__zasieg
    def getId(self):
        return self.__id
    def getLiczbamiejsc(self):
        return self.__liczbamiejsc

