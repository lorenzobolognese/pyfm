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
from formation import *
from serieA import *

class League(object):
    def __init__(self):
        team1 = Club("Juventus FC")
        tactics, players = Juventus()
        team1.SelectTeam(tactics, players)

        tactics, players = Internazionale()
        team2 = Club("FC Inter Milan")
        team2.SelectTeam(tactics, players)

        tactics, players = Napoli()
        team3 = Club("SSC Napoli")
        team3.SelectTeam(tactics, players)

        tactics, players = Roma()
        team4 = Club("AS Roma")
        team4.SelectTeam(tactics, players)

        tactics, players = Spal()
        team5 = Club("S.P.A.L.")
        team5.SelectTeam(tactics, players)

        self.board = [team1, team2, team3, team4, team5]
        self.scorerRanking = []

    def ShowIntro(self, teamHome, teamAway):
        stats1 = teamHome.formation.GetPlayerStats()
        stats2 = teamAway.formation.GetPlayerStats()
        print(stats1[0] + " vs. " + stats2[0])
        time.sleep(5)
        for line in stats1: print(line)
        time.sleep(5)
        for line in stats2: print(line)
        time.sleep(5)
        print()

    def ShowStats(self, stats1, stats2):
        print(stats1)
        print(stats2)

    def ShowTable(self):
        table = []
        for item in self.board: table.append((item.team.name, item.points))
        print(sorted(table, reverse=True, key=lambda student: student[1]))
        print(sorted(self.scorerRanking, reverse=True, key=lambda student: student[2]))

    def UpdateTable(self, club1, stats1, club2, stats2):
        goal1 = stats1[2]
        goal2 = stats2[2]
        if goal1 > goal2: club1.points = club1.points + 3
        elif goal1 < goal2: club2.points = club2.points + 3
        else:
            club1.points = club1.points + 1
            club2.points = club2.points + 1

    def UpdateScorerRank(self, matchList):
        temp = []
        found = False
        for new in self.scorerRanking:
            score = new[2]
            for old in matchList:
                if new[0] == old[0]:
                    score = score + old[2]
                    break
            temp.append((new[0], new[1], score))

        for new in matchList:
            for old in temp:
                if new[0] == old[0]:
                    found = True
            if found == False: temp.append((new[0], new[1], new[2]))
        self.scorerRanking = temp

    def Play(self, howMany):
        for t1 in self.board:
            for t2 in self.board:
                if t2 is not t1:
                    match = Match(t1, t2)
                    self.ShowIntro(t1, t2)
                    match.start()

                    while (match.isPlaying == True) or (match.isLogEmpty() == False):
                        msg = match.GetLog()
                        print(msg)
                        time.sleep(0.25)

                    stats1, stats2, scorer = match.GetStats()
                    self.UpdateTable(t1, stats1, t2, stats2)
                    self.UpdateScorerRank(scorer)
                    self.ShowTable()

def main():
    championship = League()
    championship.Play(1)

if __name__ == '__main__':
    main()
