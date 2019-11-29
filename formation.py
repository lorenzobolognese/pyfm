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

    def Add(self, role, side, player):
        self.playersList.append([role, side, player])

    def Set(self, team):
        self.name = team.name
        for i in range(0, 11):
            r = team.roster[i]
            self.playersList[i][2] = team.roster[i]

    def GetPlayerStats(self):
        l = [self.name]
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
        p = self.playersList[random.randint(1, 10)]
        return int(p[2].GetPerformance(p[0], p[1], True)), p[0], p[2].name

    def GetOverall(self):
        sum = 0
        for p in self.playersList:
            sum = sum + p[2].GetPerformance(p[0], p[1])
        return int(sum)

    def GetAttack(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["A"]: sum = sum + p[2].GetPerformance(p[0], p[1])
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetMidfield(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])
            if p[0] in ["A", "D"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetDefense(self):
        sum = 0
        for p in self.playersList:
            if p[0] in ["D"]: sum = sum + p[2].GetPerformance(p[0], p[1])
            if p[0] in ["M"]: sum = sum + p[2].GetPerformance(p[0], p[1])/2
        return int(sum)

    def GetGoalkeep(self):
        sum = 0
        for p in self.playersList:
            if p[0] == "GK": sum = sum + p[2].GetPerformance(p[0], p[1])
        return int(sum)

class F442(Formation):
    def __init__(self):
        super().__init__()
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

class F352(Formation):
    def __init__(self):
        super().__init__()
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

if __name__ == '__main__':
    pass
