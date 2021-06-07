import array

from trasa import Trasa, Lotnisko


def test_create_trasa():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    trasa = Trasa(123.98, 12.5, [lotnisko])

    assert isinstance(trasa, Trasa)


def test_getDystans_trasy():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    trasa = Trasa(123.98, 12.5, [lotnisko])

    dystans_trasy = trasa.getDystans()

    assert isinstance(trasa, Trasa)
    assert isinstance(dystans_trasy, float)
    assert dystans_trasy == 123.98


def test_getLotniska_trasy():
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Polska', 'Bialystok', 'ASBV4411')
    trasa = Trasa(123.98, 12.5, [lotnisko_1, lotnisko_2])

    lotniska = trasa.getLotniska()

    assert isinstance(trasa, Trasa)
    assert isinstance(lotniska, list)
    assert isinstance(lotniska[0], Lotnisko)
    assert isinstance(lotniska[1], Lotnisko)
    assert lotniska[0].getKraj() == 'Japonia'
    assert lotniska[1].getKraj() == 'Polska'
    assert lotniska[0].getMiasto() == 'Baku'
    assert lotniska[1].getMiasto() == 'Bialystok'
    assert lotniska[0].getId() == 'FSFJU123'
    assert lotniska[1].getId() == 'ASBV4411'


def test_dodajLotnisko_trasy():
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Polska', 'Bialystok', 'ASBV4411')
    trasa = Trasa(123.98, 12.5, [lotnisko_1])

    trasa.dodajLotnisko(lotnisko_2)
    lotniska = trasa.getLotniska()

    assert isinstance(trasa, Trasa)
    assert isinstance(lotniska, list)
    assert isinstance(lotniska[0], Lotnisko)
    assert isinstance(lotniska[1], Lotnisko)
    assert lotniska[0].getKraj() == 'Japonia'
    assert lotniska[1].getKraj() == 'Polska'
    assert lotniska[0].getMiasto() == 'Baku'
    assert lotniska[1].getMiasto() == 'Bialystok'
    assert lotniska[0].getId() == 'FSFJU123'
    assert lotniska[1].getId() == 'ASBV4411'


def test_usunLotnisko_trasy():
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    lotnisko_2 = Lotnisko('Polska', 'Bialystok', 'ASBV4411')
    trasa = Trasa(123.98, 12.5, [lotnisko_1, lotnisko_2])

    trasa.usunLotnisko()
    lotniska = trasa.getLotniska()

    assert isinstance(trasa, Trasa)
    assert isinstance(lotniska[0], Lotnisko)
    assert lotniska[0].getKraj() == 'Japonia'
    assert lotniska[0].getMiasto() == 'Baku'
    assert lotniska[0].getId() == 'FSFJU123'


def test_getCzas_trasy():
    lotnisko_1 = Lotnisko('Japonia', 'Baku', 'FSFJU123')
    trasa = Trasa(123.98, 12.5, [lotnisko_1])

    czas_lotniska = trasa.getCzas()

    assert isinstance(trasa, Trasa)
    assert isinstance(czas_lotniska, float)