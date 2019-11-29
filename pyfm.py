#-------------------------------------------------------------------------------
# Name:        pyfm
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     28/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

import time
from match import Match
from club import Club
from formation import F442, F433, F352
from serieA import Juventus, Internazionale

class League(object):
    def __init__(self):
        self.team1 = Club("Juventus FC")
        self.team1.SelectTeam(Juventus())
        self.team1.SelectFormation(F433)

        self.team2 = Club("FC Inter Milan")
        self.team2.SelectTeam(Internazionale())
        self.team2.SelectFormation(F352)

    def ShowIntro(self):
        stats1 = self.team1.formation.GetPlayerStats()
        stats2 = self.team2.formation.GetPlayerStats()
        print(stats1)
        print(stats2)
        time.sleep(5)
        print()

    def Play(self, howMany):
        for i in range(0, howMany):
            match = Match(self.team1, self.team2)
            match.start()

            while (match.isPlaying == True) or (match.isLogEmpty() == False):
                msg = match.GetLog()
                print(msg)
                time.sleep(0.5)

            print(match.GetStats())

def main():
    championship = League()
    championship.ShowIntro()
    championship.Play(10)

if __name__ == '__main__':
    main()
