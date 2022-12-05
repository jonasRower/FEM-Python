
import vystupVypocetElement
import sestavMaticiTuhosti2

# generuje vypocet do txt souboru

class vypocet:

    def __init__(self, nazevSouboru, cislaElementu, cislaUzlu, Souradnice, kodovaCisla, E, my, K, pocetBunekVRade, pocetRad, souradniceUzluPodleElementu, maticeTuhostiVsechElementu):

        self.souradniceUzluPodleElementu = souradniceUzluPodleElementu
        self.maticeTuhostiVsechElementu = maticeTuhostiVsechElementu

        self.nazevSouboru = nazevSouboru
        self.cislaElementu = cislaElementu
        self.cislaUzlu = cislaUzlu
        self.Souradnice = Souradnice
        self.kodovaCisla = kodovaCisla
        self.E = E
        self.my = my
        self.K = K

        self.vystupDotxt = []

        self.pocetBunekVRade = pocetBunekVRade
        self.pocetRad = pocetRad


        self.poleUzluElementu = self.vratDvojiciRadkuProPopisElementu(self.cislaUzlu)
        self.poleSouradnice = self.vratDvojiciRadkuProPopisElementu(self.Souradnice)
        self.poleKodovaCisla = self.vratDvojiciRadkuProPopisElementu(self.kodovaCisla)

        self.vratVypocetTxtProJedenElement()
        self.zapistxt(self.vystupDotxt)

        print("")


    def vratVypocetTxtProJedenElement(self):

        cipDolu = False

        for i in range(0, len(self.poleUzluElementu)):
            cisloElementu = i + 1
            if(cipDolu == False):
                cipDolu = True
            else:
                cipDolu = False

            uzlyJedenElement = self.poleUzluElementu[i]
            souradniceJedenElement = self.poleSouradnice[i]
            kodovaCislaJedenElement = self.poleKodovaCisla[i]
            souradniceUzluElement = self.souradniceUzluPodleElementu[i]
            maticeTuhostiElement = self.maticeTuhostiVsechElementu[i]



            vystupJedenElement = vystupVypocetElement.vypocetJedenElement(cisloElementu, uzlyJedenElement, souradniceJedenElement, kodovaCislaJedenElement, 99, 99, 99, cipDolu, souradniceUzluElement, maticeTuhostiElement)
            vystupPole = vystupJedenElement.getVystupJedenElement()
            self.vystupDotxt = self.vystupDotxt + vystupPole


    def vratDvojiciRadkuProPopisElementu(self, poledata):

        horniRadekPopisElementu = self.vratPopisElementu(poledata, -3)
        dolniRadekPopisElementu = self.vratPopisElementu(poledata, -2)
        dataNew = []

        for r in range(0, len(dolniRadekPopisElementu)):

            horniRadek = horniRadekPopisElementu[r]
            dolniRadek = dolniRadekPopisElementu[r]
            radekNew = []

            for s in range(0, len(dolniRadek)):
                horniHodnota = horniRadek[s]
                dolniHodnota = dolniRadek[s]

                if (horniHodnota == "   "):
                    if(r % 2 == 0):            # rozhoduje zda je cip nahoru nebo dolu
                        if(s == 0):
                            horniHodnota = "  1"
                        if (s == 1):
                            horniHodnota = "  3"
                        if (s == 2):
                            horniHodnota = "  2"

                    else:
                        if (s == 0):
                            horniHodnota = "  2"
                        if (s == 1):
                            horniHodnota = "  3"
                        if (s == 2):
                            horniHodnota = "  1"


                dvojiceHodnot = []
                dvojiceHodnot.append(horniHodnota)
                dvojiceHodnot.append(dolniHodnota)

                radekNew.append(dvojiceHodnot)

            dataNew.append(radekNew)


        return(dataNew)


    def vratPopisElementu(self, poleData, r1):

        cislaUzluElementu = []

        for r in range(0, self.pocetRad*2+2):
            r1 = r1 + 2
            if(r1+4 > len(poleData)):
                break
            else:
                r1B = r1+1
                r2B = r1+3

                poleRada1B = poleData[r1B]
                poleRada2B = poleData[r2B]

                for s in range(0, self.pocetBunekVRade):
                    cislaUzluElementuCipDolu = self.vratCislaUzluTrojuhelnikaCipDolu(poleRada1B, poleRada2B, s)
                    cislaUzluElementuCipNahoru = self.vratCislaUzluTrojuhelnikaCipNahoru(poleRada1B, poleRada2B, s)

                    cislaUzluElementu.append(cislaUzluElementuCipDolu)
                    cislaUzluElementu.append(cislaUzluElementuCipNahoru)

        return(cislaUzluElementu)


    def vratCislaUzluTrojuhelnikaCipDolu(self, cislaUzluRada1, cislaUzluRada2, s):

        horniLevyUzel = cislaUzluRada1[s]
        horniPravyUzel = cislaUzluRada1[s+1]
        dolniUzel = cislaUzluRada2[s]

        cislaUzluElementu = []
        cislaUzluElementu.append(horniLevyUzel)
        cislaUzluElementu.append(horniPravyUzel)
        cislaUzluElementu.append(dolniUzel)

        return(cislaUzluElementu)


    def vratCislaUzluTrojuhelnikaCipNahoru(self, cislaUzluRada1, cislaUzluRada2, s):

        dolniLevyUzel = cislaUzluRada2[s]
        dolniPravyUzel = cislaUzluRada2[s + 1]
        horniUzel = cislaUzluRada1[s + 1]

        cislaUzluElementu = []
        cislaUzluElementu.append(dolniLevyUzel)
        cislaUzluElementu.append(dolniPravyUzel)
        cislaUzluElementu.append(horniUzel)

        return(cislaUzluElementu)







    #def ziskejDataPodleCislaElementu(self):

        cisloElementu = 1




    def zapistxt(self, poleHtml):
        dataWrite = ""
        f = open(self.nazevSouboru, 'w')

        for i in range(0, len(poleHtml)):
            radek = poleHtml[i]
            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()