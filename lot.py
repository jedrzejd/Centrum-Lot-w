from trasa import Trasa
from rezerwacja import Rezerwacja
from samolot import Samolot


class Lot:
    def __init__(self, samolot: Samolot, trasa: Trasa, listaRezerwacji: list, rodzajLotu: str):
        self.__trasa = trasa
        self.__listaRezerwacji = listaRezerwacji
        self.__rodzajLotu = rodzajLotu
        self.__samolot = samolot

    def getRezerwacje(self):
        return self.__listaRezerwacji

    def getSamolot(self):
        return self.__samolot

    def getTrasa(self):
        return self.__trasa

    def dodajRezerwacje(self, rezerwacja: Rezerwacja):
        self.__listaRezerwacji.append(rezerwacja)

    def usunRezerwacje(self, rezerwacja: Rezerwacja):
        self.__listaRezerwacji.remove(rezerwacja)

    def getRodzajLotu(self):
        return self.__rodzajLotu