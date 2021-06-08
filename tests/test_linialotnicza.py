from linialotnicza import Linialotnicza

def test_create_linialotnicza():
    linialotnicza = Linialotnicza('Lot')

    assert isinstance(linialotnicza,Linialotnicza)

def