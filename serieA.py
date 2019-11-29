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
    p1 = Player("GK", "", 90, "Gigi")
    p2 = Player("D", "C", 85, "Carlos")
    p3 = Player("D", "C", 85, "Paulo")
    p4 = Player("D", "C", 91, "Giorgio")
    p5 = Player("M", "L", 90, "Gianluca")
    p6 = Player("M", "C", 92, "Pavel")
    p7 = Player("M", "C", 88, "Miralem")
    p8 = Player("M", "C", 85, "Paul")
    p9 = Player("M", "R", 85, "Angelo")
    p10 = Player("A", "C", 91, "Alessandro")
    p11 = Player("A", "C", 88, "Gonzalo")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

def Milan():
    p1 = Player("GK", "", 60, "Seba")
    p2 = Player("D", "L", 65, "Paolo")
    p3 = Player("D", "C", 65, "Franco")
    p4 = Player("D", "C", 67, "Ale")
    p5 = Player("D", "R", 59, "Cafu")
    p6 = Player("M", "L", 70, "Ricardo")
    p7 = Player("M", "C", 71, "Gennaro")
    p8 = Player("M", "C", 80, "Andrea")
    p9 = Player("M", "R", 71, "Dejan")
    p10 = Player("A", "C", 69, "Marco")
    p11 = Player("A", "C", 67, "George")
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

if __name__ == '__main__':
    pass
