from datetime import datetime

from lot import Lot
from lotnisko import Lotnisko
from trasa import Trasa
from rezerwacja import Rezerwacja
from klient import Klient
from samolot import Samolot
from bilet import Bilet


def test_create_lot():
    samolot = Samolot(1500, 'JAKUWA', 120)

    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
    lotnisko_3 = Lotnisko('Jemen', 'Baku', 'ABAF1247')

    trasa_1 = Trasa(1167.98, 10.5, [lotnisko_3, lotnisko_2])
    trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2])
    trasa_3 = Trasa(936.61, 15.2, [lotnisko_1, lotnisko_3])

    klinet_1 = Klient('jd_123')
    bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021,1,2))

    klinet_2 = Klient('ja_412')
    bilet_2_1 = Bilet('Jemen', 'Filipiny', datetime(2021,1,2))
    bilet_2_2 = Bilet('Japonia', 'Filipiny', datetime(2021,1,2))

    rezerwacja_1 = Rezerwacja(klinet_1, [bilet_1_1])
    rezerwacja_2 = Rezerwacja(klinet_2, [bilet_2_2])
    lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)

    assert isinstance(lot, Lot)


# def test_getRezerwacje():
#     samolot = Samolot(1500, 'JAKUWA', 120)
#
#     lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
#     lotnisko_2 = Lotnisko('Filipiny', 'Ramzes', 'AVIZ652')
#
#     trasa_2 = Trasa(1233.2, 12, [lotnisko_1, lotnisko_2])
#
#     klinet_1 = Klient('jd_123')
#     bilet_1_1 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
#
#     klinet_2 = Klient('ja_412')
#     bilet_2_2 = Bilet('Japonia', 'Filipiny', datetime(2021, 1, 2))
#
#     rezerwacja_1 = Rezerwacja(klinet_1, [bilet_1_1])
#     rezerwacja_2 = Rezerwacja(klinet_2, [bilet_2_2])
#     lot = Lot(samolot, trasa_2, [rezerwacja_1, rezerwacja_2], 0)
#
#
#     rezerwacje = lot.getRezerwacje()
#
#
#     assert isinstance(lot, Lot)
#     assert isinstance(rezerwacje, list)
