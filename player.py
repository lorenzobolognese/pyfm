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
    def __init__(self, rateA, rateM, rateD, rateGK, stamina, role, side, name = "John Doe"):
        self.role = role
        self.side = side
        self.rateA = rateA
        self.rateM = rateM
        self.rateD = rateD
        self.rateGK = rateGK
        self.stamina = stamina
        self.name = name

        self.VoidVote()
        self.ResetPlayedMatches()
        self.ResetTotalVote()
        self.ResetEnergy()

    def GetStats(self, fieldRole, fieldSide):
        if fieldRole in self.role: r = 100
        else: r = 50
        if (fieldRole == "GK") or (fieldSide in self.side): p = 100
        else: p = 50
        return int(self.rateA*(r/100)*(p/100)), int(self.rateM*(r/100)*(p/100)), int(self.rateD*(r/100)*(p/100)), int(self.rateGK*(r/100)*(p/100))

    def GetPerformance(self, zone, fieldRole, fieldSide):
        a, m, d, gk = self.GetStats(fieldRole, fieldSide)
        if zone == "A": power = a
        if zone == "M": power = m
        if zone == "D": power = d
        if zone == "GK": power = gk
        if zone == "ALL": power = a + m + d + gk
        return int(power)

    def ResetEnergy(self):
        self.energy = self.stamina

    def SetEnergy(self):
        if (self.energy > 0): self.energy = self.energy - 1

    def GetEnergy(self):
        return self.energy

    def VoidVote(self):
        self.vote = 0.0

    def ResetVote(self):
        self.vote = 6.0

    def SetVote(self, delta):
        self.vote = self.vote + delta
        if self.vote > 10.0: self.vote = 10.0
        elif self.vote < 0.0: self.vote = 0.0

    def GetVote(self):
        return self.vote

    def ResetTotalVote(self):
        self.totalVote = 0.0

    def SetTotalVote(self):
        self.totalVote = self.totalVote + self.vote

    def ResetPlayedMatches(self):
        self.played = 0

    def SetPlayedMatches(self):
        self.played = self.played + 1

    def GetPlayedMatches(self):
        return self.played

    def GetAvarageVote(self):
        if self.played > 0: return round(self.totalVote/self.played, 1)
        else: return 0.0

if __name__ == '__main__':
    pass
