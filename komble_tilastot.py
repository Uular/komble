#-*- coding: utf-8 -*-


def tilastoi_peli(voittaja, peliaika, pvm, vuorot):
    tilastot = open("komble_tilastot.txt", "a")
    tilastot.write(",".join([voittaja, str(peliaika), pvm, str(vuorot)]) + "\n")
    tilastot.close()
    
def laske_aika(t):
    aika = ""
    tunnit, minuutit = divmod(int(t), 3600)
    minuutit, sekunnit = divmod(minuutit, 60)
    return "%d:%.2d:%.2d" % (tunnit, minuutit, sekunnit)
    
    
def viimeiset():
    print "Viimeisten 10 pelin voittajat ja peliajat:\n"
    while True:
        try:
            tilastot = open("komble_tilastot.txt")
            rivit = tilastot.readlines()
        except IOError:
            print "Tilastoja ei ole saatavilla!"
            break
        if rivit:
            i = len(rivit) - 1
            print "Pvm:           Voittaja:    Kesto:  Vuorot:"
            j = 1
            while j <= 10 and i >= 0:
                rivi = rivit[i].split(",")
                print rivi[2].ljust(15) + rivi[0].ljust(13) + laske_aika(float(rivi[1])).ljust(8) + rivi[3].rjust(7)
                i = i - 1  
                j = j + 1
            tilastot.close()     
        else:
            print "Ei näytettävää."
        break
    print ""
    
def parhaat(n=5):
    """
    Tulostaa listan eniten kertoja voittaneista pelaajista.
    """
    tilastot = open("komble_tilastot.txt")
    rivit = tilastot.readlines()
    tilastot.close()
    voittajat = []
    kaytetyt = []
    
    for i in rivit:
        voittajat.append(i.split(",")[0])
        
    for j in range(len(rivit)):
        voittaja = voittajat[j]
        if voittaja not in kaytetyt:
            voitot = voittajat.count(voittaja)
            voittajat[j] = (voitot, voittaja)
            kaytetyt.append(voittaja)
            
    voittajat.sort()
    voittajat.reverse()
    
    if n > len(voittajat):
        n = len(voittajat)
        
    print "Historian parhaat Komblen pelaajat:\n"
    print "Sija  Nimi         Voittoja"
    
    for i in range(n):
        print str(i + 1).ljust(6) + voittajat[i][1].ljust(13) + str(voittajat[i][0]).rjust(8)

    

    
                
def tyhjenna():
    tilastot = open("komble_tilastot.txt", "w")
    tilastot.close()
    print "Tilastot tyhjennetty!"
            
def yleista():
    tilastot = open("komble_tilastot.txt")
    rivit = tilastot.readlines()
    tilastot.close()
    
    pelatut = len(rivit)
    vuorot = 0
    aika = 0
    for i in rivit:
        vuorot = vuorot + int(i.split(",")[3])
        aika = aika + float(i.split(",")[1])
    aika_vuoro = aika / vuorot
    tunnit, minuutit = divmod(int(aika), 3600)
    minuutit, sekunnit = divmod(minuutit, 60)
    
    print "Yleistä potaskaa:"
    print "Komblen peluuseen on tuhlattu elämää %d tuntia, %d minuuttia ja %d sekuntia." % (tunnit, minuutit, sekunnit)
    print "Pelaajat (mukaanlukien tietokone!) ovat pelanneet kaikkiaan %d vuoroa." % vuorot
    print "Keskimääräinen aika / vuoro on %.2f sekuntia." % aika_vuoro

def selaa():
    while True:
        print "\nVaihtoehdot: viimeiset, tyhjennä, parhaat, yleistä, poistu"
        syote = raw_input("Anna syöte: ").lower()
        if syote == "tyhjennä":
            varmistus = raw_input("Oletko varma että haluat tyhjentää tilastot? (K/E)")
            if varmistus.lower() == "k" :
                tyhjenna()       
            else:
                print "Tilastoja ei poistettu.\n"
        elif syote == "viimeiset":
            viimeiset()    
        elif syote == "parhaat":
            parhaat()
        elif syote == "poistu":
            break
        elif syote == "yleistä":
            yleista()
        
    

if __name__ == "__main__":
    print "Tervetuloa Komble-tilastoselaimeen!\n"
    selaa()