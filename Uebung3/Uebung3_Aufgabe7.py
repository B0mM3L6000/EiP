import random

rnd = random.randint(0,10)   #setzen der zufälligen zahl
check = False #bedingung für die schleife des spiels selber
check2 = False #bedingung für das ganze programm


while check2 == False:     #wird ausgeführt solange gespielt werden soll
    while check == False:      #ein ratedurchgang
        check3 = False      #bedingung für den ja/nein check später
        n = int(input("Rate eine Zahl: "))

        if n == rnd:     #wenn richtig geraten
            check = True   #ausbrechen aus dem ratedurchgang
            print("Richtig geraten!")
        else:     #wenn falsch geraten
            print("Falsch geraten!")
            if n < rnd:    #ob kleiner oder größer
                print("Die gesuchte Zahl ist größer.")
            else:
                print("Die gesuchte Zahl ist kleiner.")

    while check3 == False:   #soll nochmal gespielt werden?
        wiederholen = input("Nochmal? (y/n)")

        if wiederholen == "y":
            check3 = True   #ausbrechen aus der abfrage
            check = False   #zurücksetzen für nächsten ratedurchgang
            rnd = random.randint(0,10)   #erneutes setzen der zufallszahl für die nächste Runde
        elif wiederholen == "n":
            check3 = True    #ausbrechen aus abfrage
            check2 = True     #ausbrechen aus gesamten programm
        else:
            print("Ungültige Eingabe.")    #wenn etwas anderes als y oder n eingegeben wird
