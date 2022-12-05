

class MESH:

    def __init__(self, pocetBunekVRade, pocetRad, celkovaVyska, celkovaDelka, cislaUzlu):

        self.pocetBunekVRade = pocetBunekVRade
        self.pocetRad = pocetRad
        self.celkovaVyska = celkovaVyska
        self.celkovaDelka = celkovaDelka
        self.cislaUzlu = cislaUzlu

        self.poleDelekElementu = self.vratPoleRozdeleniElementu(celkovaDelka, pocetBunekVRade)
        self.poleVysekElementu = self.vratPoleRozdeleniElementu(celkovaVyska, pocetRad)

        self.souradniceCislaUzlu = self.generujSouradniceCiselUzlu(cislaUzlu)
        self.souradniceUzluTisk = self.generujSouradniceUzluProTisk = self.generujSouradniceUzluProTisk()

        self.sirkaElementuTisk = self.generujSirkyElementuTisk(self.pocetBunekVRade, self.pocetRad, self.poleDelekElementu)
        self.vyskaElementuTisk = self.generujVyskyElementuTisk(self.pocetBunekVRade, self.pocetRad, self.poleVysekElementu)


    def getSirkaElementuTisk(self):
        return(self.sirkaElementuTisk)

    def getVyskaElementuTisk(self):
        return(self.vyskaElementuTisk)

    def getSouradniceUzluTisk(self):
        return(self.souradniceUzluTisk)

    def getSouradniceCislaUzlu(self):
        return(self.souradniceCislaUzlu)



    def generujSouradniceUzluProTisk(self):

        souradniceUzluProTisk = []

        i1 = -1
        for i in range(0, len(self.cislaUzlu)):
            i1 = i1 + 2
            if(i1 > len(self.cislaUzlu)-1):
                break
            else:
                cislaUzluRadek = self.cislaUzlu[i1]
                souradniceDvojiceRadku = self.generujSouradniceUzluRadek(cislaUzluRadek)
                souradniceUzluProTisk = souradniceUzluProTisk + souradniceDvojiceRadku

        return(souradniceUzluProTisk)


    def generujSouradniceUzluRadek(self, cislaUzluRadek):

        souradniceUzluRadek = []
        souradniceUzluRadek1 = []
        souradniceUzluRadek2 = []

        souradniceXY = []
        souradniceXY.append("XX")
        souradniceXY.append("YY")

        for i in range(0, self.pocetBunekVRade+1):
            cisloUzluStr = cislaUzluRadek[i]
            cisloUzluStr = cisloUzluStr.replace(" ", "")
            cisloUzlu = int(cisloUzluStr)
            souradniceXY = self.vratSouradnicePodleCislaUzlu(cisloUzlu)
            souradniceX = souradniceXY[0]
            souradniceY = souradniceXY[1]

            souradniceXstr = self.doplnMezeryPodlePoctuZnaku(souradniceX)
            souradniceYstr = self.doplnMezeryPodlePoctuZnaku(souradniceY)

            souradniceUzluRadek1.append(souradniceXstr)
            souradniceUzluRadek2.append(souradniceYstr)

        souradniceUzluRadek.append(souradniceUzluRadek1)
        souradniceUzluRadek.append(souradniceUzluRadek2)

        return(souradniceUzluRadek)


    def vratSouradnicePodleCislaUzlu(self, cisloUzlu):

        for i in range(0, len(self.souradniceCislaUzlu)):
            cislaUzluRadek = self.souradniceCislaUzlu[i]
            cisloUzluPole = cislaUzluRadek[0]
            if(cisloUzluPole == cisloUzlu):
                souradniceXY = cislaUzluRadek[1]
                break

        return(souradniceXY)



    def generujSouradniceCiselUzlu(self, cislaUzlu):

        souradniceCislaUzlu = []
        polePoradniceDelekElementu = self.vratPoradniceDelekElementu(self.poleDelekElementu)
        polePoradniceVysekElementu = self.vratPoradniceDelekElementu(self.poleVysekElementu)

        r1 = -1

        for r in range(0, len(cislaUzlu)):
            radek = cislaUzlu[r]

            for s in range(0, len(radek)):
                cisloUzluStr = radek[s]
                if(cisloUzluStr == "   "):
                    break
                else:
                    if(s == 0):
                        r1 = r1 + 1

                    cisloUzluStr = cisloUzluStr.replace(" ","")
                    cisloUzlu = int(cisloUzluStr)
                    souradniceX = polePoradniceDelekElementu[s]
                    souradniceY = polePoradniceVysekElementu[r1]

                    souradniceCislaUzluRadek = []
                    souradniceXY = []
                    souradniceXY.append(souradniceX)
                    souradniceXY.append(souradniceY)

                    souradniceCislaUzluRadek.append(cisloUzlu)
                    souradniceCislaUzluRadek.append(souradniceXY)
                    souradniceCislaUzlu.append(souradniceCislaUzluRadek)

        return(souradniceCislaUzlu)



    def vratPoradniceDelekElementu(self, poleDelekElementu):

        poradnice = 0
        polePoradnic = [poradnice]

        for i in range(0, len(poleDelekElementu)):
            delkaElementu = poleDelekElementu[i]
            poradnice = poradnice + delkaElementu
            polePoradnic.append(poradnice)

        return(polePoradnic)


    # zatim konstrukci rozdeluje linearne, takze deli celou delku rovnomerne
    def vratPoleRozdeleniElementu(self, celkovaDelka, pocetBunek):

        delkaJednohoElementu = celkovaDelka/pocetBunek

        poleDelek = []
        for i in range(0, pocetBunek):
            poleDelek.append(delkaJednohoElementu)

        return(poleDelek)


    def generujVyskyElementuTisk(self, pocetBunekVRade, pocetRad, poleVysek):

        vyskaElementu = []

        for r in range(0, pocetRad):
            prazdnyDataRadek1 = []
            prazdnyDataRadek2 = []

            for s in range(0, pocetBunekVRade + 1):
                hodnotaStr = "   "
                if(s == 0):
                    hodnota = poleVysek[r]
                    hodnotaStr = self.doplnMezeryPodlePoctuZnaku(hodnota)

                prazdnyDataRadek1.append("   ")
                prazdnyDataRadek2.append(hodnotaStr)

            vyskaElementu.append(prazdnyDataRadek1)
            vyskaElementu.append(prazdnyDataRadek2)

        return(vyskaElementu)


    # generuje pole do schematu rozmeryKCE.txt
    def generujSirkyElementuTisk(self, pocetBunekVRade, pocetRad, poleDelek):

        sirkaElementu = []

        for r in range(0, pocetRad):
            prazdnyDataRadek = []

            if (r == 1):
                prazdnyDataRadek = self.prevedPoleDelekTisk(poleDelek)
            else:
                for s in range(0, pocetBunekVRade + 1):
                    prazdnyDataRadek.append("   ")

            sirkaElementu.append(prazdnyDataRadek)

        return(sirkaElementu)


    # prevede pole delek do pole, aby mohl data tisknout ve schematu
    def prevedPoleDelekTisk(self, poleDelek):

        poleDelekStr = ["   "]

        for i in range(0, len(poleDelek)):
           delka = poleDelek[i]
           delkaStr = self.doplnMezeryPodlePoctuZnaku(delka)
           poleDelekStr.append(delkaStr)

        return(poleDelekStr)



    # doplni mezery, tak aby text v bunce byl odsazeny a texty se nachazely pod sebou
    def doplnMezeryPodlePoctuZnaku(self, hodnota):

        pocetMezer = 0

        jednaSeOFloat = isinstance(hodnota, float)
        if(jednaSeOFloat == True):
            pocetMezer = 2

        else:

            if (hodnota < 100):
                pocetMezer = 1

                if (hodnota < 10):
                    pocetMezer = 2

        hodnotaNew = ""
        for i in range(0, pocetMezer):
            hodnotaNew = hodnotaNew + " "

        hodnotaNew = hodnotaNew + str(hodnota)

        return (hodnotaNew)
