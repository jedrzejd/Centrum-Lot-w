from datetime import datetime

from bilet import Bilet


def test_create_bilet():
    bilet = Bilet('Japonia', 'Polska', datetime(2021,12,1))

    assert isinstance(bilet, Bilet)


def test_getMiejsceOdlotu():
    bilet = Bilet('Japonia', 'Polska', datetime(2021,12,1))

    miejsceOdlotu = bilet.getMiejsceOdlotu()

    assert isinstance(bilet, Bilet)
    assert isinstance(miejsceOdlotu, str)
    assert miejsceOdlotu == 'Japonia'


def test_getMiejsceDocelowe():
    bilet = Bilet('Japonia', 'Polska', datetime(2021,12,1))

    miejsceDocelowe = bilet.getMiejsceDocelowe()

    assert isinstance(bilet, Bilet)
    assert isinstance(miejsceDocelowe, str)
    assert miejsceDocelowe == 'Polska'


def test_getData():
    bilet = Bilet('Japonia', 'Polska', datetime(2021,12,1))

    data = bilet.getData()

    assert isinstance(bilet, Bilet)
    assert isinstance(data, datetime)
    assert data == datetime(2021,12,1)