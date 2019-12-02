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
from formation import *

def Juventus():
    tactics = F433
    chariness = 2
    # Ratings:   A   M   D   GK
    p1  = Player(10, 17, 38, 87, "GK", "", "Szczęsny")
    p2  = Player(50, 52, 84, 0, "D", "L", "Alex Sandro")
    p3  = Player(60, 43, 87, 0, "D", "C", "De Ligt")
    p4  = Player(67, 70, 88, 0, "D", "C", "Bonucci")
    p5  = Player(82, 80, 75, 0, ["D", "M", "A"], "R", "Cuadrado")
    p6  = Player(73, 88, 80, 0 , "M", "C", "Matuidi")
    p7  = Player(78, 90, 73, 0, "M", "C", "Pjanic")
    p8  = Player(69, 87, 78, 0, ["D", "M"], ["R", "C"], "Khedira")
    p9  = Player(94, 85, 55, 0, "A", ["L", "R", "C"], "Cristiano Ronaldo")
    p10 = Player(88, 70, 45, 0, "A", "C", "Higuain")
    p11 = Player(90, 86, 51, 0, "A", ["L", "R", "C"], "Dybala")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Internazionale():
    tactics = F352
    chariness = 2
    # Ratings:   A   M   D   GK
    p1  = Player(10, 20, 29, 90, "GK", "", "Handanovic")
    p2  = Player(51, 37, 85, 0, "D", ["R", "C"], "De Vrij")
    p3  = Player(44, 39, 90, 0, "D", "C", "Skriniar")
    p4  = Player(60, 45, 83, 0, "D", "C", "Godin")
    p5  = Player(58, 40, 80, 0, "M", "L", "D'Ambrosio")
    p6  = Player(60, 80, 54, 0, "M", ["R", "C"], "Vecino")
    p7  = Player(77, 85, 66, 0, "M", ["R", "C"], "Barella")
    p8  = Player(79, 86, 70, 0, "M", ["R", "C"], "Sensi")
    p9  = Player(70, 82, 41, 0, "M", "R", "Candreva")
    p10 = Player(85, 70, 33, 0, "A", ["L", "R", "C"], "Lautaro Martinez")
    p11 = Player(88, 51, 45, 0, "A", "C", "Lukaku")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Napoli():
    tactics = F442
    chariness = 2
    # Ratings:   A   M   D   GK
    p1  = Player(10, 21, 32, 82, "GK", "", "Meret")
    p2  = Player(24, 41, 79, 0, "D", "L", "Hysaj")
    p3  = Player(32, 34, 88, 0, "D", "C", "Koulibaly")
    p4  = Player(34, 40, 84, 0, "D", "C", "Manolas")
    p5  = Player(21, 43, 75, 0, "D", "R", "Di Lorenzo")
    p6  = Player(60, 76, 67, 0, "M", "L", "Elmas")
    p7  = Player(62, 88, 59, 0, "M", "C", "Allan")
    p8  = Player(75, 83, 42, 0, "M", "C", "Zielinsky")
    p9  = Player(75, 83, 56, 0, "M", ["R", "C"], "Fabian Ruiz")
    p10 = Player(82, 82, 13, 0, "A", ["L", "C"], "Insigne")
    p11 = Player(88, 71, 34, 0, "A", ["L", "R", "C"], "Mertens")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Roma():
    tactics = F451
    chariness = 1
    # Ratings:   A   M   D   GK
    p1  = Player(10, 13, 26, 79, "GK", "", "Lopez")
    p2  = Player(37, 44, 76, 0, "D", "L", "Spinazzola")
    p3  = Player(33, 32, 74, 0, "D", "C", "Mancini")
    p4  = Player(23, 27, 80, 0, "D", "C", "Smalling")
    p5  = Player(65, 79, 78, 0, ["D", "M,"], "R", "Florenzi")
    p6  = Player(65, 77, 46, 0, "M", ["L", "C"], "Mkhitaryan")
    p7  = Player(71, 81, 34, 0, ["M", "A"], ["R", "C"], "Cristante")
    p8  = Player(55, 78, 53, 0, "M", "C", "Pellegrini")
    p9  = Player(62, 83, 69, 0, "M", ["R", "C"], "Veretout")
    p10 = Player(76, 86, 32, 0, ["M", "A"], "R", "Zaniolo")
    p11 = Player(86, 65, 19, 0, "A", "C", "Dzeko")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Spal():
    tactics = F532
    chariness = 3
    # Ratings:   A   M   D   GK
    p1  = Player(10, 12, 34, 73, "GK", "", "Berisha")
    p2  = Player(33, 30, 61, 0, "D", "L", "Reca")
    p3  = Player(18, 45, 80, 0, "D", "C", "Cionek")
    p4  = Player(31, 40, 71, 0, "D", "C", "Vicari")
    p5  = Player(20, 56, 76, 0, ["D", "M"], "C", "Tomovic")
    p6  = Player(43, 55, 60, 0, "D", "R", "Strefezza")
    p7  = Player(52, 75, 45, 0, "M", "C", "Murgia")
    p8  = Player(71, 82, 44, 0, "M", ["R", "C"], "Kurtic")
    p9  = Player(60, 77, 39, 0, ["D", "M"], "C", "Valdifiori")
    p10 = Player(72, 65, 40, 0, "A", "C", "Floccari")
    p11 = Player(83, 54, 33, 0, "A", "C", "Petagna")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Brescia():
    tactics = F352
    chariness = 3
    # Ratings:   A   M   D   GK
    p1  = Player(10, 10, 23, 63, "GK", "", "Ironen")
    p2  = Player(32, 35, 58, 0, "D", "C", "Mangraviti")
    p3  = Player(29, 47, 69, 0, "D", "C", "Cistana")
    p4  = Player(30, 56, 65, 0, "D", "C", "Chancellor")
    p8  = Player(63, 70, 45, 0, "M", ["L", "C"], "Sabelli")
    p5  = Player(64, 83, 62, 0, "M", "C", "Tonali")
    p6  = Player(47, 69, 45, 0, "M", ["C", "R"], "Ndoj")
    p7  = Player(50, 70, 67, 0, ["D", "M"], ["R", "C"], "Romulo")
    p9  = Player(64, 73, 32, 0, "M", "R", "Martella")
    p10 = Player(65, 45, 39, 0, "A", "C", "Torregrossa")
    p11 = Player(84, 30, 12, 0, "A", "C", "Balotelli")
    return tactics, chariness, [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

if __name__ == '__main__':
    pass
