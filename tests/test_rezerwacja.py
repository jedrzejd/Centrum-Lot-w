from datetime import datetime

from rezerwacja import Rezerwacja, Klient, Bilet

from indywidualny import Indywidualny
from posrednikFirmy import PosrednikFirmy


def test_create_rezerwacja():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)

    assert isinstance(rezerwacja, Rezerwacja)


def test_getKlient():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)

    klient = rezerwacja.getKlient()
    id_klienta = klient.getId()

    assert isinstance(rezerwacja, Rezerwacja)
    assert isinstance(klient, Klient)
    assert id_klienta == 'jd_123'


def test_getPosrednikFirmy():

    klinet_indywidualny = PosrednikFirmy('AZDVD12', 'Azabrasz', '123452518')
    rezerwacja = Rezerwacja(klinet_indywidualny)

    klient = rezerwacja.getKlient()
    id_klienta = klient.getId()
    nazwa_firmy_klienta = klient.getNazwaFirmy()
    nip_firmy_klienta = klient.getNIP()

    assert isinstance(rezerwacja, Rezerwacja)
    assert isinstance(klient, Klient)
    assert id_klienta =='AZDVD12'
    assert nazwa_firmy_klienta == 'Azabrasz'
    assert nip_firmy_klienta == '123452518'


def test_getKlientIndywidualny():

    klinet_indywidualny = Indywidualny('jd_123', 'Jerzy', 'Pawian', 'Poznanian', 53)
    rezerwacja = Rezerwacja(klinet_indywidualny)

    klient = rezerwacja.getKlient()
    id_klienta = klient.getId()
    imie_klienta = klient.getImie()
    nazwisko_klienta = klient.getNazwisko()
    narodowosc_klienta = klient.getNarodowosc()
    wiek_klienta = klient.wiek

    assert isinstance(rezerwacja, Rezerwacja)
    assert isinstance(klient, Klient)
    assert id_klienta =='jd_123'
    assert imie_klienta == 'Jerzy'
    assert nazwisko_klienta == 'Pawian'
    assert narodowosc_klienta == 'Poznanian'
    assert wiek_klienta == 53


def test_getBilety_and_dodajBilety():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)
    bilet = Bilet('Polska', 'Rosja', datetime(2021, 1, 22))

    rezerwacja.dodajBilety(bilet)
    bilety = rezerwacja.getBilety()

    assert isinstance(rezerwacja, Rezerwacja)
    assert len(bilety) == 1
    assert isinstance(bilety[-1], Bilet)
    assert bilety[-1].getMiejsceDocelowe() == 'Rosja'
    assert bilety[-1].getMiejsceOdlotu() == 'Polska'
    assert bilety[-1].getData() == datetime(2021, 1, 22)


def test_getBilety_and_dodajBilety_and_usunBilet():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)
    bilet_0 = Bilet('Francja', 'Usa', datetime(2023, 2, 3))
    bilet_1 = Bilet('Polska', 'Rosja', datetime(2021, 1, 22))
    bilet_2 = Bilet('Baku', 'Wlochy', datetime(2022, 5, 11))
    rezerwacja.dodajBilety(bilet_0)
    rezerwacja.dodajBilety(bilet_1)
    rezerwacja.dodajBilety(bilet_2)

    rezerwacja.usunBilet(bilet_1)
    rezerwacja.usunBilet(bilet_2)
    bilety = rezerwacja.getBilety()

    assert isinstance(rezerwacja, Rezerwacja)
    assert len(bilety) == 1
    assert isinstance(bilety[0], Bilet)
    assert bilety[-1].getMiejsceDocelowe() == 'Usa'
    assert bilety[-1].getMiejsceOdlotu() == 'Francja'
    assert bilety[-1].getData() == datetime(2023, 2, 3)
