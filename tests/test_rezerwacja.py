from datetime import datetime

from rezerwacja import Rezerwacja, Klient, Bilet


def test_create_rezerwacja():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)

    assert isinstance(rezerwacja, Rezerwacja)


def test_getKlient():
    klinet = Klient('jd_123')
    rezerwacja = Rezerwacja(klinet)

    id_klienta = rezerwacja.getKlient()

    assert isinstance(rezerwacja, Rezerwacja)
    assert isinstance(id_klienta, Klient)
    assert id_klienta.getId() == Klient('jd_123').getId()


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

    rezerwacja.usunBilet()
    rezerwacja.usunBilet()
    bilety = rezerwacja.getBilety()

    assert isinstance(rezerwacja, Rezerwacja)
    assert len(bilety) == 1
    assert isinstance(bilety[0], Bilet)
    assert bilety[-1].getMiejsceDocelowe() == 'Usa'
    assert bilety[-1].getMiejsceOdlotu() == 'Francja'
    assert bilety[-1].getData() == datetime(2023, 2, 3)
