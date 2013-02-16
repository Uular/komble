#-*- coding: utf-8 -*-

import sys
import random
import time

def gen_pelilauta():
    """Palauttaa listan muotoa
    
    [[Lauta], [[Koti1], [Maali1]], [[Koti2], [Maali2]], [[Koti3], [Maali3]], [[Koti4], [Maali4]]]
    
    jossa [Koti]-listat on täytetty neljällä pelinappulalla, [Lauta] ja [Maali] on täytetty "  ":llä.
    
    """
    
    
    pelilauta = []
    
    for i in range(28):
	    pelilauta.append("  ")
    
    lauta = [pelilauta]
	
    for i in range(4):
        pelaaja =[]
        pesa = []
        maali = []
	    
        for j in range(4):
	          pesa.append(str(i+1) + "ABCD"[j])
	          maali.append("  ")
	                    
        pelaaja.append(pesa)
        pelaaja.append(maali)        
        lauta.append(pelaaja)
    
    return lauta


	
def tulosta_pelilauta(lauta, pelaaja):
    """Tulostaa pelilaudan, kotipesät, maalialueet sekä keskelle vuorossa olevan pelaajan.
    
    """
    
            
    l = lauta[0]
    p1 = lauta[1]
    p2 = lauta[2]
    p3 = lauta[3]
    p4 = lauta[4]
    
    print "Pelitilanne:"
    print "                 v 2 >     "
    print " ┌──┬──┬──┬──┬──┬──┬──┬──┐ "
    print " │%s│%s│%s│%s│%s│%s│%s│%s│ " % (l[1],  l[2],     l[3],     l[4],     l[5],     l[6],     l[7],     l[8])
    print " ├──╆──┼──┼──┼──┼──┼──╅──┤ " 
    print "^│%s│%s│%s│%s│%s┃%s│%s│%s│ " % (l[0],  p1[0][0], p1[0][1], p1[0][2], p1[0][3], p2[1][0], p2[0][0], l[9])
    print "1├──┼──┼──┼──┼──╂──┼──┼──┤ " 
    print ">│%s│%s│%s│%s│%s┃%s│%s│%s│ " % (l[27], p1[1][0], p1[1][1], p1[1][2], p1[1][3], p2[1][1], p2[0][1], l[10])
    print " ├──┼━━┿━━╈━━┷━━╉──┼──┼──┤ "
    print " │%s│%s│%s┃ KOM ┃%s│%s│%s│ " % (l[26], p4[0][3], p4[1][3],                     p2[1][2], p2[0][2], l[11])
    print " ├──┼──┼──┨%s┠──┼──┼──┤ " % lauta[pelaaja][2][:5].center(5)
    print " │%s│%s│%s┃ BLE ┃%s│%s│%s│ " % (l[25], p4[0][2], p4[1][2],                     p2[1][3], p2[0][3], l[12])
    print " ├──┼──┼──╊━━┯━━╇━━┿━━┼──┤ "
    print " │%s│%s│%s┃%s│%s│%s│%s│%s│<" % (l[24], p4[0][1], p4[1][1], p3[1][3], p3[1][2], p3[1][1], p3[1][0], l[13])
    print " ├──┼──┼──╂──┼──┼──┼──┼──┤3"
    print " │%s│%s│%s┃%s│%s│%s│%s│%s│v" % (l[23], p4[0][0], p4[1][0], p3[0][3], p3[0][2], p3[0][1], p3[0][0], l[14])
    print " ├──╄──┼──┼──┼──┼──┼──╃──┤ " 
    print " │%s│%s│%s│%s│%s│%s│%s│%s│ " % (l[22], l[21],    l[20],    l[19],    l[18],    l[17],    l[16],    l[15])
    print " └──┴──┴──┴──┴──┴──┴──┴──┘ "
    print "     < 4 ^                 "
            
    
