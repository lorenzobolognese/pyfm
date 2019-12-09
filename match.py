#-------------------------------------------------------------------------------
# Name:        match
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

import random
import time
from queue import Queue
from threading import Thread

# Match events
MATCH_EVENT_NOTHING_HAPPENED = 0
MATCH_EVENT_HOME_TEAM_GOAL = 1
MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED = -10
MATCH_EVENT_HOME_TEAM_SHOOT_SAVED = -11
MATCH_EVENT_AWAY_TEAM_GOAL = 2
MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED = -20
MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED = -21

class Match(Thread):
    def __init__(self, club1, club2, isNeutralField = True):
        super().__init__()
        self.teamAway = club2.tactics
        self.nameHome = club1.name
        self.nameAway = club2.name
        self.isNeutralField = isNeutralField
        self.log = Queue()
        self.isPlaying = True

        self.shoot1 = 0
        self.goalHome = 0
        self.offenseHome = 0
        self.shootHome = 0
        self.possessionHome = 0

        self.goalAway = 0
        self.offenseAway = 0
        self.shootAway = 0
        self.possessionAway = 0

        self.scorerList = []

    def GetLog(self):
        return self.log.get()

    def isLogEmpty(self):
        return self.log.empty()

    def GetStats(self):
        poss1, poss2 = self.GetBallPossession(90)
        stats1 = [self.offenseHome, self.shootHome, self.goalHome, poss1]
        stats2 = [self.offenseAway, self.shootAway, self.goalAway, poss2]
        return stats1, stats2, self.scorerList

    def UpdatePlayerStats(self, name, teamName):
        temp = []
        found = False
        for item in self.scorerList:
            score = item[2]
            if item[0] == name:
                score = score + 1
                found = True
            temp.append((item[0], item[1], score))
        if found == False: temp.append((name, teamName, 1))
        self.scorerList = temp

    def GetBallPossession(self, minute):
        poss1 = int(round((self.possessionHome*100)/minute, 0))
        poss2 = int(round((self.possessionAway*100)/minute, 0))
        return poss1, poss2

    def Challenge(self, minute):
        overAll1 = self.teamHome.GetOverall() + int(self.isNeutralField) * self.teamHome.GetHomeBonus("ALL")
        attack1 = self.teamHome.GetAttack() + int(self.isNeutralField) * self.teamHome.GetHomeBonus("A")
        midfield1 = self.teamHome.GetMidfield() + int(self.isNeutralField) * self.teamHome.GetHomeBonus("M")
        defense1 = self.teamHome.GetDefense() + int(self.isNeutralField) * self.teamHome.GetHomeBonus("D")
        goalkeep1 = self.teamHome.GetGoalkeep()
        chariness1 = self.teamHome.GetChariness()

        overAll2 = self.teamAway.GetOverall()
        attack2 = self.teamAway.GetAttack()
        midfield2 = self.teamAway.GetMidfield()
        defense2 = self.teamAway.GetDefense()
        goalkeep2 = self.teamAway.GetGoalkeep()
        chariness2 = self.teamAway.GetChariness()

        weather = random.randint(0,1)
        draw1 = ((chariness1 + weather) * overAll1)
        draw2 = ((chariness2 + weather) * overAll2)

        stats = random.randint(0, draw1 + draw2 + midfield1 + midfield2)
        if (stats < draw1):
            self.possessionHome = self.possessionHome + 1
            return MATCH_EVENT_NOTHING_HAPPENED, "", "", self.GetBallPossession(minute)
        elif (stats < draw1 + draw2):
            self.possessionAway = self.possessionAway + 1
            return MATCH_EVENT_NOTHING_HAPPENED, "", "", self.GetBallPossession(minute)
        elif (stats < draw1 + draw2 + midfield1):
            self.possessionHome = self.possessionHome + 1
            attacking = self.teamHome
            defending = self.teamAway
            attack = attack1
            defense = defense2
            goalkeep = goalkeep2
            returnEventGoal = MATCH_EVENT_HOME_TEAM_GOAL
            returnEventSaved = MATCH_EVENT_HOME_TEAM_SHOOT_SAVED
            returnEventStopped = MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED
        else:
            self.possessionAway = self.possessionAway + 1
            attacking = self.teamAway
            defending = self.teamHome
            attack = attack2
            defense = defense1
            goalkeep = goalkeep1
            returnEventGoal = MATCH_EVENT_AWAY_TEAM_GOAL
            returnEventSaved = MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED
            returnEventStopped = MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED

        attacking.AdjustPlayerVote("M", "UP")
        defending.AdjustPlayerVote("M", "DOWN")
        stats = random.randint(0, attack + defense)
        if (stats < attack):
            attacking.AdjustPlayerVote("A", "UP")
            defending.AdjustPlayerVote("D", "DOWN")
            strike, role, name = attacking.GetStriker()
            stats = random.randint(0, strike + goalkeep)
            if (stats < strike):
                attacking.AdjustStrikerVote("UP")
                defending.AdjustPlayerVote("GK", "DOWN")
                return returnEventGoal, role, name, self.GetBallPossession(minute)
            else:
                attacking.AdjustStrikerVote("DOWN")
                defending.AdjustPlayerVote("GK", "UP")
                return returnEventSaved, role, name, self.GetBallPossession(minute)
        else:
            attacking.AdjustPlayerVote("A", "DOWN")
            defending.AdjustPlayerVote("D", "UP")
            return returnEventStopped, "", "", self.GetBallPossession(minute)

    def run(self):
        self.isPlaying = True
        for minute in range(1, 91):
            res, role, name, possession = self.Challenge(minute)
            if res == MATCH_EVENT_NOTHING_HAPPENED: self.log.put("Minute:" + str(minute) + " --> " + str(self.goalHome) + " - " + str(self.goalAway) + " " + str(possession) + "%")
            if res == MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED:
                self.offenseHome = self.offenseHome + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.nameHome + " ATTACK STOPPED --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))
            if res == MATCH_EVENT_HOME_TEAM_SHOOT_SAVED:
                self.offenseHome = self.offenseHome + 1
                self.shootHome = self.shootHome + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), " + self.nameHome + " SHOOT SAVED --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))
            if res == MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED:
                self.offenseAway = self.offenseAway + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.nameAway + " ATTACK STOPPED --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))
            if res == MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED:
                self.offenseAway = self.offenseAway + 1
                self.shootAway = self.shootAway + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role +  "), " + self.nameAway + " SHOOT SAVED --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))
            if res == MATCH_EVENT_HOME_TEAM_GOAL:
                self.offenseHome = self.offenseHome + 1
                self.shootHome = self.shootHome + 1
                self.goalHome = self.goalHome + 1
                self.UpdatePlayerStats(name, self.nameHome)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.nameHome + "!!! --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))
            if res == MATCH_EVENT_AWAY_TEAM_GOAL:
                self.offenseAway = self.offenseAway + 1
                self.shootAway = self.shootAway + 1
                self.goalAway = self.goalAway + 1
                self.UpdatePlayerStats(name, self.nameAway)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.nameAway + "!!! --> " + self.nameHome + " vs. " + self.nameAway + ": " + str(self.goalHome) + " - " + str(self.goalAway))

        self.isPlaying = False

if __name__ == '__main__':
    pass

