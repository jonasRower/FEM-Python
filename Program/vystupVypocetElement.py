
# pripravuje data do txt pro jeden element, tedy:
# cisla uzlu + schema
# souradnice + schema
# kodova cisla + schema
# modul pruznosti + my vypis
# souradnice vypis
# matice tuhosti lokalni vcetne kodovych cisel


class vypocetJedenElement:
    def __init__(self, cisloElementu, cislaUzlu, Souradnice, kodovaCisla, E, my, K, cipDolu, souradniceUzluElement, maticeTuhostiElement):

        self.souradniceUzluElement = souradniceUzluElement
        self.maticeTuhostiElement = maticeTuhostiElement

        self.cipDolu = cipDolu
        self.cisloElementu = cisloElementu
        self.cislaUzlu = cislaUzlu
        self.Souradnice = Souradnice
        self.kodovaCisla = kodovaCisla
        self.E = E
        self.my = my
        self.K = K



        self.vystupJedenElement = self.vytvorData()

    def getVystupJedenElement(self):
        return(self.vystupJedenElement)


    def vytvorData(self):

        if(self.cipDolu == True):
            trojuhelnikUzly = self.nakresliTrojuhelnikSCipemDolu(self.cislaUzlu)
            trojuhelnikSouradnice = self.nakresliTrojuhelnikSCipemDolu(self.Souradnice)
            trojuhelnikKodovaCisla = self.nakresliTrojuhelnikSCipemDolu(self.kodovaCisla)

        else:
            trojuhelnikUzly = self.nakresliTrojuhelnikSCipemNahoru(self.cislaUzlu)
            trojuhelnikSouradnice = self.nakresliTrojuhelnikSCipemNahoru(self.Souradnice)
            trojuhelnikKodovaCisla = self.nakresliTrojuhelnikSCipemNahoru(self.kodovaCisla)


        souradniceXY = self.dopisSouradniceXY(self.souradniceUzluElement)
        maticeTuhostiElementu = self.tiskniMaticiTuhosti(self.maticeTuhostiElement, self.kodovaCisla)

        sloucenaData = self.slucBunkyKSobe(trojuhelnikUzly, trojuhelnikSouradnice, "        ")
        sloucenaData = self.slucBunkyKSobe(sloucenaData, trojuhelnikKodovaCisla, "          ")
        sloucenaData = self.zarovnejBunkuNaDelkuZnaku(sloucenaData, 65)
        sloucenaData = self.slucBunkyKSobe(sloucenaData, souradniceXY, "")
        sloucenaData = self.zarovnejBunkuNaDelkuZnaku(sloucenaData, 90)
        sloucenaData = self.slucBunkyKSobe(sloucenaData, maticeTuhostiElementu, "")

        ###############################################

        poleProZapis = []

        poleProZapis.append("")
        poleProZapis.append("")
        poleProZapis.append("############################################################################################################################################")
        poleProZapis.append("")
        poleProZapis.append("")
        poleProZapis.append("Element " + str(self.cisloElementu))
        poleProZapis.append("")
        poleProZapis.append("")
        poleProZapis.append("Uzly elementu       Souradnice elementu     Kodova cisla elementu    Souradnice elementu                  Matice tuhosti elementu"  )
        poleProZapis.append("Lokalni/Globalni           X / Y                   X / Y                                                            K0  ")
        poleProZapis.append("")
        poleProZapis = poleProZapis + sloucenaData

        # poleProZapis = poleProZapis + trojuhelnikSCipemDolu

        return(poleProZapis)

        self.zapistxt(poleProZapis)

    def slucBunkyKSobe(self, bunkaVlevo, bunkaVPravo, mezera):
        slouceneRadky = []

        for r in range(0, len(bunkaVlevo)):
            radekVlevo = bunkaVlevo[r]
            if(r > len(bunkaVPravo)-1):
                radekVPravo = ""
            else:
                radekVPravo = bunkaVPravo[r]

            sloucenyRadek = radekVlevo + mezera + radekVPravo
            slouceneRadky.append(sloucenyRadek)

        return (slouceneRadky)

    def nakresliTrojuhelnikSCipemNahoru(self, oznaceniVrcholuTrojuhelnika):
        horniCipDvojice = oznaceniVrcholuTrojuhelnika[0]
        dolniLevyCipDvojice = oznaceniVrcholuTrojuhelnika[1]
        dolniPravyCipDvojice = oznaceniVrcholuTrojuhelnika[2]

        horniCipDvojiceX = horniCipDvojice[0]
        horniCipDvojiceY = horniCipDvojice[1]

        dolniLevyCipX = dolniLevyCipDvojice[0]
        dolniLevyCipY = dolniLevyCipDvojice[1]

        dolniPravyCipX = dolniPravyCipDvojice[0]
        dolniPravyCipY = dolniPravyCipDvojice[1]

        trojuhelnik = []

        trojuhelnik.append(self.dopisPocetMezerPredString(str(horniCipDvojiceX),12))
        trojuhelnik.append(self.dopisPocetMezerPredString(str(horniCipDvojiceY),12))
        trojuhelnik.append("          /|")
        trojuhelnik.append("         / |")
        trojuhelnik.append("        /  |")
        trojuhelnik.append("       /   |")
        trojuhelnik.append("      /    |")
        trojuhelnik.append("     /     |")
        trojuhelnik.append("    /      |")
        trojuhelnik.append("    --------")
        trojuhelnik.append(self.dopisPocetMezerPredString(str(dolniLevyCipX),4) + " " + self.dopisPocetMezerPredString(str(dolniPravyCipX),7))
        trojuhelnik.append(self.dopisPocetMezerPredString(str(dolniLevyCipY),4) + " " + self.dopisPocetMezerPredString(str(dolniPravyCipY),7))


        return (trojuhelnik)


    def nakresliTrojuhelnikSCipemDolu(self, oznaceniVrcholuTrojuhelnika):
        dolniCipDvojice = oznaceniVrcholuTrojuhelnika[2]
        horniLevyCipDvojice = oznaceniVrcholuTrojuhelnika[0]
        horniPravyCipDvojice = oznaceniVrcholuTrojuhelnika[1]

        dolniCipDvojiceX = dolniCipDvojice[0]
        dolniCipDvojiceY = dolniCipDvojice[1]

        horniLevyCipX = horniLevyCipDvojice[0]
        horniLevyCipY = horniLevyCipDvojice[1]

        horniPravyCipX = horniPravyCipDvojice[0]
        horniPravyCipY = horniPravyCipDvojice[1]

        trojuhelnik = []

        trojuhelnik.append(self.dopisPocetMezerPredString(str(horniLevyCipX),4)+ " " + self.dopisPocetMezerPredString(str(horniPravyCipX),6))
        trojuhelnik.append(self.dopisPocetMezerPredString(str(horniLevyCipY),4)+ " " + self.dopisPocetMezerPredString(str(horniPravyCipY),6))
        trojuhelnik.append("   --------")
        trojuhelnik.append("   |      /")
        trojuhelnik.append("   |     / ")
        trojuhelnik.append("   |    /  ")
        trojuhelnik.append("   |   /   ")
        trojuhelnik.append("   |  /    ")
        trojuhelnik.append("   | /     ")
        trojuhelnik.append("   |/      ")
        trojuhelnik.append(" " + self.dopisPocetMezerPredString(str(dolniCipDvojiceX),8))
        trojuhelnik.append(" " + self.dopisPocetMezerPredString(str(dolniCipDvojiceY),8))

        return (trojuhelnik)


    def dopisSouradniceXY(self, souradniceUzluPodleElementu):

        poleSouradnice = []

        poleSouradnice.append("")
        poleSouradnice.append("")
        poleSouradnice.append("        x1 = " + souradniceUzluPodleElementu[0])
        poleSouradnice.append("        y1 = " + souradniceUzluPodleElementu[1])
        poleSouradnice.append("        x2 = " + souradniceUzluPodleElementu[2])
        poleSouradnice.append("        y2 = " + souradniceUzluPodleElementu[3])
        poleSouradnice.append("        x3 = " + souradniceUzluPodleElementu[4])
        poleSouradnice.append("        y3 = " + souradniceUzluPodleElementu[5])

        return(poleSouradnice)


    # ziska radek s vektorem kodovych cisel, aby je mohl tisknout k matici tuhosti
    def vratVodorovnyVektorKodovychCiselTisku(self, kodovaCisla):

        kodovaCislaRadek = ""

        for r in range(0, len(kodovaCisla)):
            kodovaCislaXY = kodovaCisla[r]

            for s in range(0, len(kodovaCislaXY)):
                kodoveCislo = kodovaCislaXY[s]
                kodoveCislo = self.dopisPocetMezerPredString(kodoveCislo,8)
                kodovaCislaRadek = kodovaCislaRadek + "   " + kodoveCislo

        return(kodovaCislaRadek)


    # ziska sloupec s vektorem kodovych cisel, aby je mohl tisknout k matici tuhosti
    def vratSvislyVektorKodovychCiselTisku(self, kodovaCisla):

        kodovaCislaSloupec = []

        for r in range(0, len(kodovaCisla)):
            kodovaCislaXY = kodovaCisla[r]

            for s in range(0, len(kodovaCislaXY)):
                kodoveCislo = kodovaCislaXY[s]
                kodovaCislaSloupec.append(kodoveCislo)

        return(kodovaCislaSloupec)


    def tiskniMaticiTuhosti(self, maticeTuhosti, kodovaCisla):

        maticeTuhostiTisk = []
        kodovaCislaRadek = self.vratVodorovnyVektorKodovychCiselTisku(kodovaCisla)
        kodovaCislaSloupec = self.vratSvislyVektorKodovychCiselTisku(kodovaCisla)

        maticeTuhostiTisk.append("")
        maticeTuhostiTisk.append("")
        maticeTuhostiTisk.append(kodovaCislaRadek)
        maticeTuhostiTisk.append("    -----------------------------------------------------------------------")

        for r in range(0, len(maticeTuhosti)):
            radekMaticeTuhosti = maticeTuhosti[r]

            radekTisk = ""
            for s in range(0, len(radekMaticeTuhosti)):
                hodnota = radekMaticeTuhosti[s]
                hodnota = round(hodnota, 3)
                hodnotaStr = str(hodnota)
                hodnotaStr = self.dopisPocetMezerPredString(str(hodnotaStr),8)
                radekTisk = radekTisk + "   " + hodnotaStr

            kodoveCisloSloupec = kodovaCislaSloupec[r]
            radekTisk = radekTisk + "   |" + kodoveCisloSloupec

            maticeTuhostiTisk.append(radekTisk)

        return(maticeTuhostiTisk)


    def dopisPocetMezerPredString(self, text, odsazeniPoslednihoZnakuZLeva):

        textStr = str(text)
        textStr = textStr.replace(" ", "")
        pocetZnaku = len(textStr)
        pocetMezer = odsazeniPoslednihoZnakuZLeva - pocetZnaku
        mezera = ""

        for r in range(0, pocetMezer):
            mezera = mezera + " "

        textNew = mezera + textStr

        return(textNew)


    def zarovnejBunkuNaDelkuZnaku(self, bunkaPole, pocetZnaku):

        bunkaNew = []

        for i in range(0, len(bunkaPole)):
            radek = bunkaPole[i]
            radekNew = self.doplnTextNaRadkuOPrazdneZnaky(radek, pocetZnaku)
            bunkaNew.append(radekNew)

        return(bunkaNew)


    # rozsiri text na radku tak, aby text byl doplnen o prazdne znaky na specifickou delku
    def doplnTextNaRadkuOPrazdneZnaky(self, text, pocetZnakuCelkem):

        delkaStavajicihoTextu = len(text)
        pridejPocetZnaku = pocetZnakuCelkem - delkaStavajicihoTextu

        # vytvori mezeru o poctu znaku
        mezera = ""
        for i in range(0, pridejPocetZnaku):
            mezera = mezera + " "

        textNew = text + mezera

        return (textNew)