def tarkista_siirto(lauta, pelaaja, kirjain, noppa):
    """Tarkistaa voiko nappulaa nappula siirtää annetun määrän askelia pelilaudalla.
    
    Argumentit:
    lauta   : Pelitilannetta kuvaava lista, gen_pelilauta()-muodossa.
    pelaaja : Vuorossa olevan pelaajan numero, 1-4   
    kirjain : Siirrettävän nappulan kirjain, A-D, voi myös olla muotoa "1A" etc.
    noppa   : Askelmäärä (nopan näyttämä)

    Palauttaa monikon (sallittu, virhe):
    sallittu : True jos siirto on sallittu, False jos ei.
    virhe    : Merkkijono joka kuvaa siirron laittomuuden syytä. Tyhjä jos siirto on sallittu.
    
    """
    
    vikailmoitus = "Käynnistä peli uudestaan ('Q'), jos ongelma toistuu ota yhteys pelin tekijään."    
    
    while True:    
        if len(kirjain) == 1:
            if kirjain.upper() in "ABCD":
                kirjain = kirjain.upper()
                break
            else:
                virhe = "Annoit viallisen syötteen."
                return False, virhe                
        elif len(kirjain) == 2 and kirjain[0].isdigit():        
            if int(kirjain[0]) == pelaaja :
                kirjain = kirjain[1].upper()                                
            elif 1 <= int(kirjain[0]) <= 4:
                virhe = "Vaikka se tuntuisikin hyvältä eleeltä, et voi siirtää vastustajien nappuloita."
                return False, virhe                
            else:
                virhe = "Annoit viallisen syötteen."
                return False, virhe                
        else:
            virhe = "Annoit viallisen syötteen."
            return False, virhe
        
    if 1 <= pelaaja <= 4:
        nappula = str(pelaaja) + kirjain        
    else:
        virhe = "Pelaajan numero on viallinen.", vikailmoitus
        return False, virhe

    pelilauta = lauta[0]
    koti = lauta[pelaaja][0]    
    koti_index = (pelaaja - 1) * 7 # Kotipesästä poistuvien nappuloiden indeksi pelilaudalla 
    maali = lauta[pelaaja][1]
    maali_index = (koti_index - 1) % 28 # Pelaajan maalia edeltävä indeksi pelilaudalla
    
    if nappula in maali:
        virhe = "Et voi siirtää maaliin päässeita nappuloita."
        return False, virhe        
    elif nappula in koti:    
        if noppa != 6:
            virhe = "Tarvitset kuutosen siirtääksesi nappulan kotipesästä!"
            return False, virhe            
        elif pelilauta[koti_index][0] == str(pelaaja):
            virhe = "Et voi siirtää oman nappulasi päälle!"
            return False, virhe
        else:
            return True, ""     
    elif nappula in pelilauta:
        ruutu = pelilauta.index(nappula)
        if 0 <= (maali_index - ruutu) < noppa:      # Toteutuu jos noppalukema siirtäisi nappulan maalialueelle tai sen ohi
            if ruutu + noppa - maali_index > 4:     # Toteutuu jos nappula siirtyisi maalialueen ohi
                virhe = "Maaliruutuun täytyy osua tasaluvulla, etkä voi mennä maalialueen ohi!"
                return False, virhe
            elif maali[ruutu + noppa - maali_index - 1] != "  ": # Toteutuu jos maaliruutu on varattu
                virhe = "Maaliruutuun pitää osua tasaluvulla, etkä voi käyttää samaa ruutua kahdesti!"
                return False, virhe            
            else:
                return True, ""
        else:
            return True, ""
    else:
        virhe = "Nappulaa ei löydy mistään sallitusta ruudusta.", vikailmoitus
        return False, virhe

    
