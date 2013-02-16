#-*- coding: utf-8 -*-
"""Komble ©2012 Uula Ranta

Kimble-klooni Pythonille.

"""

import komble_peli
import komble_tilastot
import time

if __name__ == "__main__":
    print " |  / ©2012 U. Ranta |     |     "
    print " ' /  _ \  __ `__ \  __ \  |  _ \\"
    print " . \ (   | |   |   | |   | |  __/"
    print "_|\_\___/ _|  _|  _|_.__/ _|\___|\n"
    
    print "Tervetuloa Kombleen!"
    
    while True:
        print "Syötä mitä haluat tehdä:\n"
        
        print "Pelata Komblea     : Komble"
        print "Katsella tilastoja : Tilastot"
        print "Poistua            : Quit\n"
        
        moodi = raw_input("> ").lower()
        
        if moodi:
            if moodi == "komble":
                aloitusaika = time.time()
                voittaja, vuorot = komble_peli.pelaa()
                lopetusaika = time.time()
                peliaika = lopetusaika - aloitusaika
                pvm = time.strftime("%a %d.%m.%Y")
                komble_tilastot.tilastoi_peli(voittaja, peliaika, pvm, vuorot)
       
                
                print "Voittaja tallennettu tilastoihin. Kiitos pelaamisesta!\n"
                              
            elif moodi == "tilastot":
                komble_tilastot.selaa()
                
            elif moodi == "quit":
                print "\nJoku toinen kerta uudelleen!\n"
                import sys
                sys.exit()
        else:
            print "Anna syöte!\n"
    
    peli.peli()