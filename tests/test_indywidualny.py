from indywidualny import Indywidualny


def test_create_indywidualny_klient():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    assert isinstance(indywidualny_klient, Indywidualny)


def test_getID_indywidualny_klien():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    id_klienta = indywidualny_klient.getId()

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(id_klienta, str)
    assert id_klienta == '1009'


def test_getImie():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    imie_klienta = indywidualny_klient.getImie()

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(imie_klienta, str)
    assert imie_klienta == 'Janusz'


def test_getNazwisko():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    nazwisko_klienta = indywidualny_klient.getNazwisko()

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(nazwisko_klienta, str)
    assert nazwisko_klienta == 'Kowal'


def test_getNarodowosc():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    narodowosc_klienta = indywidualny_klient.getNarodowosc()

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(narodowosc_klienta, str)
    assert narodowosc_klienta == 'Uzbekistan'


def test_getWiek():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)

    wiek_kilenta = indywidualny_klient.wiek

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(wiek_kilenta, int)
    assert wiek_kilenta == 123


def test_setWiek():
    indywidualny_klient = Indywidualny('1009', 'Janusz', 'Kowal', 'Uzbekistan', 123)
    indywidualny_klient.wiek = 15

    wiek_kilenta = indywidualny_klient.wiek

    assert isinstance(indywidualny_klient, Indywidualny)
    assert isinstance(wiek_kilenta, int)
    assert wiek_kilenta == 15