def toteuta_siirto(lauta, pelaaja, kirjain, noppa):
    """
    Siirtää haluttua nappulaa pelilaudalla.
    HUOM: funktio EI tarkista siirron laillisuutta.
    Käytä siihen tarkoitukseen funktiota tarkista_siirto() ennen tämän kutsumista.
    
    """
   
    pelilauta = lauta[0]
    koti = lauta[pelaaja][0]    
    koti_index = (pelaaja - 1) * 7 #Kotipesästä poistuvien nappuloiden indeksi pelilaudalla 
    maali_index = (koti_index - 1) % 28 #Pelaajan maalia edeltävä indeksi pelilaudalla
    
    nappula = str(pelaaja) + kirjain[-1].upper()
    

    
    if nappula in koti:
        print "%s siirsi nappulan %s kotipesästä." % (lauta[pelaaja][2], nappula)
        if pelilauta[koti_index] != "  ":
            lauta = palauta_kotipesaan(lauta, koti_index)
        lauta[pelaaja][0][koti.index(nappula)] = "  "
        lauta[0][koti_index] = nappula
        return lauta
        
    else:
        ruutu = pelilauta.index(nappula)
        kohderuutu = (ruutu + noppa) % 28
        
        if 0 <= (maali_index - ruutu) < noppa:      # Toteutuu jos noppalukema siirtäisi nappulan maalialueelle
            print "%s siirsi nappulan %s maalialueelle." % (lauta[pelaaja][2], nappula)
            maaliruutu = ruutu + noppa - maali_index - 1
            lauta[pelaaja][1][maaliruutu] = nappula
            lauta[0][ruutu] = "  "
            return lauta         
        else:
            print "%s siirsi nappulaa %s." % (lauta[pelaaja][2], nappula)
            if pelilauta[kohderuutu] != "  ":
                lauta = palauta_kotipesaan(lauta, kohderuutu)
            lauta[0][kohderuutu] = nappula
            lauta[0][ruutu] = "  "
            return lauta

            
def palauta_kotipesaan(lauta, i):
    """Siirtää nappulan laudan indeksissä i kotipesään ja tyhjentää ruudun josta se poistetaan.
    Palauttaa pelilautaa kuvaavan listan muokattuna.
    
    """
     
    tapettu_pelaaja = int(lauta[0][i][0])
    tapettu_nappula = lauta[0][i]
    tyhja_kotipaikka = lauta[tapettu_pelaaja][0].index("  ")
    lauta[tapettu_pelaaja][0][tyhja_kotipaikka] = tapettu_nappula
    lauta[0][i] = "  "
    
    print "Samassa rytäkässä %s syötiin ja oksennettiin takaisin kotipesäänsä." % tapettu_nappula
    
    return lauta
            
    
           
def heita_noppaa():
    """Simuloi nopan heiton.
    Palauttaa monikon, jossa:
        luku : Satunnainen väliltä 1-6
        sana : Merkkijono joka kuvaa luvun sanallisesti
        
    """
    
    luku = random.randint(1,6)
    
    if luku == 1: sana = "ykkösen"
    elif luku == 2: sana = "kakkosen"
    elif luku == 3: sana = "kolmosen"
    elif luku == 4: sana = "nelosen"
    elif luku == 5: sana = "viitosen"
    elif luku == 6: sana = "kuutosen"
    return luku, sana
    
def tarkista_lailliset(lauta, pelaaja, noppa):
    """Tarkistaa onko vuorossa olevalla pelaajalla yhtäkään laillista siirtoa nopan näyttämällä luvulla.
    Palauttaa True jos on, False jos ei.
    
    """

    laillinen = False
    
    for i in "ABCD":
        laillinen = tarkista_siirto(lauta, pelaaja, i, noppa)[0]
        if laillinen:
            return True 
                      
    return False
    
