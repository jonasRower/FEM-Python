
class kodovaCislaVypocet:

    def __init__(self, kodovaCisla, pocetRad, pocetBunekVRade, souradniceUzlu):

        self.kodovaCisla = kodovaCisla
        self.pocetRad = pocetRad
        self.pocetBunekVRade = pocetBunekVRade
        self.souradniceUzlu = souradniceUzlu

        self.kodovaCislaDoVypoctu = self.generujKodovaCisla(kodovaCisla)
        self.vsechnaKodovaCisla = self.vytvorVektorVsechKodovychCisel(self.kodovaCislaDoVypoctu)
        self.seznamElementuPodleKodovychCisel = self.vratSeznamElementuPodleKodovychCisel(self.vsechnaKodovaCisla, self.kodovaCislaDoVypoctu)
        self.souradniceUzluPodleElementu = self.vratSouradniceUzluPodleElementu()
        self.kodovaCislaPodleElementu = self.vratSeznamKodovychCiselPodleElementu(self.kodovaCislaDoVypoctu)


    def getKodovaCislaDoVypoctu(self):
        return(self.kodovaCislaDoVypoctu)

    def getVsechnaKodovaCisla(self):
        return(self.vsechnaKodovaCisla)

    def getSeznamElementuPodleKodovychCisel(self):
        return(self.seznamElementuPodleKodovychCisel)

    def getSouradniceUzluPodleElementu(self):
        return(self.souradniceUzluPodleElementu)

    def getKodovaCislaPodleElementu(self):
        return(self.kodovaCislaPodleElementu)



    # dopise souradnice uzlu k jednotlivym elementum
    # souradnice jsou razeny podle lokalniho ocislovani elementu
    def vratSouradniceUzluPodleElementu(self):

        souradnicePodleElementu = []

        r1 = -2
        for r in range(0, len(self.souradniceUzlu)):
            r1 = r1 + 2
            if(r1 > len(self.souradniceUzlu)-3):
                break
            else:
                poleX1 = self.souradniceUzlu[r1]
                poleY1 = self.souradniceUzlu[r1+1]
                poleX2 = self.souradniceUzlu[r1+2]
                poleY2 = self.souradniceUzlu[r1+3]

                for s in range(0, self.pocetBunekVRade):
                    souradnicePodleElementuCipDolu = self.vratSouradniceUzluProElementCipemDolu(poleX1, poleY1, poleX2, poleY2, s)
                    souradnicePodleElementuCipNahoru = self.vratSouradniceUzluProElementCipemNahoru(poleX1, poleY1, poleX2, poleY2, s)
                    souradnicePodleElementu.append(souradnicePodleElementuCipDolu)
                    souradnicePodleElementu.append(souradnicePodleElementuCipNahoru)

        return(souradnicePodleElementu)


    def vratSouradniceUzluProElementCipemDolu(self, poleX1, poleY1, poleX2, poleY2, s):

        souradnicePodleElementu = []

        x1 = poleX1[s]
        y1 = poleY1[s]
        x2 = poleX2[s]
        y2 = poleY2[s]
        x3 = poleX1[s+1]
        y3 = poleY1[s+1]

        souradnicePodleElementu.append(x1)
        souradnicePodleElementu.append(y1)
        souradnicePodleElementu.append(x2)
        souradnicePodleElementu.append(y2)
        souradnicePodleElementu.append(x3)
        souradnicePodleElementu.append(y3)

        return(souradnicePodleElementu)


    def vratSouradniceUzluProElementCipemNahoru(self, poleX1, poleY1, poleX2, poleY2, s):

        souradnicePodleElementu = []

        x1 = poleX2[s+1]
        y1 = poleY2[s+1]
        x2 = poleX2[s]
        y2 = poleY2[s]
        x3 = poleX1[s+1]
        y3 = poleY1[s+1]

        souradnicePodleElementu.append(x1)
        souradnicePodleElementu.append(y1)
        souradnicePodleElementu.append(x2)
        souradnicePodleElementu.append(y2)
        souradnicePodleElementu.append(x3)
        souradnicePodleElementu.append(y3)

        return(souradnicePodleElementu)



    # dopise seznam elementu, ktere obsahuji kodove cislo
    def vratSeznamElementuPodleKodovychCisel(self, vsechnaKodovaCisla, kodovaCisla):

        seznamElementuPodleKodovychCisel = []

        for i in range(0, len(vsechnaKodovaCisla)):
            seznamElementuPodleKodovychCiselRadek = []

            kodoveCislo = vsechnaKodovaCisla[i]
            seznamElementu = self.vratSeznamElementuPodleKodovehoCisla(kodovaCisla, kodoveCislo)
            seznamElementuPodleKodovychCiselRadek.append(kodoveCislo)
            seznamElementuPodleKodovychCiselRadek.append(seznamElementu)

            seznamElementuPodleKodovychCisel.append(seznamElementuPodleKodovychCiselRadek)

        return(seznamElementuPodleKodovychCisel)


    def vratSeznamElementuPodleKodovehoCisla(self, kodovaCisla, kodoveCislo):

        cislaElementu = []

        for i in range(0, len(kodovaCisla)):
            kodovaCislaElement = kodovaCisla[i]
            if kodoveCislo in kodovaCislaElement:
                cisloElementu = i + 1
                cislaElementu.append(cisloElementu)

        return(cislaElementu)


    def vytvorVektorVsechKodovychCisel(self, kodovaCisla):

        vsechnaKodovaCisla = []

        # vytvori seznam vsech kodovych cisel, ktere vsak mohou byt duplicitni
        for i in range(0, len(kodovaCisla)):
            kodovaCislaElementu = kodovaCisla[i]
            vsechnaKodovaCisla = vsechnaKodovaCisla + kodovaCislaElementu

        # ke kazdemu indexu pole nalezi pocet vyskytu kodovych cisel
        poctyKodovychCisel = []
        vsechnaKodovaCislaUnikatni = []

        for i in range(0, len(vsechnaKodovaCisla)):
            kodoveCisloAktualni = i
            pocetKodovychCisel = vsechnaKodovaCisla.count(kodoveCisloAktualni)
            if (pocetKodovychCisel > 0):
                vsechnaKodovaCislaUnikatni.append(kodoveCisloAktualni)

        return(vsechnaKodovaCislaUnikatni)


    def ziskejKodovaCislaProTrojuhelnikOrientovanyCipemDolu(self, kodovaCisla, index, rada):

        kodovaCislaElementu = []

        kodovaCislaRadek1 = kodovaCisla[rada + 0]
        kodovaCislaRadek2 = kodovaCisla[rada + 1]
        kodovaCislaRadek3 = kodovaCisla[rada + 2]
        kodovaCislaRadek4 = kodovaCisla[rada + 3]

        KC1 = kodovaCislaRadek1[index]
        KC2 = kodovaCislaRadek2[index]
        KC3 = kodovaCislaRadek1[index + 1]
        KC4 = kodovaCislaRadek2[index + 1]
        KC5 = kodovaCislaRadek3[index]
        KC6 = kodovaCislaRadek4[index]

        kodovaCislaElementu.append(KC1)
        kodovaCislaElementu.append(KC2)
        kodovaCislaElementu.append(KC3)
        kodovaCislaElementu.append(KC4)
        kodovaCislaElementu.append(KC5)
        kodovaCislaElementu.append(KC6)

        return(kodovaCislaElementu)


    def ziskejKodovaCislaProTrojuhelnikOrientovanyCipemNahoru(self, kodovaCisla, index, rada):
        kodovaCislaElementu = []

        kodovaCislaRadek1 = kodovaCisla[rada]
        kodovaCislaRadek2 = kodovaCisla[rada + 1]
        kodovaCislaRadek3 = kodovaCisla[rada + 2]
        kodovaCislaRadek4 = kodovaCisla[rada + 3]

        KC1 = kodovaCislaRadek3[index]
        KC2 = kodovaCislaRadek4[index]
        KC3 = kodovaCislaRadek3[index + 1]
        KC4 = kodovaCislaRadek4[index + 1]
        KC5 = kodovaCislaRadek1[index + 1]
        KC6 = kodovaCislaRadek2[index + 1]

        kodovaCislaElementu.append(KC1)
        kodovaCislaElementu.append(KC2)
        kodovaCislaElementu.append(KC3)
        kodovaCislaElementu.append(KC4)
        kodovaCislaElementu.append(KC5)
        kodovaCislaElementu.append(KC6)

        return (kodovaCislaElementu)



    def generujKodovaCisla(self, kodovaCisla):

        kodovaCislaVsechElementu = []
        radek = -2

        for r in range(0, self.pocetRad):
            radek = radek + 2

            for i in range(0, self.pocetBunekVRade):

                kodovaCislaElementu1 = self.ziskejKodovaCislaProTrojuhelnikOrientovanyCipemDolu(kodovaCisla, i, radek)
                kodovaCislaElementu2 = self.ziskejKodovaCislaProTrojuhelnikOrientovanyCipemNahoru(kodovaCisla, i, radek)

                kodovaCislaElementu1Int = self.prevedObsahPoleNaCisla(kodovaCislaElementu1)
                kodovaCislaElementu2Int = self.prevedObsahPoleNaCisla(kodovaCislaElementu2)

                kodovaCislaVsechElementu.append(kodovaCislaElementu1Int)
                kodovaCislaVsechElementu.append(kodovaCislaElementu2Int)

        return(kodovaCislaVsechElementu)


    def vratSeznamKodovychCiselPodleElementu(self, kodovaCisla):

        seznamKodovychCiselPodleElementu = []
        pocetKodovychCisel = (self.pocetRad + 1)*(self.pocetBunekVRade + 1)*2

        for KC in range(1, pocetKodovychCisel+1):
            seznamRadek = []
            seznamElementu = self.vratElementyObsahujiciDaneKodoveCislo(kodovaCisla, KC)
            seznamRadek.append(KC)
            seznamRadek.append(seznamElementu)
            seznamKodovychCiselPodleElementu.append(seznamRadek)

        return(seznamKodovychCiselPodleElementu)


    def vratElementyObsahujiciDaneKodoveCislo(self, kodovaCisla, kodoveCislo):

        elementyObsahujiciKodoveCislo = []

        for i in range(0, len(kodovaCisla)):
            kodovaCislaElement = kodovaCisla[i]
            if(kodoveCislo in kodovaCislaElement):
                elementyObsahujiciKodoveCislo.append(i+1)

        return(elementyObsahujiciKodoveCislo)


    def prevedObsahPoleNaCisla(self, obsahPole):

        obsahPoleNew = []

        for i in range(0, len(obsahPole)):
            obsahStr = obsahPole[i]

            obsah = obsahStr.replace(" ", "")
            obsahInt = int(obsah)

            obsahPoleNew.append(obsahInt)

        return(obsahPoleNew)