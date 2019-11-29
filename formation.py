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
        self.name = ""
        self.module = ""

    def Add(self, role, side, player):
        self.playersList.append([role, side, player])

    def Set(self, team):
        self.name = team.name
        for i in range(0, 11):
            r = team.roster[i]
            self.playersList[i][2] = team.roster[i]

    def GetPlayerStats(self):
        l = [self.name, self.module]
        for p in self.playersList:
            l.append(p[0] + p[1] + " " + p[2].name + " --> " + str(p[2].GetPerformance(p[0], p[1])))
        return l

    def GetPartyStats(self):
        l = [self.GetAttack()]
        l.append(self.GetMidfield())
        l.append(self.GetDefense())
        l.append(self.GetGoalkeep())
        l.append(self.GetOverall())
        return l

    def GetStrike(self):
        sum = 0
        # Increasing of propability it's a midfielder or attacker to attempt the shoot
        whichPlayer = random.randint(1, 40)
        if whichPlayer > 10 and whichPlayer < 21: whichPlayer = random.randint(5, 10)
        elif whichPlayer > 20: whichPlayer = random.randint(8, 10)

        p = self.playersList[whichPlayer]
        return int(p[2].GetPerformance(p[0], p[1], True)*2), p[0], p[2].name

    def GetOverall(self):
        sum = 0
        for p in self.playersList:
            sum = sum + p[2].GetPerformance(p[0], p[1])*2
        return int(sum)

    def GetAttack(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["A"]: sum = sum + p[2].GetPerformance(p[0], p[1])*2
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetMidfield(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])*2
            if p[0] in ["A", "D"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetDefense(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["D"]: sum = sum + p[2].GetPerformance(p[0], p[1])*2
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetGoalkeep(self):
        sum = 0
        for p in self.playersList:
            if p[0] == "GK": sum = sum + p[2].GetPerformance(p[0], p[1])*2
        return int(sum)

class F442(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-4-2"
        self.dummy = Player(["GK", "D", "M", "A"], ["L", "R", "C"], 0)
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

class F433(Formation):
    def __init__(self):
        super().__init__()
        self.module = "4-3-3"
        self.dummy = Player(["GK", "D", "M", "A"], ["L", "R", "C"], 0)
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
        self.dummy = Player(["GK", "D", "M", "A"], ["L", "R", "C"], 0)
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

class F352(Formation):
    def __init__(self):
        super().__init__()
        self.module = "3-5-2"
        self.dummy = Player(["GK", "D", "M", "A"], ["L", "R", "C"], 0)
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
        self.dummy = Player(["GK", "D", "M", "A"], ["L", "R", "C"], 0)
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

if __name__ == '__main__':
    pass
