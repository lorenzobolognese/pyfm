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

MATCH_INTRO_SPEED_TIMEOUT = 0.0
MATCH_COMMENTARY_SPEED_TIMEOUT = 0.0

class League(object):
    def __init__(self):
        name, tactics, chariness, players = Juventus()
        team1 = Club(name)
        team1.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Internazionale()
        team2 = Club(name)
        team2.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Napoli()
        team3 = Club(name)
        team3.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Roma()
        team4 = Club(name)
        team4.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Spal()
        team5 = Club(name)
        team5.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Brescia()
        team6 = Club(name)
        team6.SelectTeam(tactics, chariness, players)

        name, tactics, chariness, players = Cagliari()
        team7 = Club(name)
        team7.SelectTeam(tactics, chariness, players)

        self.board = [team1, team2, team3, team4, team5, team6, team7]
        self.scorerRanking = []

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
                        time.sleep(MATCH_COMMENTARY_SPEED_TIMEOUT)

                    stats1, stats2, scorer = match.GetStats()
                    self.ShowStats(stats1, stats2, t1, t2)
                    self.UpdateTable(t1, stats1, t2, stats2)
                    self.UpdateScorerRank(scorer)
                    self.ShowTable()

def main():
    championship = League()
    championship.Play(1)

if __name__ == '__main__':
    main()
