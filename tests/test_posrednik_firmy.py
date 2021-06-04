from posrednikFirmy import PosrednikFirmy


def test_create_posrednik_firmy():
    posrednik_firmy = PosrednikFirmy('192', 'Fajna nazwa', '1923132')

    assert isinstance(posrednik_firmy, PosrednikFirmy)


def test_getID_posrednik_firmy():
    posrednik_firmy = PosrednikFirmy('192', 'Fajna nazwa', '1923132')

    id_klienta = posrednik_firmy.getId()

    assert isinstance(posrednik_firmy, PosrednikFirmy)
    assert isinstance(id_klienta, str)
    assert id_klienta == '192'


def test_getNazwaFirmy():
    posrednik_firmy = PosrednikFirmy('192', 'Fajna nazwa', '1923132')

    nazwa_firmy = posrednik_firmy.getNazwaFirmy()

    assert isinstance(posrednik_firmy, PosrednikFirmy)
    assert isinstance(nazwa_firmy, str)
    assert nazwa_firmy == 'Fajna nazwa'


def test_getNIP():
    posrednik_firmy = PosrednikFirmy('192', 'Fajna nazwa', '1923132')

    NIP_firmy = posrednik_firmy.getNIP()

    assert isinstance(posrednik_firmy, PosrednikFirmy)
    assert isinstance(NIP_firmy, str)
    assert NIP_firmy == '1923132'