#-------------------------------------------------------------------------------
# Name:        sim
# Purpose:
#
# Author:      bolognes
#
# Created:     28/11/2019
# Copyright:   (c) bolognes 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
from match import Match
from formation import F442, F352
from team import Team
from player import Player

class Team1(object):
    def __init__(self):
        super().__init__()
        t = Team("Bianconera")
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

        t.Add(p1)
        t.Add(p2)
        t.Add(p3)
        t.Add(p4)
        t.Add(p5)
        t.Add(p6)
        t.Add(p7)
        t.Add(p8)
        t.Add(p9)
        t.Add(p10)
        t.Add(p11)

        self.f = F352()
        self.f.Set(t)

class Team2(object):
    def __init__(self):
        super().__init__()
        t = Team("Rossonera")

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

        t.Add(p1)
        t.Add(p2)
        t.Add(p3)
        t.Add(p4)
        t.Add(p5)
        t.Add(p6)
        t.Add(p7)
        t.Add(p8)
        t.Add(p9)
        t.Add(p10)
        t.Add(p11)

        self.f = F442()
        self.f.Set(t)

class Board(object):
    def __init__(self):
        self.team1 = Team1()
        self.team2 = Team2()

        self.points1 = 0
        self.points2 = 0

        self.goalsFor1 = 0
        self.goalsFor2 = 0

        self.goalsAgainst1 = 0
        self.goalsAgainst2 = 0

        self.won1 = 0
        self.won2 = 0

        self.lost1 = 0
        self.lost2 = 0

        self.draw1 = 0
        self.draw2 = 0

    def Update(self, goal1, goal2):
        self.goalsFor1 = self.goalsFor1 + goal1
        self.goalsFor2 = self.goalsFor2 + goal2

        self.goalsAgainst1 = self.goalsAgainst1 + goal2
        self.goalsAgainst2 = self.goalsAgainst2 + goal1

        if goal1 > goal2:
            self.points1 = self.points1 + 3
            self.won1 = self.won1 + 1
            self.lost2 = self.lost2 + 1
        elif goal1 < goal2:
            self.points2 = self.points2 + 3
            self.won2 = self.won2 + 1
            self.lost1 = self.lost1 + 1
        else:
            self.points1 = self.points1 + 1
            self.points2 = self.points2 + 1
            self.draw1 = self.draw1 + 1
            self.draw2 = self.draw2 + 1

    def ShowIntro(self):
        self.team1.f.ShowPlayerStats()
        time.sleep(10)
        print()
        self.team2.f.ShowPlayerStats()
        time.sleep(10)
        print()

    def ShowBoard(self):
        print(self.team1.f.name + " " + str(self.points1) + " " + str(self.won1) + " " + str(self.lost1) + " " + str(self.draw1) + " " + str(self.goalsFor1) + " " + str(self.goalsAgainst1))
        print(self.team2.f.name + " " + str(self.points2) + " " + str(self.won2) + " " + str(self.lost2) + " " + str(self.draw2) + " " + str(self.goalsFor2) + " " + str(self.goalsAgainst2))
        time.sleep(10)

    def Run(self, howMany):
        for i in range(0, howMany):
            m = Match(self.team1.f, self.team2.f)
            goal1, goal2 = m.Play()
            m.ShowStats()
            self.Update(goal1, goal2)
            self.ShowBoard()

def main():
    championship = Board()
    championship.ShowIntro()
    championship.Run(10)


if __name__ == '__main__':
    main()
