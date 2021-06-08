from klient import Klient
from trasa import Trasa
from lot import Lot
from samolot import Samolot
from datetime import datetime


class Linialotnicza:
    def __init__(self, nazwalinii: str, samoloty, loty, trasy, klienci):
        self.__nazwalinii = nazwalinii
        self.__samoloty = samoloty
        self.__loty = loty
        self.__trasy = trasy
        self.__klienci = klienci

    def getNazwaLinii(self):
        return self.__nazwalinii

    def getSamoloty(self):
        return self.__samoloty

    def getLoty(self):
        return self.__loty

    def getTrasy(self):
        return self.__trasy

    def getKlienci(self):
        return self.__klienci

    def dodajKlienta(self,klient: Klient):
        self.__klienci.append(klient)

    def usunKlienta(self,klient: Klient):
        self.__klienci.pop(klient)

    def dodajSamolot(self,samolot: Samolot):
        self.__samoloty.append(samolot)

    def usunSamolot(self,samolot: Samolot):
        self.__samoloty.pop(samolot)

    def dodajTrase(self,trasa: Trasa):
        self.__trasy.append(trasa)

    def usunTrase(self,trasa: Trasa):
        self.__trasy.pop(trasa)

    def generujLot(self,samolot:Samolot,trasa: Trasa,listaRezerwacji: list,rodzajLotu: str):
        self.__loty.append(samolot,trasa,listaRezerwacji,rodzajLotu)

    def zapis(self):
        pass

    def odczyt(self):
        pass



