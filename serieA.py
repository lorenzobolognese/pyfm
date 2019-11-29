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

def Juventus():
    p1  = Player("GK", "", 88, "Wojciech Szczęsny")
    p2  = Player("D", "L", 85, "Alex Sandro")
    p3  = Player("D", "C", 90, "Matthijs de Ligt")
    p4  = Player("D", "C", 92, "Leonardo Bonucci")
    p5  = Player("D", "R", 85, "Juan Cuadrado")
    p6  = Player("M", "C", 85, "Blaise Matuidi")
    p7  = Player("M", "C", 89, "Miralem Pjanic")
    p8  = Player("M", "C", 85, "Sami Khedira")
    p9  = Player("A", "L", 94, "Cristiano Ronaldo")
    p10 = Player("A", "C", 88, "Gonzalo Higuain")
    p11 = Player("A", "R", 92, "Paulo Dybala")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Internazionale():
    p1  = Player("GK", "", 89, "Samir Handanovic")
    p2  = Player("D", "C", 87, "Stefan De Vrij")
    p3  = Player("D", "C", 91, "Milan Skriniar")
    p4  = Player("D", "C", 85, "Diego Godin")
    p5  = Player("M", "L", 82, "Danilo D'Ambrosio")
    p6  = Player("M", "C", 80, "Matias Vecino")
    p7  = Player("M", "C", 87, "Nicolò Barella")
    p8  = Player("M", "C", 86, "Stefano Sensi")
    p9  = Player("M", "R", 82, "Antonio Candreva")
    p10 = Player("A", "C", 87, "Lautaro Martinez")
    p11 = Player("A", "C", 89, "Romelo Lukaku")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

if __name__ == '__main__':
    pass
