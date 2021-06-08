from linialotnicza import Linialotnicza
from samolot import Samolot
from lot import Lot
from klient import Klient
from rezerwacja import Rezerwacja
from datetime import datetime
from bilet import Bilet
from trasa import Trasa
from lotnisko import Lotnisko


def test_create_linialotnicza():

    samolot = Samolot(1500.5,'ASI',120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    lotnisko_3 = Lotnisko('Jemen', 'Baku', 'ABAF1247')
    trasa_1 = Trasa(1167.98, 10.5, [lotnisko_3, lotnisko_2],1)
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    trasa_3 = Trasa(936.61, 15.2, [lotnisko_1, lotnisko_3],3)
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_2 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    rezerwacja_3 = Rezerwacja(klient_2, [bilet_2_2])
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    lot_2 = Lot(samolot, trasa_3, [rezerwacja_1, rezerwacja_3], 0)

    linialotnicza = Linialotnicza('Lataj z Nami',[samolot], [lot], [trasa_2], [klient_1])
    linialotnicza_2 = Linialotnicza('W chmurach',[samolot],[lot_2],[trasa_1],[klient_2])

    assert isinstance(linialotnicza,Linialotnicza)
    assert isinstance(linialotnicza_2,Linialotnicza)


def test_getNazwaLinii():

    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    nazwalinii=linialotnicza.getNazwaLinii()

    assert nazwalinii=='Lataj z Nami'


def test_getSamoloty():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    samoloty = linialotnicza.getSamoloty()

    assert samoloty[0] == samolot


def test_getLoty():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    loty = linialotnicza.getLoty()

    assert loty[0]== lot


def test_getTrasy():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    trasy = linialotnicza.getTrasy()

    assert trasy[0] == trasa_2


def test_getKlienci():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    klienci = linialotnicza.getKlienci()

    assert klienci[0]==klient_1


def test_dodajKlienta():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1])

    linialotnicza.dodajKlienta(klient_2)
    klienci=linialotnicza.getKlienci()
    ostatniklient=klient_2.getId()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatniklient == 'md_987'


def test_usunKlienta():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1,klient_2])

    linialotnicza.usunKlienta(klient_2)
    klienci=linialotnicza.getKlienci()
    ostatniklient=klient_1.getId()

    assert isinstance(linialotnicza,Linialotnicza)
    assert len(klienci) == 1
    assert ostatniklient == 'jd_123'


def test_dodaj_Samolot():
    samolot = Samolot(1500.5, 'ASI', 120)
    samolot_2 = Samolot(2000.1, 'BAS', 60)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1,klient_2])

    linialotnicza.dodajSamolot(samolot_2)
    samolot = linialotnicza.getSamoloty()
    ostatniksamolot = samolot[-1].getId()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatniksamolot == 'BAS'

def test_dodaj_usun_Samolot():
    samolot = Samolot(1500.5, 'ASI', 120)
    samolot_2 = Samolot(2000.1, 'BAS', 60)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1,klient_2])

    linialotnicza.dodajSamolot(samolot_2)
    linialotnicza.usunSamolot(samolot)
    samolot = linialotnicza.getSamoloty()
    ostatniksamolot = samolot[0].getId()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatniksamolot == 'BAS'


def test_dodaj_Trasa():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    lotnisko_3 = Lotnisko('Jemen', 'Baku', 'ABAF1247')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    trasa_3 = Trasa(633.2, 7, [lotnisko_3, lotnisko_2],3)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1,klient_2])

    linialotnicza.dodajTrase(trasa_3)
    trasy = linialotnicza.getTrasy()
    ostatniatrasa = trasy[-1].getID()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatniatrasa == 3


def test_dodaj_usunTrasa():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    lotnisko_3 = Lotnisko('Jemen', 'Baku', 'ABAF1247')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2],2)
    trasa_3 = Trasa(633.2, 7, [lotnisko_3, lotnisko_2],3)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1,klient_2])

    linialotnicza.dodajTrase(trasa_3)
    linialotnicza.usunTrase(trasa_2)

    trasy = linialotnicza.getTrasy()
    ostatniatrasa = trasy[0].getID()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatniatrasa == 3


def test_generowanieLotu():
    samolot = Samolot(1500.5, 'ASI', 120)
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    lotnisko_3 = Lotnisko('Jemen', 'Baku', 'ABAF1247')
    klient_1 = Klient('jd_123')
    klient_2 = Klient('md_987')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021, 1, 2))
    rezerwacja_1 = Rezerwacja(klient_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klient_2, [bilet_2_1])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2], 2)
    trasa_3 = Trasa(633.2, 7, [lotnisko_3, lotnisko_2], 3)
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
    linialotnicza = Linialotnicza('Lataj z Nami', [samolot], [lot], [trasa_2], [klient_1, klient_2])

    linialotnicza.generujLot(samolot,trasa_3,[rezerwacja_1,rezerwacja_2],1)

    loty=linialotnicza.getLoty()
    ostatnilot=loty[-1].getRodzajLotu()

    assert isinstance(linialotnicza,Linialotnicza)
    assert ostatnilot == 1


# from linialotnicza import Linialotnicza
#
# def test_create_linialotnicza():
#     linialotnicza = Linialotnicza('Lot')
#
#     assert isinstance(linialotnicza,Linialotnicza)
#
# def