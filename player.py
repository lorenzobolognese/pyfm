#-------------------------------------------------------------------------------
# Name:        player
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class Player(object):
    def __init__(self, rateA, rateM, rateD, rateGK, role, side, name = "John Doe"):
        self.role = role
        self.side = side
        self.rateA = rateA
        self.rateM = rateM
        self.rateD = rateD
        self.rateGK = rateGK
        self.name = name

    def GetStats(self, fieldRole, fieldSide):
        if fieldRole in self.role: r = 100
        else: r = 50
        if (fieldRole == "GK") or (fieldSide in self.side): p = 100
        else: p = 50
        return self.rateA*(r/100)*(p/100), self.rateM*(r/100)*(p/100), self.rateD*(r/100)*(p/100), self.rateGK*(r/100)*(p/100)

    def GetPerformance(self, zone, fieldRole, fieldSide):
        a, m, d, gk = self.GetStats(fieldRole, fieldSide)
        if zone == "A": power = a
        if zone == "M": power = m
        if zone == "D": power = d
        if zone == "GK": power = gk
        if zone == "ALL": power = a + m + d + gk
        return power

if __name__ == '__main__':
    pass
