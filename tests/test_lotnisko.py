from lotnisko import Lotnisko


def test_create_lotnisko():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')

    assert isinstance(lotnisko, Lotnisko)


def test_getKraj_lotniska():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')

    kraj_lotniska = lotnisko.getKraj()

    assert isinstance(lotnisko, Lotnisko)
    assert isinstance(kraj_lotniska, str)
    assert kraj_lotniska == 'Japonia'


def test_getMiasto_lotniska():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')

    misato_lotniska = lotnisko.getMiasto()

    assert isinstance(lotnisko, Lotnisko)
    assert isinstance(misato_lotniska, str)
    assert misato_lotniska == 'Baku'


def test_getID_lotniska():
    lotnisko = Lotnisko('Japonia', 'Baku', 'FSFJU123')

    id_lotniska = lotnisko.getId()

    assert isinstance(lotnisko, Lotnisko)
    assert isinstance(id_lotniska, str)
    assert id_lotniska == 'FSFJU123'