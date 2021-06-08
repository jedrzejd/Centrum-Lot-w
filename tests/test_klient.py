from klient import Klient


def test_create_klient():
    klient = Klient('123')

    assert isinstance(klient, Klient)


def test_getID_klienta():
    klient = Klient('123')
    id_klient = klient.getId()

    assert id_klient == '123'
