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
from config import MATCH_MASKS_TIMEOUT, MATCH_COMMENTARY_SPEED_TIMEOUT, LEAGUE

class League(object):
    def __init__(self, league):
        self.scorerRanking = []
        self.board = []
        self.result = []
        for challenger in league:
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
        self.ShowTactics(teamHome, timeout)
        self.ShowTactics(teamAway, timeout)

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

    def UpdateRound(self, statsHome, statsAway):
        goalHome = statsHome[2]
        goalAway = statsAway[2]
        self.result.append([goalHome, goalAway])

    def UpdateTable(self, clubHome, statsHome, clubAway, statsAway):
        goalHome = statsHome[2]
        goalAway = statsAway[2]
        clubHome.played = clubHome.played + 1
        clubHome.goalFor = clubHome.goalFor + goalHome
        clubHome.goalAgainst = clubHome.goalAgainst + goalAway
        clubAway.played = clubAway.played + 1
        clubAway.goalFor = clubAway.goalFor + goalAway
        clubAway.goalAgainst = clubAway.goalAgainst + goalHome
        if goalHome > goalAway:
            clubHome.points = clubHome.points + 3
            clubHome.won = clubHome.won + 1
            clubAway.lost = clubAway.lost + 1
        elif goalHome < goalAway:
            clubAway.points = clubAway.points + 3
            clubAway.won = clubAway.won + 1
            clubHome.lost = clubHome.lost + 1
        else:
            clubHome.draw = clubHome.draw + 1
            clubAway.draw = clubAway.draw + 1
            clubHome.points = clubHome.points + 1
            clubAway.points = clubAway.points + 1

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
        calendar = Draw(self.board, shuffle = True)
        for i in range (0, len(calendar)):
            teams = len(self.board) # 20
            matches = int(teams/2) # 10
            rounds = int(len(calendar)/matches) #38

            # Show last round results and new round matches
            self.ShowRound(calendar, int(len(self.board)/2), i, MATCH_MASKS_TIMEOUT)

            # Get teams to play
            clubHome = calendar[i][0]
            clubAway = calendar[i][1]

            # Home team
            playing = Coach(clubHome.tactics, clubHome.roster)
            clubHome.SelectTeam(clubHome.tactics, clubHome.chariness, playing)

            # Away team
            playing = Coach(clubAway.tactics, clubAway.roster)
            clubAway.SelectTeam(clubAway.tactics, clubAway.chariness, playing)

            # Play match
            match = Match(clubHome, clubAway, isNeutralField = False)
            self.ShowIntro(clubHome, clubAway, MATCH_MASKS_TIMEOUT)
            match.start()

            # Print out commentary
            while (match.isPlaying == True) or (match.isLogEmpty() == False):
                msg = match.GetLog()
                print(msg)
                time.sleep(MATCH_COMMENTARY_SPEED_TIMEOUT)

            # Match and league statistics
            statsHome, statsAway, scorer = match.GetStats()
            self.ShowStats(statsHome, statsAway, clubHome, clubAway, MATCH_MASKS_TIMEOUT)
            self.UpdateTable(clubHome, statsHome, clubAway, statsAway)
            self.UpdateScorerRank(scorer)
            self.UpdateRound(statsHome, statsAway)
            self.ShowTable(MATCH_MASKS_TIMEOUT)

def main():
    championship = League(LEAGUE)
    championship.Play()

if __name__ == '__main__':
    main()
