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
from coach import Coach
from formation import *
from serieA import SERIEA

MATCH_INTRO_SPEED_TIMEOUT = 0.0
MATCH_COMMENTARY_SPEED_TIMEOUT = 0.0

class League(object):
    def __init__(self):
        self.scorerRanking = []
        self.board = []
        for item in SERIEA:
            name, tactics, chariness, roster = item()
            playing = Coach(tactics, roster)
            subscribing = Club(name)
            subscribing.SelectTeam(tactics, chariness, playing)
            self.board.append(subscribing)

    def ShowTeams(self):
        for t in self.board:
            stats = t.formation.GetPlayerStats()
            for line in stats: print(line)

    def ShowIntro(self, teamHome, teamAway):
        stats1 = teamHome.formation.GetPlayerStats()
        stats2 = teamAway.formation.GetPlayerStats()
        print(stats1[0] + " vs. " + stats2[0])
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        for line in stats1: print(line)
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        for line in stats2: print(line)
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        print()

    def ShowStats(self, stats1, stats2, t1, t2):
        name1 = t1.formation.GetPlayerStats()
        name2 = t2.formation.GetPlayerStats()
        print(name1[0] + " vs. " + name2[0])
        print(stats1)
        print(stats2)

    def ShowTable(self):
        table = []
        for item in self.board: table.append((item.team.name, item.points, item.played, item.won, item.draw, item.lost, item.goalFor, item.goalAgainst))
        print("CHAMPIONSHIP BOARD")
        teams = sorted(table, reverse=True, key=lambda parameter: parameter[1])
        for t in teams: print(t)
        print()
        print("STRIKERS")
        scorers = sorted(self.scorerRanking, reverse=True, key=lambda parameter: parameter[2])
        for p in scorers: print(p)
        print()

    def UpdateTable(self, club1, stats1, club2, stats2):
        goal1 = stats1[2]
        goal2 = stats2[2]
        club1.played = club1.played + 1
        club1.goalFor = club1.goalFor + goal1
        club1.goalAgainst = club1.goalAgainst + goal2
        club2.played = club2.played + 1
        club2.goalFor = club2.goalFor + goal2
        club2.goalAgainst = club2.goalAgainst + goal1
        if goal1 > goal2:
            club1.points = club1.points + 3
            club1.won = club1.won + 1
            club2.lost = club2.lost + 1
        elif goal1 < goal2:
            club2.points = club2.points + 3
            club2.won = club2.won + 1
            club1.lost = club1.lost + 1
        else:
            club1.draw = club1.draw + 1
            club2.draw = club2.draw + 1
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

    def Play(self):
        for t1 in self.board:
            for t2 in self.board:
                if t2 is not t1:
                    match = Match(t1, t2, isNeutralField = False)
                    self.ShowIntro(t1, t2)
                    match.start()

                    while (match.isPlaying == True) or (match.isLogEmpty() == False):
                        msg = match.GetLog()
                        print(msg)
                        time.sleep(MATCH_COMMENTARY_SPEED_TIMEOUT)

                    stats1, stats2, scorer = match.GetStats()
                    self.ShowStats(stats1, stats2, t1, t2)
                    self.UpdateTable(t1, stats1, t2, stats2)
                    self.UpdateScorerRank(scorer)
                    self.ShowTable()

def main():
    championship = League()
    #championship.ShowTeams()
    championship.Play()

if __name__ == '__main__':
    main()
