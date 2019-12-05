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
        for challenger in SERIEA:
            name, tactics, chariness, roster = challenger()
            subscribe = Club(name, tactics, chariness, roster)
            self.board.append(subscribe)

    def ShowIntro(self, teamHome, teamAway):
        stats1 = teamHome.tactics.GetPlayerStats()
        stats2 = teamAway.tactics.GetPlayerStats()
        print(teamHome.name + " vs. " + teamAway.name)
        print(teamHome.tactics.module + " vs. " + teamAway.tactics.module)
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        for line in stats1: print(line)
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        for line in stats2: print(line)
        time.sleep(MATCH_INTRO_SPEED_TIMEOUT)
        print()

    def ShowStats(self, stats1, stats2, teamHome, teamAway):
        print(teamHome.name + " vs. " + teamAway.name)
        print(stats1)
        print(stats2)

    def ShowTable(self):
        table = []
        for item in self.board:
            table.append((item.name, item.points, item.played, item.won, item.draw, item.lost, item.goalFor, item.goalAgainst))
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
        for club1 in self.board:
            for club2 in self.board:
                if club2 is not club1:
                    # Home team
                    playing = Coach(club1.tactics, club1.roster)
                    club1.SelectTeam(club1.tactics, club1.chariness, playing)

                    # Away team
                    playing = Coach(club2.tactics, club2.roster)
                    club2.SelectTeam(club2.tactics, club2.chariness, playing)

                    # Play match
                    match = Match(club1, club2, isNeutralField = False)
                    self.ShowIntro(club1, club2)
                    match.start()

                    while (match.isPlaying == True) or (match.isLogEmpty() == False):
                        msg = match.GetLog()
                        print(msg)
                        time.sleep(MATCH_COMMENTARY_SPEED_TIMEOUT)

                    stats1, stats2, scorer = match.GetStats()
                    self.ShowStats(stats1, stats2, club1, club2)
                    self.UpdateTable(club1, stats1, club2, stats2)
                    self.UpdateScorerRank(scorer)
                    self.ShowTable()

def main():
    championship = League()
    championship.Play()

if __name__ == '__main__':
    main()
