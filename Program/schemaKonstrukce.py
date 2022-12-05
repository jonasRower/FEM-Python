
# vykresli schema konstrukce do txt
# do schematu dopise kodova cisla
class schema:

    def __init__(self, hodnotyRadekSloupec, nazevSouboru, cislaElementu, poziceNaRadku, pocetBunekVRade, pocetRad, jednaSeORozmeryElementu):

        self.pocetRad = pocetRad + 1
        self.pocetBunek = pocetBunekVRade + 1

        self.schemaPole = []
        #self.poziceNaRadku = [1, 10, 19, 28, 37, 46]
        self.poziceNaRadku = poziceNaRadku
        #self.ocislovaniElementu = [["   ", "  1", "  3", "  5", "  7", "  9"], ["   ", "  2", "  4", "  6", "  8", " 10"], ["   ", "   ", " 11", " 13", " 15", " 17"], ["   ", " 12", " 14", " 16", " 18", " 20"]]

        self.ocislovaniElementu = cislaElementu
        self.hodnotyRadekSloupec = hodnotyRadekSloupec
        self.nazevSouboru = nazevSouboru
        self.jednaSeORozmeryElementu = jednaSeORozmeryElementu
        #self.hodnotyRadekSloupec = [[" 58", " 66", " 77", " 15", " 88", " 99"], [" 58", " 66", " 77", " 15", " 88", " 99"], [" 58", " 66", " 77", " 15", " 88", " 99"], ["158", "166", "177", "115", "188", "199"], ["158", "166", "177", "115", "188", "199"], ["258", "266", "277", "215", "288", "299"], ["258", "266", "277", "215", "288", "299"]]


        # ziska pole se schematem
        self.schemaPole = self.poskladejRadyBunekPodSebe()

        # odsadi schema vice z leva, aby se tam veslo ocislovani
        self.schemaPole = self.odsadSchemaDalOdKraje(5, self.schemaPole)

        self.schemaPole = self.dopisCiselneOznaceniProJednotliveRadky(self.schemaPole)
        self.schemaPole = self.dopisOznaceniProJednotliveElementy(self.schemaPole)
        self.zapistxt(self.schemaPole)



    def dopisOznaceniProJednotliveElementy(self, schemaPole):

        indexyRadkuOznaceniElementu = self.vratIndexyRadkuProOznaceniElementu(schemaPole)
        schemaPoleNew = []
        lichy = False

        for i in range(0, len(schemaPole)):
            radek = schemaPole[i]

            if i in indexyRadkuOznaceniElementu:
                if(lichy == False):
                    lichy = True
                    posun = -4
                else:
                    lichy = False
                    posun = 0

                indexI = indexyRadkuOznaceniElementu.index(i)
                cislovaniElementu = self.ocislovaniElementu[indexI]


                radek = self.dopisCiselneOznaceniProDanyRadek(radek, cislovaniElementu, posun)

            schemaPoleNew.append(radek)

        return(schemaPoleNew)


    def dopisCiselneOznaceniProJednotliveRadky(self, schemaPole):

        indexyVodorovneRozdeleni = self.vratIndexyRadkuSVodorovnymRozdelenim(schemaPole)
        schemaPoleNew = []

        for i in range(0, len(schemaPole)):
            radek = schemaPole[i]

            if i in indexyVodorovneRozdeleni:
                indexI = indexyVodorovneRozdeleni.index(i)
                if(indexI > len(self.hodnotyRadekSloupec)-1):
                    hodnotyNaRadku = "   "
                else:
                    hodnotyNaRadku = self.hodnotyRadekSloupec[indexI]

                posun = 0

                if(self.jednaSeORozmeryElementu == True):
                    if(i == 4):
                        posun = -4

                radek = self.dopisCiselneOznaceniProDanyRadek(radek, hodnotyNaRadku, posun)


            schemaPoleNew.append(radek)

        return(schemaPoleNew)



    def vratIndexyRadkuProOznaceniElementu(self, schemaPole):

        indexyRadkuOznaceniElementu = []
        prvniVodorovneRozdeleni = True

        for r in range(1, len(schemaPole)):
            radek = schemaPole[r]
            jednaSeOVodorovneRozdeleni = self.detekujSubstring(radek, "---")
            if (jednaSeOVodorovneRozdeleni == True):
                if(prvniVodorovneRozdeleni == False):
                    indexyRadkuOznaceniElementu.append(r - 5)
                    indexyRadkuOznaceniElementu.append(r - 4)

                prvniVodorovneRozdeleni = False

        return(indexyRadkuOznaceniElementu)



    def popisCisleneOznaceniElementu(self, radek, oznaceniElemnetu):

        for i in range(0, len(self.poziceNaRadku)):
            pozice = self.poziceNaRadku[i]
            hodnota = "XXX"

            radek = self.dopisCiselneOznaceniNaRadek(radek, hodnota, pozice)

        return(radek)



    def dopisCiselneOznaceniProDanyRadek(self, radek, hodnotyNaRadku, posun):

        for i in range(0, len(self.poziceNaRadku)):
            pozice = self.poziceNaRadku[i] + posun

            # pokud je pole kratsi, pak se vrati prazdna hodnota
            if (i > len(hodnotyNaRadku) - 1):
                hodnota = "   "
            else:
                hodnota = hodnotyNaRadku[i]

            radek = self.dopisCiselneOznaceniNaRadek(radek, hodnota, pozice)
            print("")

        return(radek)



    def dopisCiselneOznaceniNaRadek(self, puvodniRadek, ciselneOznaceni, pozice):

        poleZnakuRadkuNew = []
        vysledekStr = ""

        poleZnakuRadku = list(puvodniRadek)
        ciselneOznaceniPoleZnaku = list(ciselneOznaceni)
        znakOrig = True
        indexOznac = -1

        aa = len(poleZnakuRadku)


        if(len(poleZnakuRadku) < pozice):
            vysledekStr = puvodniRadek

            for i in range(len(poleZnakuRadku), pozice+1):
                vysledekStr = vysledekStr + " "

            vysledekStr = vysledekStr + ciselneOznaceni
            print("")


        else:
            for r in range(0, len(poleZnakuRadku)):
                if(znakOrig == True):
                    znak = poleZnakuRadku[r]
                else:
                    indexOznac = indexOznac + 1
                    znak = ciselneOznaceniPoleZnaku[indexOznac]

                    if(indexOznac == len(ciselneOznaceniPoleZnaku)-1):
                        znakOrig = True

                if(r == pozice):
                    znakOrig = False


                poleZnakuRadkuNew.append(znak)

            # prevede pole znaku zpet Na string
            for i in range(0, len(poleZnakuRadkuNew)):
                znak = poleZnakuRadkuNew[i]
                vysledekStr = vysledekStr + znak


        return(vysledekStr)



    def vratIndexyRadkuSVodorovnymRozdelenim(self, schemaPole):

        indexyVodorovneRozdeleni = []

        for r in range(1, len(schemaPole)):
            radek = schemaPole[r]
            jednaSeOVodorovneRozdeleni = self.detekujSubstring(radek, "---")
            if(jednaSeOVodorovneRozdeleni == True):
                indexyVodorovneRozdeleni.append(r-2)
                indexyVodorovneRozdeleni.append(r-1)


        return(indexyVodorovneRozdeleni)


    # vrati True, pokud text obsahuje substring
    def detekujSubstring(self, text, substring):

        try:
            index = text.index(substring)
        except:
            index = -1

        if(index == -1):
            obsahujeSubString = False
        else:
            obsahujeSubString = True


        return(obsahujeSubString)


    def poskladejRadyBunekPodSebe(self):

        #pocetRad = 3
        schemaPole = []

        for i in range(1, self.pocetRad):
            if(i == 1):
                jednaSeOPrvniRadu = True
            else:
                jednaSeOPrvniRadu = False

            rada = self.nakresliASkladejBunkyVJedneRade(jednaSeOPrvniRadu)

            for r in range(0, len(rada)):
                radek = rada[r]
                schemaPole.append(radek)

        return(schemaPole)


    def odsadSchemaDalOdKraje(self, odsazeni, schemaPole):

        schemaPoleNew = []

        # vytvori string odsazeni
        odsazeniStr = ""
        for i in range(0, odsazeni):
            odsazeniStr = odsazeniStr + " "

        # vlozi prazdne radky
        for i in range(0, odsazeni):
            radek = ""
            schemaPoleNew.append(radek)

        for r in range(0, len(schemaPole)):
            radek = schemaPole[r]
            radek = odsazeniStr + radek
            schemaPoleNew.append(radek)

        return(schemaPoleNew)


    def nakresliASkladejBunkyVJedneRade(self, jednaSeOPrvniRadu):

        #pocetBunek = 5
        schemaBunkaPole = []

        # nevim proc to nefunguje pro self.pocetBunek = 2, tak to resim podminkou
        #jednaSeOPrvniRadu = False

        bunka1 = self.vytvorRaduBunek("|", 10, jednaSeOPrvniRadu)

        if(self.pocetBunek == 2):
            schemaBunkaPole = bunka1
        else:
            for i in range(1, self.pocetBunek-1):
                bunka2 = self.vytvorRaduBunek(" ", 9, jednaSeOPrvniRadu)
                schemaBunkaPole = self.slucBunkyKSobe(bunka1, bunka2)

                bunka1 = schemaBunkaPole

        return(schemaBunkaPole)


    def slucBunkyKSobe(self, bunka1, bunka2):

        schemaBunkaPole = []

        for r in range(0, len(bunka1)):
            radek1 = bunka1[r]
            radek2 = bunka2[r]

            radek = radek1 + radek2

            schemaBunkaPole.append(radek)

        return(schemaBunkaPole)


    def vytvorRaduBunek(self, svislaCaraVlevo, countChar, jednaSeOPrvniRadu):

        schemaBunkaPole = []

        if (jednaSeOPrvniRadu == True):
            schemaBunkaPole = self.zapisRadekNaHorniHraneElementu(countChar, schemaBunkaPole)

        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-3, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-4, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-5, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-6, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-7, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-8, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekUvnitrElementu(countChar, countChar-9, svislaCaraVlevo, schemaBunkaPole)
        schemaBunkaPole = self.zapisRadekNaHorniHraneElementu(countChar, schemaBunkaPole)

        return(schemaBunkaPole)


    def zapisRadekNaHorniHraneElementu(self, pocetZnakuMeziSvislymiOkraji, schemaBunkaPole):

        radekCaraVodorovna = ""

        for i in range(0, pocetZnakuMeziSvislymiOkraji):
            radekCaraVodorovna = radekCaraVodorovna + "-"

        schemaBunkaPole.append(radekCaraVodorovna)

        return(schemaBunkaPole)


    def zapisRadekUvnitrElementu(self, pocetZnakuMeziSvislymiOkraji, indexSikmeHrany, svislaCaraVlevo, schemaBunkaPole):

        radekcaraSvisla = svislaCaraVlevo

        for i in range(0, pocetZnakuMeziSvislymiOkraji-2):
            if (i == indexSikmeHrany):
                znak = "/"
            else:
                znak = " "

            radekcaraSvisla = radekcaraSvisla + znak


        radekcaraSvisla = radekcaraSvisla + "|"
        schemaBunkaPole.append(radekcaraSvisla)

        return(schemaBunkaPole)



    def zapistxt(self, poleHtml):

        dataWrite = ""
        f = open(self.nazevSouboru, 'w')

        for i in range(0, len(poleHtml)):
            radek = poleHtml[i]
            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()