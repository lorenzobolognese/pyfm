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
from berger import Draw
from serieA import SERIEA

MATCH_MASKS_TIMEOUT = 5.0
MATCH_COMMENTARY_SPEED_TIMEOUT = 0.25

class League(object):
    def __init__(self):
        self.scorerRanking = []
        self.board = []
        self.result = []
        for challenger in SERIEA:
            name, tactics, chariness, roster = challenger()
            subscribe = Club(name, tactics, chariness, roster)
            self.board.append(subscribe)

    def ShowTactics(self, team, timeout):
        stats = team.tactics.GetPlayerStats()
        print(team.name + " (" + team.tactics.module + ")")
        for line in stats: print(line)
        print()
        time.sleep(timeout)

    def ShowIntro(self, teamHome, teamAway, timeout):
        print("--- " + teamHome.name + " vs. " + teamAway.name + " ---")
        print()
        self.ShowTactics(teamHome, timeout)
        self.ShowTactics(teamAway, timeout)
        print(" ---> Kick Off!!! <---")

    def ShowStats(self, statsHome, statsAway, teamHome, teamAway, timeout):
        print(" ---> Final whistle <---")
        print()
        print("MATCH STATS (attempts, shoots, goals)")
        print(teamHome.name + ": " + str(statsHome))
        print(teamAway.name + ": " + str(statsAway))
        print()
        time.sleep(timeout)

    def ShowTable(self, timeout):
        table = []
        for item in self.board: table.append((item.name, item.points, item.played, item.won, item.draw, item.lost, item.goalFor, item.goalAgainst))
        print("CHAMPIONSHIP BOARD")
        teams = sorted(table, reverse=True, key=lambda parameter: parameter[1])
        for t in teams: print(t)
        print()
        time.sleep(timeout)
        print("STRIKERS")
        scorers = sorted(self.scorerRanking, reverse=True, key=lambda parameter: parameter[2])
        for p in scorers: print(p)
        print()
        time.sleep(timeout)

    def ShowRound(self, calendar, matches, idx, timeout):
        result = ""
        if (idx % matches) == 0:
            # Last round results
            if (idx > 0):
                print("ROUND " + str((int((idx-1)/matches))+1) + ": FINAL RESULTS")
                for i in range(0, matches):
                    if (len(self.result) > 0): result = self.result.pop(0)
                    print(calendar[idx-matches+i][0].name + " vs. " + calendar[idx-matches+i][1].name + ": " + str(result[0]) + " - " + str(result[1]))
                print()

            # Next round table
            print("ROUND " + str((int(idx/matches))+1))
            for i in range(0, matches):
                print(calendar[idx+i][0].name + " vs. " + calendar[idx+i][1].name)
            print()
            time.sleep(timeout)

    def UpdateRound(self, stats1, stats2):
        goal1 = stats1[2]
        goal2 = stats2[2]
        self.result.append([goal1, goal2])

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
        calendar = Draw(self.board)
        for i in range (0, len(calendar)):
            teams = len(self.board) # 20
            matches = int(teams/2) # 10
            rounds = int(len(calendar)/matches) #38

            # Show last round results and new round matches
            self.ShowRound(calendar, int(len(self.board)/2), i, MATCH_MASKS_TIMEOUT)

            # Get teams to play
            club1 = calendar[i][0]
            club2 = calendar[i][1]

            # Home team
            playing = Coach(club1.tactics, club1.roster)
            club1.SelectTeam(club1.tactics, club1.chariness, playing)

            # Away team
            playing = Coach(club2.tactics, club2.roster)
            club2.SelectTeam(club2.tactics, club2.chariness, playing)

            # Play match
            match = Match(club1, club2, isNeutralField = False)
            self.ShowIntro(club1, club2, MATCH_MASKS_TIMEOUT)
            match.start()

            # Print out commentary
            while (match.isPlaying == True) or (match.isLogEmpty() == False):
                msg = match.GetLog()
                print(msg)
                time.sleep(MATCH_COMMENTARY_SPEED_TIMEOUT)

            # Match and league statistics
            stats1, stats2, scorer = match.GetStats()
            self.ShowStats(stats1, stats2, club1, club2, MATCH_MASKS_TIMEOUT)
            self.UpdateTable(club1, stats1, club2, stats2)
            self.UpdateScorerRank(scorer)
            self.UpdateRound(stats1, stats2)
            self.ShowTable(MATCH_MASKS_TIMEOUT)

def main():
    championship = League()
    championship.Play()

if __name__ == '__main__':
    main()
