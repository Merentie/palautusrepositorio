from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.pelaa()

        elif vastaus.endswith("b"):
            yksinpeli = KPSTekoaly()
            yksinpeli.pelaa()

        elif vastaus.endswith("c"):
            haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()
        
        else:
            break


if __name__ == "__main__":
    main()
