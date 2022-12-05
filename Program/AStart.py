import sestavMaticiTuhosti
import schemaKonstrukce
import generujKodovaCisla
import kodovaCislaDoVypoctu
import generujMesh
import vystupVypocet
import sestavMaticiTuhosti2
import vystupKGlob

#maticeTuhosti = sestavMaticiTuhosti.maticeTuhosti()
#schemaKonstrukce.schema()


pocetBunekVRade = 4
pocetRad = 3

celkovaDelka = 12
celkovaVyska = 6


oznaceniKCE = generujKodovaCisla.oznaceniKCE(pocetBunekVRade, pocetRad)
cislaElementu = oznaceniKCE.getCislaElementu()
cislaUzlu = oznaceniKCE.getCislaUzlu()
kodovaCisla = oznaceniKCE.getKodovaCisla()
poziceNaRadku = oznaceniKCE.getPoziceNaRadku()

meshSit = generujMesh.MESH(pocetBunekVRade, pocetRad, celkovaVyska, celkovaDelka, cislaUzlu)
sirkaElementu = meshSit.getSirkaElementuTisk()
vyskaElementu = meshSit.getVyskaElementuTisk()
souradniceUzlu = meshSit.getSouradniceUzluTisk()
souradniceUzluPole = meshSit.getSouradniceCislaUzlu()

schemaKonstrukce.schema(sirkaElementu, "rozmeryKCE.txt", vyskaElementu, poziceNaRadku, pocetBunekVRade, pocetRad, True)
schemaKonstrukce.schema(souradniceUzlu, "souradniceUzlu.txt", cislaElementu, poziceNaRadku, pocetBunekVRade, pocetRad, False)
schemaKonstrukce.schema(cislaUzlu, "cislaUzlu.txt", cislaElementu, poziceNaRadku, pocetBunekVRade, pocetRad, False)
schemaKonstrukce.schema(kodovaCisla, "kodovaCisla.txt", cislaElementu, poziceNaRadku, pocetBunekVRade, pocetRad, False)

# pripravy kodova cisla do vypoctu pro jednotlive elementy
kodovaCislaVypocet = kodovaCislaDoVypoctu.kodovaCislaVypocet(kodovaCisla, pocetRad, pocetBunekVRade, souradniceUzlu)
kodovaCislaPodleElementu = kodovaCislaVypocet.getKodovaCislaDoVypoctu()
vsechnaKodovaCisla = kodovaCislaVypocet.getVsechnaKodovaCisla()
seznamElementuPodleKodovychCisel = kodovaCislaVypocet.getSeznamElementuPodleKodovychCisel()
souradniceUzluPodleElementu = kodovaCislaVypocet.getSouradniceUzluPodleElementu()
elementyPodleKodovehoCisla = kodovaCislaVypocet.getKodovaCislaPodleElementu()

# sestavi matici tuhosti do vypoctu
#sestavMaticiTuhosti.maticeTuhosti(kodovaCisla, vsechnaKodovaCisla, seznamElementuPodleKodovychCisel)

# vola jadro FEM
jadroFEM = sestavMaticiTuhosti2.maticeTuhosti(souradniceUzluPodleElementu, elementyPodleKodovehoCisla, kodovaCislaPodleElementu, vsechnaKodovaCisla)
maticeTuhostiVsechElementu = jadroFEM.getMaticeTuhostiVsechElementu()
maticeTuhostiGlobalni = jadroFEM.getMaticiTuhostiGlobalni()



vystupVypocet.vypocet("vystup.txt", cislaElementu, cislaUzlu, souradniceUzlu, kodovaCisla, 99, 99, 99, pocetBunekVRade, pocetRad, souradniceUzluPodleElementu, maticeTuhostiVsechElementu)
vystupKGlob.vystupSestaveniKGlob(maticeTuhostiGlobalni, vsechnaKodovaCisla)


print("")