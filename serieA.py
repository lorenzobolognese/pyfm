#-------------------------------------------------------------------------------
# Name:        serieA
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     28/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from player import Player

def Internazionale():
    p1  = Player("GK", "", 89, "Handanovic")
    p2  = Player("D", "C", 87, "De Vrij")
    p3  = Player("D", "C", 91, "Skriniar")
    p4  = Player("D", "C", 85, "Godin")
    p5  = Player("M", "L", 82, "D'Ambrosio")
    p6  = Player("M", "C", 80, "Vecino")
    p7  = Player("M", "C", 87, "Barella")
    p8  = Player("M", "C", 86, "Sensi")
    p9  = Player("M", "R", 82, "Candreva")
    p10 = Player("A", "C", 87, "Lautaro Martinez")
    p11 = Player("A", "C", 89, "Lukaku")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Juventus():
    p1  = Player("GK", "", 88, "Szczęsny")
    p2  = Player("D", "L", 85, "Alex Sandro")
    p3  = Player("D", "C", 90, "De Ligt")
    p4  = Player("D", "C", 92, "Bonucci")
    p5  = Player("D", "R", 85, "Cuadrado")
    p6  = Player("M", "C", 85, "Matuidi")
    p7  = Player("M", "C", 89, "Pjanic")
    p8  = Player("M", "C", 85, "Khedira")
    p9  = Player("A", "L", 94, "Cristiano Ronaldo")
    p10 = Player("A", "C", 88, "Higuain")
    p11 = Player("A", "R", 92, "Dybala")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Napoli():
    p1  = Player("GK", "", 82, "Meret")
    p2  = Player("D", "L", 82, "Hysaj")
    p3  = Player("D", "C", 90, "Koulibaly")
    p4  = Player("D", "C", 86, "Manolas")
    p5  = Player("D", "R", 80, "Di Lorenzo")
    p6  = Player("M", "L", 81, "Elmas")
    p7  = Player("M", "C", 90, "Allan")
    p8  = Player("M", "C", 87, "Zielinsky")
    p9  = Player("M", "R", 88, "Fabian Ruiz")
    p10 = Player("A", "C", 85, "Insigne")
    p11 = Player("A", "C", 85, "Mertens")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Roma():
    p1  = Player("GK", "", 82, "Lopez")
    p2  = Player("D", "L", 82, "Spinazzola")
    p3  = Player("D", "C", 90, "Mancini")
    p4  = Player("D", "C", 86, "Smalling")
    p5  = Player("D", "R", 80, "Florenzi")
    p6  = Player("M", "L", 81, "Mkhitaryan")
    p7  = Player("M", "C", 90, "Cristante")
    p8  = Player("M", "C", 87, "Pellegrini")
    p9  = Player("M", "C", 88, "Veretout")
    p10 = Player("M", "R", 85, "Zaniolo")
    p11 = Player("A", "C", 85, "Dzeko")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Spal():
    p1  = Player("GK", "", 74, "Berisha")
    p2  = Player("D", "L", 70, "Reca")
    p3  = Player("D", "C", 76, "Cionek")
    p4  = Player("D", "C", 78, "Vicari")
    p5  = Player("D", "C", 77, "Tomovic")
    p6  = Player("D", "R", 65, "Strefezza")
    p7  = Player("M", "C", 70, "Murgia")
    p8  = Player("M", "C", 85, "Kurtic")
    p9  = Player("M", "C", 75, "Valdifiori")
    p10 = Player("A", "C", 70, "Floccari")
    p11 = Player("A", "C", 83, "Petagna")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

if __name__ == '__main__':
    pass
