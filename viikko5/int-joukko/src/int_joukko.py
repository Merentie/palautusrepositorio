KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, alkio):
        if alkio in self.lista:
            return True
        
        else:
            return False
        

    def lisaa(self, lisattava_alkio):
        if not self.kuuluu(lisattava_alkio):
            self.lista[self.alkioiden_lkm] = lisattava_alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.lista) == 0:
                self.luo_uusi_sailytuspaikka()
    
            return True
        
        else: 
            return False
        
    def luo_uusi_sailytuspaikka(self):
        vanha_lista = self.lista
        self.kopioi_lista(self.lista, vanha_lista)
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.lista)


    def poista(self, poistettava_alkio):
        poistetun_alkion_sijainti = self.poista_alkio_ja_palauta_sen_sijainti(poistettava_alkio)

        if poistetun_alkion_sijainti == None:
            return False # alkiota ei löytynyt listasta
        
        self.jarjesta_alkiot(poistetun_alkion_sijainti)

        self.alkioiden_lkm = self.alkioiden_lkm - 1

        return True
    
    def poista_alkio_ja_palauta_sen_sijainti(self, poistettava_alkio):
        for listan_indeksi in range(self.alkioiden_lkm):
            if poistettava_alkio == self.lista[listan_indeksi]:
                poistettavan_alkion_sijainti = listan_indeksi  # siis luku löytyy tuosta kohdasta :D
                self.lista[poistettavan_alkion_sijainti] = 0
                return poistettavan_alkion_sijainti
    
    def jarjesta_alkiot(self, poistetun_alkion_sijainti):
        for listan_indeksi in range(poistetun_alkion_sijainti, self.alkioiden_lkm - 1):
            siirrettava_alkio = self.lista[listan_indeksi]
            self.lista[listan_indeksi] = self.lista[listan_indeksi + 1]
            self.lista[listan_indeksi + 1] = siirrettava_alkio

    def kopioi_lista(self, a_lista, b_lista):
        for listan_indeksi in range(len(a_lista)):
            b_lista[listan_indeksi] = a_lista[listan_indeksi]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = self._luo_lista(self.alkioiden_lkm)

        for listan_indeksi in range(len(lista)):
            lista[listan_indeksi] = self.lista[listan_indeksi]

        return lista

    @staticmethod
    def yhdiste(a_lista, b_lista):
        x = IntJoukko()

        for a_alkio in a_lista.to_int_list():
            x.lisaa(a_alkio)

        for b_alkio in b_lista.to_int_list():
            x.lisaa(b_alkio)

        return x

    @staticmethod
    def leikkaus(a_lista, b_lista):
        y = IntJoukko()

        for a_alkio in a_lista.to_int_list():
            for b_alkio in b_lista.to_int_list():
                if a_alkio == b_alkio:
                    y.lisaa(a_alkio)

        return y

    @staticmethod
    def erotus(a_lista, b_lista):
        z = IntJoukko()

        for a_alkio in a_lista.to_int_list():
            z.lisaa(a_alkio)

        for b_alkio in b_lista.to_int_list():
            z.poista(b_alkio)

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        else:
            tulostus = "{"
            for listan_indeksi in range(self.alkioiden_lkm - 1):
                tulostus += str(self.lista[listan_indeksi]) + ", "
            tulostus += str(self.lista[self.alkioiden_lkm - 1]) + "}"
            return tulostus
