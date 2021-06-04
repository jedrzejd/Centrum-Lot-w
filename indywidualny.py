from klient import Klient


class Indywidualny(Klient):
    def __init__(self, id, imie, nazwisko, narodowość, wiek):
        super().__init__(id)
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__narodowosc = narodowość
        self.__wiek = wiek

    def getImie(self):
        return self.__imie

    def getNazwisko(self):
        return self.__nazwisko

    def getNarodowosc(self):
        return self.__narodowosc

    @property
    def wiek(self):
        return self.__wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        self.__wiek = nowy_wiek