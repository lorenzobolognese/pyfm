#-------------------------------------------------------------------------------
# Name:        formation
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

import random
from player import Player

class Formation(object):
    def __init__(self):
        self.playersList = []
        self.dummy = Player(0, 0, 0, 0, 0, ["GK", "D", "M", "A"], ["L", "R", "C"])
        self.name = ""
        self.module = ""
        self.lastStriker = None
        self.chariness = 0

    def Add(self, role, side, player):
        self.playersList.append([role, side, player])

    def Set(self, playing, chariness):
        self.chariness = chariness
        for i in range(0, 11):
            self.playersList[i][2] = playing[i]

    def GetPlayerStats(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        l = []
        for p in self.playersList:
            l.append(p[0] + p[1] + " " + p[2].name + " --> " + str(p[2].GetStats(p[0], p[1])) + ", Energy = " + str(p[2].GetEnergy()) + ", Vote = " + str(p[2].GetVote()) + ", Average = " + str(p[2].GetAvarageVote()))
        return l

    def GetPartyStats(self):
        l = [self.GetAttack()]
        l.append(self.GetMidfield())
        l.append(self.GetDefense())
        l.append(self.GetGoalkeep())
        l.append(self.GetOverall())
        return l

    def GetPlayer(self, role):
        temp = 0
        sum = 0
        for p in self.playersList:
            if p[0] == role: sum = sum + p[2].GetPerformance(role, p[0], p[1])
        whichPlayer = random.randint(0, sum)
        for p in self.playersList:
            if p[0] == role: temp = temp + p[2].GetPerformance(role, p[0], p[1])
            if temp >= whichPlayer: return p

    def AdjustPlayerVote(self, role, direction):
        p = self.GetPlayer(role)
        if direction == "UP": p[2].SetVote(0.5)
        elif direction == "DOWN": p[2].SetVote(-0.5)

    def GetStriker(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        # Increasing of propability it's a midfielder or attacker to attempt the shoot
        dfn = self.GetPlayer("D")
        mid = self.GetPlayer("M")
        atk = self.GetPlayer("A")
        whichPlayer = random.randint(1, 40)
        if whichPlayer < 5: p = dfn
        elif whichPlayer > 4 and whichPlayer < 21: p = mid
        elif whichPlayer > 20: p = atk
        self.lastStriker = p[2]
        return int(p[2].GetPerformance("A", p[0], p[1])), p[0], p[2].name

    def AdjustStrikerVote(self, direction):
        if direction == "UP": self.lastStriker.SetVote(1.0)
        elif direction == "DOWN": self.lastStriker.SetVote(-0.5)

    def GetOverall(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        sum = 0
        for p in self.playersList: sum = sum + p[2].GetPerformance("ALL", p[0], p[1])
        return int(sum)

    def GetAttack(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        sum = 0
        for p in self.playersList: sum = sum + p[2].GetPerformance("A", p[0], p[1])
        return int(sum)

    def GetMidfield(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        sum = 0
        for p in self.playersList: sum = sum + p[2].GetPerformance("M", p[0], p[1])
        return int(sum)

    def GetDefense(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        sum = 0
        for p in self.playersList: sum = sum + p[2].GetPerformance("D", p[0], p[1])
        return int(sum)

    def GetGoalkeep(self):
        # p[0] --> role
        # p[1] --> side
        # p[2] --> player
        sum = 0
        for p in self.playersList: sum = sum + p[2].GetPerformance("GK", p[0], p[1])
        return int(sum)

    def GetHomeBonus(self, zone):
        if zone == "A": power = self.GetAttack()/11
        if zone == "M": power = self.GetMidfield()/11
        if zone == "D": power = self.GetDefense()/11
        if zone == "ALL": power = self.GetOverall()/11
        return int(power)

    def GetChariness(self):
        return self.chariness

class F442(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-4-2"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "L", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "R", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)

class F424(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-2-4"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("A", "L", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "R", self.dummy)

class F433(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-3-3"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("A", "L", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "R", self.dummy)

class F451(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-5-1"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "L", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "R", self.dummy)
        self.Add("A", "C", self.dummy)

class F343(Formation):
    def __init__(self):
        super().__init__()
        self.module = "3-4-3"
        self.Add("GK", "", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("M", "L", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "R", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)

class F352(Formation):
    def __init__(self):
        super().__init__()
        self.module = "3-5-2"
        self.Add("GK", "", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("M", "L", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "R", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)

class F532(Formation):
    def __init__(self):
        super().__init__()
        self.module = "5-3-2"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("A", "C", self.dummy)
        self.Add("A", "C", self.dummy)

class F541(Formation):
    def __init__(self):
        super().__init__()
        self.module = "5-4-1"
        self.Add("GK", "", self.dummy)
        self.Add("D", "L", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "C", self.dummy)
        self.Add("D", "R", self.dummy)
        self.Add("M", "L", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "C", self.dummy)
        self.Add("M", "R", self.dummy)
        self.Add("A", "C", self.dummy)

if __name__ == '__main__':
    test = F451()
    print(test.GetAttack())
    print(test.GetMidfield())
    print(test.GetDefense())
    print(test.GetGoalkeep())