def pelaa_vuoro(lauta, pelaaja, ai):
    """Pelaa yhden vuoron Komblea annetulla laudalla.
    Palauttaa noppalukeman käytettäväksi pääohjelmassa.
    
    """
    
    if ai == True:
        noppa, noppa_s = heita_noppaa()
        print "%s heitti %s!" % (lauta[pelaaja][2], noppa_s) 
        
        if tarkista_lailliset(lauta, pelaaja, noppa):        
            while True:
                kirjain = random.choice("ABCD")
                siirto, virhe = tarkista_siirto(lauta, pelaaja, kirjain, noppa)
                
                if siirto:
                    lauta = toteuta_siirto(lauta, pelaaja, kirjain, noppa)
                    break
        else:
            print "Ei yhtäkään laillista siirtoa!"                 
    else:
        tulosta_pelilauta(lauta, pelaaja)
        raw_input("\n%s, ole hyvä ja paina POP-O-MATICia!" % lauta[pelaaja][2])
        noppa, noppa_s = heita_noppaa()
        
        if tarkista_lailliset(lauta, pelaaja, noppa): 
            while True:
                nappula = raw_input("%s, heitit %s. Mitä nappulaa haluat siirtää? (%dA, %dB, %dC, %dD) " 
                                    % (lauta[pelaaja][2], noppa_s,
                                    pelaaja, pelaaja, pelaaja, pelaaja))
                
                if nappula.strip().upper() == "Q":     # Tarkistaa lopetetaanko peli
                    while True:
                        lopetus = raw_input("Haluatko varmasti keskeyttää pelin? (Kyllä/Ei) ")
                        
                        if lopetus.lower() == "k" or lopetus.lower() == "kyllä":
                            sys.exit()
                        elif lopetus.lower() != "e" and lopetus.lower() != "ei":
                            print "Annoit viallisen syötteen."
                        else:
                            break
                elif nappula.strip().lower() == "tilanne":
                    tulosta_pelilauta(lauta, pelaaja)
                else:
                    siirto, virhe = tarkista_siirto(lauta, pelaaja, nappula, noppa)
                    
                    if siirto:
                        lauta = toteuta_siirto(lauta, pelaaja, nappula, noppa)
                        break
                    else:
                        print virhe
        else:
            print "Ei yhtäkään laillista siirtoa!"
    return noppa
def pelaa():
    """
    Pelaa Komblea kunnes joku voittaa.
    
    Pelin päättyessa, palauttaa voittajan nimen ja vuorojen yhteenlasketun määrän monikkona.
    
    """
    
    lauta = gen_pelilauta()
    vuorot = 0
    
    for i in range(1, 5):
        pass
        while True:
            nimi = raw_input("Anna %d. pelaajan nimi: (jätä tyhjäksi kun et halua lisätä ihmispelaajia) " % i)
            if "," in nimi:
                print "Nimessä ei saa olla pilkkuja. Yritä uudestaan."
            else: break
        if not nimi:
            for j in range(1, 6-i):
                nimi = "Bot-%d" % j
                lauta[i + j - 1].append(nimi)
                lauta[i + j - 1].append(True)
            break
        lauta[i].append(nimi[:12])
        lauta[i].append(False)
    
    pelaaja = random.randint(1, 4) # Valitsee aloittajan
    
    print "Peli alkaa! Ensimmäisenä vuorossa: %s!\n" % lauta[pelaaja][2]
    
    n = 0
    while True:
        time.sleep(0.1)
        ai = lauta[pelaaja][3]
        noppa = pelaa_vuoro(lauta, pelaaja, ai)
                
        if "  " not in lauta[pelaaja][1]:       # Toteutuu kun pelaajan maalissa ei ole tyhjiä ruutuja
            print "%s voitti pelin!\n" % lauta[pelaaja][2]
            tulosta_pelilauta(lauta, pelaaja)
            return lauta[pelaaja][2], vuorot
            
        if noppa == 6:        # Asettaa seuraavan vuoron pelaajan.
            print "%s heitti kuutosen, joten hän saa jatkaa!" % lauta[pelaaja][2]
        elif pelaaja == 4:
            pelaaja = 1
            print ""
            vuorot += 1
        else: 
            pelaaja = pelaaja + 1
            print ""
            vuorot += 1
