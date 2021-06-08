from klient import Klient
from trasa import Trasa
from lot import Lot
from samolot import Samolot
from datetime import datetime
import pandas as pd


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

    def dodajKlienta(self, klient: Klient):
        self.__klienci.append(klient)

    def usunKlienta(self, klient: Klient):
        self.__klienci.remove(klient)

    def dodajSamolot(self, samolot: Samolot):
        self.__samoloty.append(samolot)

    def usunSamolot(self, samolot: Samolot):
        self.__samoloty.remove(samolot)

    def dodajTrase(self, trasa: Trasa):
        self.__trasy.append(trasa)

    def usunTrase(self, trasa: Trasa):
        self.__trasy.remove(trasa)

    def generujLot(self, samolot: Samolot, trasa: Trasa, listaRezerwacji: list, rodzajLotu: str):
        self.__loty.append(samolot, trasa, listaRezerwacji, rodzajLotu)

    def zapis(self):
        # sam = self.getSamoloty()
        # sam_list = []
        # for x in sam:
        #     sam_id = x.getId()
        #     sam_Zasieg = x.getZasieg()
        #     sam_Liczbamiejsc = x.getLiczbamiejsc()
        #     sam_list.append([sam_id, sam_Zasieg, sam_Liczbamiejsc])
        # csv_samoloty = pd.DataFrame(sam_list)
        # csv_samoloty.to_csv('data/plik_samoloty.csv', index=False)
        #
        #
        # # loty = self.getLoty()
        # # loty_list = []
        # # for x in loty:
        # #     loty_id_Samolot = x.getSamolot().getId()
        # #     loty_rezerwacje = x.getRezerwacje()
        # #     loty_id_trasy = x.getTrasa().getId()
        # #     loty_rodzaj = x.getRodzajLotu()
        # #     loty_list.append([loty_id_Samolot, loty_rezerwacje, loty_id_trasy, loty_rodzaj])
        # # csv_loty = pd.DataFrame(loty_list)
        # # print(csv_loty)
        # # csv_loty.to_csv('data/plik_loty.csv', index=False)
        #
        # trasy = self.getSamoloty()
        # trasy_list = []
        # for x in sam:
        #     sam_id = x.getId()
        #     sam_Zasieg = x.getZasieg()
        #     sam_Liczbamiejsc = x.getLiczbamiejsc()
        #     sam_list.append([sam_id, sam_Zasieg, sam_Liczbamiejsc])
        # csv_trasy = pd.DataFrame(sam_list)
        # csv_trasy.to_csv('data/plik_trasy.csv', index=False)
        #
        # __plik_trasy = 'data/plik_trasy.csv'
        # __plik_klienci = 'data/plik_klienci.csv'


    def odczyt(self):
        csv_samoloty = pd.read_csv(self.__plik_samoloty)
        csv_loty = pd.read_csv(self.__plik_loty)
        csv_trasy = pd.read_csv(self.__plik_trasy)
        csv_klienci = pd.read_csv(self.__plik_klienci)



lotnisko = Linialotnicza('Lot', [Samolot(12.3, '12', 34)], [], [], [])
lotnisko.zapis()