from lotnisko import Lotnisko

class Trasa:
    def __init__(self,dystans: float,czas: float, lotniska:list):
        self.dystans = dystans
        self.czas = czas
        self.lotniska = lotniska
    def getDystans(self):
        return self.dystans
    def getLotniska(self):
        return self.lotniska
    def dodajLotnisko(self,lotnisko:Lotnisko):
        self.__lotnisko.append(lotnisko)
    def usunLotnisko(self):
        self.__lotnisko.pop()
    def getCzas(self):
        return self.czas
