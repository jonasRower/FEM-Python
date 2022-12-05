

class oznaceniKCE:

    def __init__(self, pocetBunekVRade, pocetRad):

        self.pocetBunekVRade = pocetBunekVRade
        self.pocetRad = pocetRad

        self.cislaUzlu = []
        self.cislaUzlu = self.generujCislaUzlu()

        self.poziceNaRadku = self.generujPoziceNaRadku()
        self.cislaElementuTisk = self.generujOcislovaniElementu()
        self.cislaUzluTisk = self.upravPoleCislaUzluOPrazdneIndexy(self.cislaUzlu)
        self.kodovaCisla = self.generujKodovaCisla(self.cislaUzlu)
        self.kodovaCislaTisk = self.generujDataProTiskKodovaCisla(self.kodovaCisla)



    def getCislaUzlu(self):
        return(self.cislaUzluTisk)

    def getKodovaCisla(self):
        return(self.kodovaCislaTisk)

    def getCislaElementu(self):
        return(self.cislaElementuTisk)

    def getPoziceNaRadku(self):
        return(self.poziceNaRadku)



    def generujPoziceNaRadku(self):

        poziceNaRadku = []
        pozice = -8

        for i in range(0, self.pocetBunekVRade+1):
            pozice = pozice + 9
            poziceNaRadku.append(pozice)

        return(poziceNaRadku)


    def generujOcislovaniElementu(self):

        ocislovaniElementuJedneRady = []
        posledniCisloUzlu1 = -1
        posledniCisloUzlu2 = 0

        for r in range(0, self.pocetRad):
            ocislovaniElementuJedneRady = self.generujOcislovaniElementuProJednuRadu(posledniCisloUzlu1, posledniCisloUzlu2, ocislovaniElementuJedneRady)
            posledniCisloUzlu1 = posledniCisloUzlu1 + self.pocetBunekVRade*2
            posledniCisloUzlu2 = posledniCisloUzlu2 + self.pocetBunekVRade*2

        return(ocislovaniElementuJedneRady)


    def generujOcislovaniElementuProJednuRadu(self, posledniCisloUzlu1, posledniCisloUzlu2, ocislovaniElementuJedneRady):

        ocislovaniElementuJedneRady1 = []
        ocislovaniElementuJedneRady2 = []

        for i in range(0, self.pocetBunekVRade+1):

            if(i == 0):
                posledniCisloUzlu1Str = "   "
                posledniCisloUzlu2Str = "   "
            else:
                posledniCisloUzlu1 = posledniCisloUzlu1 + 2
                posledniCisloUzlu2 = posledniCisloUzlu2 + 2

                posledniCisloUzlu1Str = self.doplnMezeryPodlePoctuZnaku(posledniCisloUzlu1)
                posledniCisloUzlu2Str = self.doplnMezeryPodlePoctuZnaku(posledniCisloUzlu2)

            ocislovaniElementuJedneRady1.append(posledniCisloUzlu1Str)
            ocislovaniElementuJedneRady2.append(posledniCisloUzlu2Str)

        ocislovaniElementuJedneRady.append(ocislovaniElementuJedneRady1)
        ocislovaniElementuJedneRady.append(ocislovaniElementuJedneRady2)

        return(ocislovaniElementuJedneRady)



    # vytvori pole pro tisk - kodova cisla
    # pole je ve formatu tak aby bylo tisknutelne ve schema konstrukce
    def generujDataProTiskKodovaCisla(self, kodovaCisla):

        kodovaCislaUzlyTisk = []

        for i in range(0, len(kodovaCisla)):
            kodovaCislaUzlyRadek = kodovaCisla[i]
            kodovaCislaUzlyTisk = self.vratDvojiciRadkuProTiskKodovaCisla(kodovaCislaUzlyRadek, kodovaCislaUzlyTisk)


        return(kodovaCislaUzlyTisk)


    def vratDvojiciRadkuProTiskKodovaCisla(self, kodovaCislaUzlyRadek, kodovaCislaUzlyTisk):

        kodovaCislaUzlyRadekNew1 = []
        kodovaCislaUzlyRadekNew2 = []

        for i in range(0, len(kodovaCislaUzlyRadek)):

            kodovaCislaUzel = kodovaCislaUzlyRadek[i]
            kodoveCislo1 = kodovaCislaUzel[0]
            kodoveCislo2 = kodovaCislaUzel[1]

            kodoveCislo1str = self.doplnMezeryPodlePoctuZnaku(kodoveCislo1)
            kodoveCislo2str = self.doplnMezeryPodlePoctuZnaku(kodoveCislo2)

            kodovaCislaUzlyRadekNew1.append(kodoveCislo1str)
            kodovaCislaUzlyRadekNew2.append(kodoveCislo2str)

        kodovaCislaUzlyTisk.append(kodovaCislaUzlyRadekNew1)
        kodovaCislaUzlyTisk.append(kodovaCislaUzlyRadekNew2)

        return(kodovaCislaUzlyTisk)


    def generujKodovaCisla(self, cislaUzlu):

        posledniKodoveCislo = 0
        kodovaCisla = []

        for i in range(0, len(cislaUzlu)):
            cislaUzluRadek = cislaUzlu[i]
            kodovaCislaRadek = self.vratKodovaCislaProRadek(cislaUzluRadek, posledniKodoveCislo)
            kodovaCisla.append(kodovaCislaRadek)

            kodovaCislaPosledniUzel = kodovaCislaRadek[len(kodovaCislaRadek)-1]
            posledniKodoveCislo = kodovaCislaPosledniUzel[1]

        return(kodovaCisla)


    def vratKodovaCislaProRadek(self, cislaUzluRadek , posledniKodoveCislo):

        kodovaCislaRadek = []

        for i in range(0, len(cislaUzluRadek)):
            cisloUzlu = cislaUzluRadek[0]

            kodovaCislaVUzlu = self.vratDvojiciKodovychCiselKDanemuUzlu(cisloUzlu, posledniKodoveCislo)
            kodovaCislaRadek.append(kodovaCislaVUzlu)
            posledniKodoveCislo = kodovaCislaVUzlu[1]

        return(kodovaCislaRadek)


    def vratDvojiciKodovychCiselKDanemuUzlu(self, cisloUzlu, posledniKodoveCislo):
        kodovaCislaVUzlu = []

        kodoveCisloAktualni = posledniKodoveCislo + 1
        kodovaCislaVUzlu.append(kodoveCisloAktualni)

        kodoveCisloAktualni = kodoveCisloAktualni + 1
        kodovaCislaVUzlu.append(kodoveCisloAktualni)

        return(kodovaCislaVUzlu)





    def generujCislaUzlu(self):

        cislaUzlu = []
        cisloUzlu = 0

        for r in range(0, self.pocetRad+1):
            cislaUzluNaRadku = []

            for s in range(0, self.pocetBunekVRade+1):
                cisloUzlu = cisloUzlu + 1
                cislaUzluNaRadku.append(cisloUzlu)

            cislaUzlu.append(cislaUzluNaRadku)

        return(cislaUzlu)


    # aby bylo mozne tisknout konstrukci do schematu s cisly uzlu
    # je treba aby kazdy lichy radek obsahoval prazdne hodnoty - jelikož vzdy se tisknou 2 radky
    def upravPoleCislaUzluOPrazdneIndexy(self, cislaUzlu):

        pocetSloupcu = len(cislaUzlu[0])
        prazdnyRadek = []
        cislaUzluNew = []

        #vytvori prazdny radek
        for i in range(0, pocetSloupcu):
            prazdnyRadek.append("   ")

        for r in range(0, len(cislaUzlu)):
            cislaUzluNaRadku = cislaUzlu[r]
            cislaUzluNaRadku = self.doplnMezeryPodlePoctuZnakuProCelyRadek(cislaUzluNaRadku)

            cislaUzluNew.append(prazdnyRadek)
            cislaUzluNew.append(cislaUzluNaRadku)

        return(cislaUzluNew)


    # doplni mezery pro cely radek
    def doplnMezeryPodlePoctuZnakuProCelyRadek(self, hodnotyNaRadku):

        hodnotyNaRadkuNew = []

        for i in range(0, len(hodnotyNaRadku)):
            hodnota = hodnotyNaRadku[i]
            hodnota = int(hodnota)
            hodnotaNew = self.doplnMezeryPodlePoctuZnaku(hodnota)

            hodnotyNaRadkuNew.append(hodnotaNew)

        return(hodnotyNaRadkuNew)


    # doplni mezery, tak aby text v bunce byl odsazeny a texty se nachazely pod sebou
    def doplnMezeryPodlePoctuZnaku(self, hodnota):

        pocetMezer = 0

        if (hodnota < 100):
            pocetMezer = 1

            if (hodnota < 10):
                pocetMezer = 2

        hodnotaNew = ""
        for i in range(0, pocetMezer):
            hodnotaNew = hodnotaNew + " "

        hodnotaNew = hodnotaNew + str(hodnota)


        return(hodnotaNew)