import numpy as np
from copy import copy, deepcopy

class maticeTuhosti:

    def __init__(self, souradniceUzluPodleElementu, elementyPodleKodovehoCisla, kodovaCisla, vsechnaKodovaCisla):

        self.souradniceUzluPodleElementu = souradniceUzluPodleElementu
        self.elementyPodleKodovehoCisla = elementyPodleKodovehoCisla
        self.kodovaCisla = kodovaCisla
        self.vsechnaKodovaCisla = vsechnaKodovaCisla

        self.E = 30
        self.my = 0.25
        self.t = 0.5

        self.b = 3
        self.h = 2

        self.poleDvojicKodovychCisel = self.vygenerujDvojiceKodovychCisel(self.vsechnaKodovaCisla)
        self.pocetKodovychCisel = self.ziskejPocetKodovychCisel()
        self.lokalizaceKodovychCisel = self.lokalizujKodovaCislaPodleElementuAIndexu()
        self.dvojiceKodovychCiselProVsechnyElementy = self.generujDvojiceKodovychCiselProVsechnyElementy()


        # matice D
        self.D = self.vratMaticiD(self.my, self.E)

        # seznam vsech matic elementu pro vsechny elementy
        self.maticeTuhostiVsechElementu = self.vratPoleMaticTuhostiProVsechnyElementy(self.souradniceUzluPodleElementu)

        # vytvori matici tuhosti plnou nul (prazdnou), tak aby mohl do ni zapisovat
        self.kGlob = self.vytvorPrazdnouGlobalniMaticiPodleVsechKodovychCisel(self.vsechnaKodovaCisla)

        # zapise do globalni matice tuhosti jednotlive cleny
        self.kGlob = self.vytvorKGlob(self.kGlob)

        print("")



    def getMaticeTuhostiVsechElementu(self):
        return(self.maticeTuhostiVsechElementu)

    def getMaticiTuhostiGlobalni(self):
        return(self.kGlob)




    ############## tady je chyba
    def vytvorKGlob(self, KGlob):

        for el in range(0, len(self.dvojiceKodovychCiselProVsechnyElementy)):
            dvojiceKodovychCiselElement = self.dvojiceKodovychCiselProVsechnyElementy[el]
            kGlobRadek = []

            for r in range(0, len(dvojiceKodovychCiselElement)):
                dvojiceKodovychCiselRadek = dvojiceKodovychCiselElement[r]

                for s in range(0, len(dvojiceKodovychCiselRadek)):
                    dvojiceKodovychCiselBunka = dvojiceKodovychCiselRadek[s]

                    KCradek = dvojiceKodovychCiselBunka[0]
                    KCsloupec = dvojiceKodovychCiselBunka[1]

                    # ziska soucet tuhosti v jednom clenu
                    sumaKclen = self.vratSoucetVsechLokalnichClenuMaticeTuhosti(KCradek, KCsloupec)
                    KGlob = self.zapisSoucetTuhostiDoMaticeTuhosti(KCradek, KCsloupec, sumaKclen, KGlob)

                    print("")

        return(KGlob)


    def zapisSoucetTuhostiDoMaticeTuhosti(self, KCradek, KCsloupec, hodnota, KGlob):

        # abych updatoval jen jeden člen pole je třeba, aby okopíroval pole
        # jinak se přepisují členy ve všech řádcích

        KGlobNew = []
        indexKCradek = self.vsechnaKodovaCisla.index(KCradek)
        indexKCsloupec = self.vsechnaKodovaCisla.index(KCsloupec)

        for r in range(0, len(KGlob)):
            radekKGlob = KGlob[r]
            # vytvari kopii vsech radku
            radekKGlobC = deepcopy(radekKGlob)
            if(r == indexKCradek):
                radekKGlobC[indexKCsloupec] = hodnota
            KGlobNew.append(radekKGlobC)

        return(KGlobNew)


    # vytvori globalni matici tuhosti plnou 0
    def vytvorPrazdnouGlobalniMaticiPodleVsechKodovychCisel(self, vsechnaKodovaCisla):

        nulovaMaticeKradek = []
        nulovaMaticeK = []
        for s in range(0, len(vsechnaKodovaCisla)):
            nulovaMaticeKradek.append(0)

        for r in range(0, len(vsechnaKodovaCisla)):
            nulovaMaticeK.append(nulovaMaticeKradek)

        return (nulovaMaticeK)


    # vrati soucet vsech lokalnich clenu matice tuhosti
    def vratSoucetVsechLokalnichClenuMaticeTuhosti(self, KCradek, KCsloupec):

        dvojiceElementAPozicePole = self.proDvojiciKodovychCiselVratSeznamElementuAPozicKtereScitat(KCradek, KCsloupec)
        sumaKclen = 0

        for i in range(0, len(dvojiceElementAPozicePole)):
            elementAPozice = dvojiceElementAPozicePole[i]
            elementPoziceRadek = elementAPozice[0]
            elementPoziceSloupec = elementAPozice[1]
            elementRadek = elementPoziceRadek[0]
            elementSloupec = elementPoziceSloupec[0]

            if(elementRadek == elementSloupec):
                poziceRadek = elementPoziceRadek[1]
                poziceSloupec = elementPoziceSloupec[1]
                element = elementRadek

                Kclen = self.vratClenMaticeTuhostiPodleDvojiceKCAelementu(poziceRadek, poziceSloupec, element)
                sumaKclen = sumaKclen + Kclen

        return(sumaKclen)


    # vrati seznam vsech pozic na vsech elementech ktere je treba secist
    def proDvojiciKodovychCiselVratSeznamElementuAPozicKtereScitat(self, KCradek, KCsloupec):

        radekLok = self.vratSeznamPozicProNacitaniClenuTuhosti(KCradek)
        sloupecLok = self.vratSeznamPozicProNacitaniClenuTuhosti(KCsloupec)

        dvojiceElementAPozicePole = []

        if (radekLok != -1):
            if (sloupecLok != -1):
                maxI = len(max(radekLok[0], sloupecLok[0]))

                for i in range(0, maxI):
                    elementAPoziceRadek = self.vratElementAPoziciDleIndexu(radekLok, i)
                    elementAPoziceSloupec = self.vratElementAPoziciDleIndexu(sloupecLok, i)

                    if(elementAPoziceRadek[0] > -1):
                        if (elementAPoziceSloupec[0] > -1):
                            dvojiceElementAPozice = []
                            dvojiceElementAPozice.append(elementAPoziceRadek)
                            dvojiceElementAPozice.append(elementAPoziceSloupec)

                            dvojiceElementAPozicePole.append(dvojiceElementAPozice)


        return(dvojiceElementAPozicePole)



    # vrati pozici kodoveho cisla v poli v zavislosti na elementu

    def vratElementAPoziciDleIndexu(self, lokalizace, index):

        elemLok = lokalizace[0]
        poziceLok = lokalizace[1]

        element = -1
        pozice = -1
        data = []

        if (index < len(elemLok)):
            element = elemLok[index]
            pozice = poziceLok[index]

        data.append(element)
        data.append(pozice)

        return (data)


    # vrati soucet vsech tuhosti pres vsechny elementy pro jedno dane kodove cislo
    def vratSeznamPozicProNacitaniClenuTuhosti(self, KodoveCislo):

        poziceLok = -1

        for i in range(0, len(self.lokalizaceKodovychCisel)):
            radekLokalizace = self.lokalizaceKodovychCisel[i]
            KCLok = radekLokalizace[0]
            if(KCLok == KodoveCislo):
                poziceLok = radekLokalizace[1]
                break

        return(poziceLok)


    def vratClenMaticeTuhostiPodleDvojiceKCAelementu(self, KindexRadek, KindexSloupec, element):
        Kelem = self.maticeTuhostiVsechElementu[element-1]
        KelemRadek = Kelem[KindexRadek]
        KelemClen = KelemRadek[KindexSloupec]

        return(KelemClen)



    # vygeneruje dvojice kodovych cisel, ktere odpovidaji pozicim radek, sloupec
    def generujDvojiceKodovychCiselProVsechnyElementy(self):

        dvojiceKCVsechnyElementy = []

        for KC in range(0, len(self.kodovaCisla)):
            kodovaCislaElement = self.kodovaCisla[KC]
            poleDvojicKC = self.vygenerujDvojiceKodovychCisel(kodovaCislaElement)
            dvojiceKCVsechnyElementy.append(poleDvojicKC)

        return(dvojiceKCVsechnyElementy)

    # vygeneruje dvojice kodovych cisel, ktere odpovidaji pozicim radek, sloupec
    def vygenerujDvojiceKodovychCisel(self, kodovaCislaElement):

        poleDvojicKC = []

        for r in range(len(kodovaCislaElement)):
            rKC = kodovaCislaElement[r]
            radekKC = []

            for s in range(len(kodovaCislaElement)):
                sKC = kodovaCislaElement[s]

                dvojiceKC = []
                dvojiceKC.append(rKC)
                dvojiceKC.append(sKC)

                radekKC.append(dvojiceKC)
            poleDvojicKC.append(radekKC)

        return(poleDvojicKC)


    def lokalizujKodovaCislaPodleElementuAIndexu(self):

        lokalizaceKodovychCiselPole = []

        for KC in range(1, self.pocetKodovychCisel):
            seznamElementuAIndexyPoleRadek = []
            seznamElementuAIndexy = self.proHledaneKodoveCisloVratSeznamElementuAIndexyKodovychCiselVPoli(KC)
            seznamElementuAIndexyPoleRadek.append(KC)

            seznamElementuAIndexyPoleRadek.append(seznamElementuAIndexy)

            # 1. místo - Kodové číslo
            # 2. místo - seznam elementů, na který se dané kódové číslo nachází
            # 3. místo - ke každému elementu je index který odpovídá pořadí v poli kódových čísel pro daný element
            lokalizaceKodovychCiselPole.append(seznamElementuAIndexyPoleRadek)

        return(lokalizaceKodovychCiselPole)


    def proHledaneKodoveCisloVratSeznamElementuAIndexyKodovychCiselVPoli(self, hledaneKodoveCislo):

        seznamElementuAIndexy = []

        seznamElementu = self.vratSeznamElementuKdeSeNachaziKodoveCislo(self.elementyPodleKodovehoCisla, hledaneKodoveCislo)
        indexyVPoliKC = []
        for i in range(0, len(seznamElementu)):
            element = seznamElementu[i]
            kodovaCislaElement = self.kodovaCisla[element-1]
            indexVPoliKC = kodovaCislaElement.index(hledaneKodoveCislo)
            indexyVPoliKC.append(indexVPoliKC)

        seznamElementuAIndexy.append(seznamElementu)
        seznamElementuAIndexy.append(indexyVPoliKC)

        return(seznamElementuAIndexy)


    def vratSeznamElementuKdeSeNachaziKodoveCislo(self, elementyPodleKodovehoCisla, ocekavaneKodoveCislo):

        for i in range(0, len(elementyPodleKodovehoCisla)):
            kodovaCislaElement = elementyPodleKodovehoCisla[i]
            kodoveCisloPole = kodovaCislaElement[0]
            if(ocekavaneKodoveCislo == kodoveCisloPole):
                kodovaCisla = kodovaCislaElement[1]
                break

        return(kodovaCisla)


    def vratPoleMaticTuhostiProVsechnyElementy(self, souradniceUzluPodleElementu):

        maticeTuhostiVsechElementu = []

        for i in range(0, len(souradniceUzluPodleElementu)):
            souradniceElementu = souradniceUzluPodleElementu[i]

            maticeTuhostiElementu = self.vratMaticiTuhostiElementu(souradniceElementu)
            maticeTuhostiVsechElementu.append(maticeTuhostiElementu)

        return(maticeTuhostiVsechElementu)


    def vratMaticiD(self, my, E):
        # Matice D
        D0 = E / (1 - my * my)
        D = [[D0, my * D0, 0], [my * D0, D0, 0], [0, 0, D0 * (1 - my) / 2]]

        return (D)


    def vratMaticiTuhostiElementu(self, souradnice):

        souradniceInt = self.prevedPoleNaFloat(souradnice)

        x1 = souradniceInt[0]
        y1 = souradniceInt[1]
        x2 = souradniceInt[2]
        y2 = souradniceInt[3]
        x3 = souradniceInt[4]
        y3 = souradniceInt[5]

        x12 = x1 - x2
        x13 = x1 - x3
        x23 = x2 - x3

        y12 = y2 - y1
        y13 = y3 - y1
        y23 = y3 - y2

        x21 = -x12
        y31 = -y13
        x32 = -x23

        detJ = abs(x13 * y23 - x23 * y13)


        B = [[y23, 0, y31, 0, y12, 0], [0, x32, 0, x13, 0, x21], [x32, y23, x13, y31, x21, y12]]
        B = np.multiply(B, 1 / detJ)
        BT = np.transpose(B)
        BTD = np.matmul(BT, self.D)
        BTDB = np.matmul(BTD, B)
        K = np.multiply(BTDB, self.t * detJ / 2)

        return (K)


    def prevedPoleNaFloat(self, pole):

        poleNew = []

        # prevede souradnice na int
        for i in range(0, len(pole)):
            hodnotaStr = pole[i]
            hodnotaStr = hodnotaStr.replace(" ", "")
            hodnota = float(hodnotaStr)
            poleNew.append(hodnota)

        return (poleNew)



    # ziska pocet kodovych cisel z poleDvojicKodovychCisel
    def ziskejPocetKodovychCisel(self):

        kodoveCisloMax = 0

        for r in range(0, len(self.poleDvojicKodovychCisel)):
            dvojiceKodovychCiselRadek = self.poleDvojicKodovychCisel[r]

            for s in range(0, len(self.poleDvojicKodovychCisel)):
                dvojiceKodovychCiselSloupec = dvojiceKodovychCiselRadek[s]

                for b in range(0, len(dvojiceKodovychCiselSloupec)):
                    dvojiceKodovychCiselBunka = dvojiceKodovychCiselRadek[b]
                    kodoveCislo1 = dvojiceKodovychCiselBunka[0]
                    kodoveCislo2 = dvojiceKodovychCiselBunka[1]

                    if (kodoveCislo1 > kodoveCisloMax):
                        kodoveCisloMax = kodoveCislo1

                    if (kodoveCislo2 > kodoveCisloMax):
                        kodoveCisloMax = kodoveCislo2

        return (kodoveCisloMax)

    def vratPocetKodovychCisel(self):
        self.pocetElementu = len(self.kodovaCisla)
        KCposledniRadek = self.kodovaCisla[self.pocetElementu - 1]
        self.pocetKodovychCisel = KCposledniRadek[len(KCposledniRadek) - 1]

        print("")