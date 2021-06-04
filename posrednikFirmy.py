from klient import Klient


class PosrednikFirmy(Klient):
    def __init__(self, id: str, NazwaFirmy: str, NIP: str):
        super().__init__(id)
        self.__nazwaFirmy = NazwaFirmy
        self.__NIP = NIP

    def getNazwaFirmy(self):
        return self.__nazwaFirmy

    def getNIP(self):
        return self.__NIP