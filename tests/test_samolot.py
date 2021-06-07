from samolot import Samolot

def test_create_samolot():
    samolot = Samolot(150.0,'UHC64920',75)

    assert isinstance(samolot,Samolot)

def test_getZasieg_samolot():
    samolot = Samolot(150.0,'UHC64920',75)

    zasieg_samolot = samolot.getZasieg()

    assert isinstance(samolot, Samolot)
    assert isinstance(zasieg_samolot, float)
    assert zasieg_samolot == 150.0

def test_getId_samolot():
    samolot = Samolot(150.0, 'UHC64920', 75)

    id_samolot = samolot.getId()

    assert isinstance(samolot, Samolot)
    assert isinstance(id_samolot, str)
    assert id_samolot == 'UHC64920'

def test_getLiczbamiejsc():
    samolot = Samolot(150.0, 'UHC64920', 75)

    liczbamiejsc = samolot.getLiczbamiejsc()

    assert isinstance(samolot, Samolot)
    assert isinstance(liczbamiejsc, int)
    assert liczbamiejsc == 75
