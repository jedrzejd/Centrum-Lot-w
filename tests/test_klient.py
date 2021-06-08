from klient import Klient


def test_create_klient():
    klient = Klient('123')

    assert isinstance(klient, Klient)


def test_getID_klineta():
    klient = Klient('123')
    id_klient = klient.getId()

    assert id_klient == '123'
