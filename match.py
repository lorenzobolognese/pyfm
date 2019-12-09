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
        self.f1 = club1.tactics
        self.f2 = club2.tactics
        self.name1 = club1.name
        self.name2 = club2.name
        self.isNeutralField = isNeutralField
        self.log = Queue()
        self.isPlaying = True

        self.goal1 = 0
        self.offense1 = 0
        self.shoot1 = 0
        self.possession1 = 0

        self.goal2 = 0
        self.offense2 = 0
        self.shoot2 = 0
        self.possession2 = 0

        self.scorerList = []

    def GetLog(self):
        return self.log.get()

    def isLogEmpty(self):
        return self.log.empty()

    def GetStats(self):
        poss1, poss2 = self.GetBallPossession(90)
        stats1 = [self.offense1, self.shoot1, self.goal1, poss1]
        stats2 = [self.offense2, self.shoot2, self.goal2, poss2]
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
        poss1 = int(round((self.possession1*100)/minute, 0))
        poss2 = int(round((self.possession2*100)/minute, 0))
        return poss1, poss2

    def Challenge(self, minute):
        overAll1 = self.f1.GetOverall() + int(self.isNeutralField) * self.f1.GetHomeBonus("ALL")
        attack1 = self.f1.GetAttack() + int(self.isNeutralField) * self.f1.GetHomeBonus("A")
        midfield1 = self.f1.GetMidfield() + int(self.isNeutralField) * self.f1.GetHomeBonus("M")
        defense1 = self.f1.GetDefense() + int(self.isNeutralField) * self.f1.GetHomeBonus("D")
        goalkeep1 = self.f1.GetGoalkeep()
        chariness1 = self.f1.GetChariness()

        overAll2 = self.f2.GetOverall()
        attack2 = self.f2.GetAttack()
        midfield2 = self.f2.GetMidfield()
        defense2 = self.f2.GetDefense()
        goalkeep2 = self.f2.GetGoalkeep()
        chariness2 = self.f2.GetChariness()

        weather = random.randint(0,1)
        draw1 = ((chariness1 + weather) * overAll1)
        draw2 = ((chariness2 + weather) * overAll2)

        stats = random.randint(0, draw1 + draw2 + midfield1 + midfield2)
        if (stats < draw1):
            self.possession1 = self.possession1 + 1
            return MATCH_EVENT_NOTHING_HAPPENED, "", "", self.GetBallPossession(minute)
        elif (stats < draw1 + draw2):
            self.possession2 = self.possession2 + 1
            return MATCH_EVENT_NOTHING_HAPPENED, "", "", self.GetBallPossession(minute)
        elif (stats < draw1 + draw2 + midfield1):
            self.possession1 = self.possession1 + 1
            attacking = self.f1
            defending = self.f2
            attack = attack1
            defense = defense2
            goalkeep = goalkeep2
            returnEventGoal = MATCH_EVENT_HOME_TEAM_GOAL
            returnEventSaved = MATCH_EVENT_HOME_TEAM_SHOOT_SAVED
            returnEventStopped = MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED
        else:
            self.possession2 = self.possession2 + 1
            attacking = self.f2
            defending = self.f1
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
            if res == MATCH_EVENT_NOTHING_HAPPENED: self.log.put("Minute:" + str(minute) + " --> " + str(self.goal1) + " - " + str(self.goal2) + " " + str(possession) + "%")
            if res == MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED:
                self.offense1 = self.offense1 + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.name1 + " ATTACK STOPPED --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_HOME_TEAM_SHOOT_SAVED:
                self.offense1 = self.offense1 + 1
                self.shoot1 = self.shoot1 + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), " + self.name1 + " SHOOT SAVED --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED:
                self.offense2 = self.offense2 + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.name2 + " ATTACK STOPPED --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED:
                self.offense2 = self.offense2 + 1
                self.shoot2 = self.shoot2 + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role +  "), " + self.name2 + " SHOOT SAVED --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_HOME_TEAM_GOAL:
                self.offense1 = self.offense1 + 1
                self.shoot1 = self.shoot1 + 1
                self.goal1 = self.goal1 + 1
                self.UpdatePlayerStats(name, self.name1)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.name1 + "!!! --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_GOAL:
                self.offense2 = self.offense2 + 1
                self.shoot2 = self.shoot2 + 1
                self.goal2 = self.goal2 + 1
                self.UpdatePlayerStats(name, self.name2)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.name2 + "!!! --> " + self.name1 + " vs. " + self.name2 + ": " + str(self.goal1) + " - " + str(self.goal2))

        self.isPlaying = False

if __name__ == '__main__':
    pass

