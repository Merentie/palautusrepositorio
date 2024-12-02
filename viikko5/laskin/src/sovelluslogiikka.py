class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset = [0]

    def miinus(self, operandi):
        self._edelliset.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edelliset.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edelliset.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._edelliset.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def edellinen(self):
        if self._edelliset == []:
            return
        self._arvo = self._edelliset[-1]
        self._edelliset.pop(-1)