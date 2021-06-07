from klient import Klient
from bilet import Bilet


class Rezerwacja:
    def __init__(self, klient, bilety):
        self.__klient = klient
        self.__bilety = bilety

    def getKlient(self):
        return self.__klient

    def getBilety(self):
        return self.__bilety

    def dodajBilety(self, bilet: Bilet):
        self.__bilety.append(bilet)

    def usunBilet(self, bilet: Bilet):
        self.__bilety.remove(bilet)