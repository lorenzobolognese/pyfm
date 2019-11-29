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
from club import Club
from formation import F442, F352
from serieA import Juventus, Milan

class Board(object):
    def __init__(self):
        self.team1 = Club("Juventus FC")
        self.team1.SelectTeam(Juventus())
        self.team1.SelectFormation(F352)

        self.team2 = Club("AC Milan")
        self.team2.SelectTeam(Milan())
        self.team2.SelectFormation(F442)

    def ShowIntro(self):
        self.team1.formation.ShowPlayerStats()
        time.sleep(10)
        print()
        self.team2.formation.ShowPlayerStats()
        time.sleep(10)
        print()

    def Run(self, howMany):
        for i in range(0, howMany):
            m = Match(self.team1.formation, self.team2.formation)
            goal1, goal2 = m.Play()
            m.ShowStats()

def main():
    championship = Board()
    championship.ShowIntro()
    championship.Run(1)


if __name__ == '__main__':
    main()
