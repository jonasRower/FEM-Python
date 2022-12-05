
class vystupSestaveniKGlob:

    def __init__(self, KGlob, kodovaCislaGlobalni):

        self.KGlob = KGlob
        self.kodovaCislaGlobalni = kodovaCislaGlobalni

        self.nazevSouboru = "vystupKGlob.txt"

        self.vystupDotxt = []
        self.vystupDotxt = self.tiskniMaticiTuhosti(KGlob, kodovaCislaGlobalni)

        #self.vystupDotxt.append("aaa")
        #self.vystupDotxt.append("bbb")
        #self.vystupDotxt.append("ccc")

        self.zapistxt(self.vystupDotxt)


    # ziska radek s vektorem kodovych cisel, aby je mohl tisknout k matici tuhosti
    def vratVodorovnyVektorKodovychCiselTisku(self, kodovaCisla):

        kodovaCislaRadek = ""

        for r in range(0, len(kodovaCisla)):
            kodoveCislo = kodovaCisla[r]
            kodoveCislo = self.dopisPocetMezerPredString(kodoveCislo, 8)
            kodovaCislaRadek = kodovaCislaRadek + "   " + kodoveCislo

        return (kodovaCislaRadek)


    # v zavislosti na poctu kodovych cisel vytvori vodorovnou oddelovaci caru
    def vratVodorovnouCaru(self, kodovaCislaGlobalni):

        oddelovaciCara = "    "
        pocetKodovychCisel = len(kodovaCislaGlobalni)

        for i in range(0, pocetKodovychCisel):
            oddelovaciCara = oddelovaciCara + "-----------"

        return(oddelovaciCara)


    # ziska sloupec s vektorem kodovych cisel, aby je mohl tisknout k matici tuhosti
    def vratSvislyVektorKodovychCiselTisku(self, kodovaCisla):

        kodovaCislaSloupec = []

        for r in range(0, len(kodovaCisla)):
            kodoveCislo = kodovaCisla[r]
            kodovaCislaSloupec.append(kodoveCislo)

        return (kodovaCislaSloupec)


    def tiskniMaticiTuhosti(self, maticeTuhosti, kodovaCisla):

        maticeTuhostiTisk = []
        kodovaCislaRadek = self.vratVodorovnyVektorKodovychCiselTisku(kodovaCisla)
        kodovaCislaSloupec = self.vratSvislyVektorKodovychCiselTisku(kodovaCisla)
        oddelovaciCara = self.vratVodorovnouCaru(kodovaCisla)

        maticeTuhostiTisk.append("")
        maticeTuhostiTisk.append("")
        maticeTuhostiTisk.append(kodovaCislaRadek)
        maticeTuhostiTisk.append(oddelovaciCara)

        for r in range(0, len(maticeTuhosti)):
            radekMaticeTuhosti = maticeTuhosti[r]

            radekTisk = ""
            for s in range(0, len(radekMaticeTuhosti)):
                hodnota = radekMaticeTuhosti[s]
                hodnota = round(hodnota, 3)
                hodnotaStr = str(hodnota)
                hodnotaStr = self.dopisPocetMezerPredString(str(hodnotaStr), 8)
                radekTisk = radekTisk + "   " + hodnotaStr

            kodoveCisloSloupec = kodovaCislaSloupec[r]
            radekTisk = radekTisk + "   |" + str(kodoveCisloSloupec)

            maticeTuhostiTisk.append(radekTisk)

        return (maticeTuhostiTisk)


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


    def zapistxt(self, poletxt):
        dataWrite = ""
        f = open(self.nazevSouboru, 'w')

        for i in range(0, len(poletxt)):
            radek = poletxt[i]
            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()