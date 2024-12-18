from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        toisen_siirto = input("Toisen pelaajan siirto: ")
        return toisen_siirto
