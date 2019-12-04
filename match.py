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
    def __init__(self, team1, team2, isNeutralField = True):
        super().__init__()
        self.f1 = team1.formation
        self.f2 = team2.formation
        self.isNeutralField = isNeutralField
        self.log = Queue()
        self.isPlaying = True

        self.goal1 = 0
        self.offense1 = 0
        self.shoot1 = 0

        self.goal2 = 0
        self.offense2 = 0
        self.shoot2 = 0

        self.scorerList = []

    def GetLog(self):
        return self.log.get()

    def isLogEmpty(self):
        return self.log.empty()

    def GetStats(self):
        stats1 = [self.offense1, self.shoot1, self.goal1]
        stats2 = [self.offense2, self.shoot2, self.goal2]
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

    def Challenge(self):
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
        draw = ((chariness1 + weather) * overAll1) + ((chariness2 + weather) * overAll2)

        stats = random.randint(0, draw + midfield1 + midfield2)
        if (stats < draw): return MATCH_EVENT_NOTHING_HAPPENED, "", ""
        elif (stats < draw + midfield1): res = 1
        else: res = 2

        # Home team attacking...
        if (res == 1):
            stats = random.randint(0, attack1 + defense2)
            if (stats < attack1):
                strike, role, name = self.f1.GetStrike()
                stats = random.randint(0, strike + goalkeep2)
                if (stats < strike): return MATCH_EVENT_HOME_TEAM_GOAL, role, name
                else: return MATCH_EVENT_HOME_TEAM_SHOOT_SAVED, role, name
            else: return MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED, "", ""

        # Away team attacking...
        elif (res == 2):
            stats = random.randint(0, attack2 + defense1)
            if (stats < attack2):
                strike, role, name = self.f2.GetStrike()
                stats = random.randint(0, strike + goalkeep1)
                if (stats < strike): return MATCH_EVENT_AWAY_TEAM_GOAL, role, name
                else: return MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED, role, name
            else: return MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED, "", ""

    def run(self):
        self.isPlaying = True
        for minute in range(1, 91):
            res, role, name = self.Challenge()
            if res == MATCH_EVENT_NOTHING_HAPPENED: self.log.put("Minute:" + str(minute) + " --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_HOME_TEAM_ATTACK_STOPPED:
                self.offense1 = self.offense1 + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.f1.name + " ATTACK STOPPED --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_HOME_TEAM_SHOOT_SAVED:
                self.offense1 = self.offense1 + 1
                self.shoot1 = self.shoot1 + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), " + self.f1.name + " SHOOT SAVED --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_ATTACK_STOPPED:
                self.offense2 = self.offense2 + 1
                self.log.put("Minute:" + str(minute) + " --> " + self.f2.name + " ATTACK STOPPED --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_SHOOT_SAVED:
                self.offense2 = self.offense2 + 1
                self.shoot2 = self.shoot2 + 1
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role +  "), " + self.f2.name + " SHOOT SAVED --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_HOME_TEAM_GOAL:
                self.offense1 = self.offense1 + 1
                self.shoot1 = self.shoot1 + 1
                self.goal1 = self.goal1 + 1
                self.UpdatePlayerStats(name, self.f1.name)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.f1.name + "!!! --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))
            if res == MATCH_EVENT_AWAY_TEAM_GOAL:
                self.offense2 = self.offense2 + 1
                self.shoot2 = self.shoot2 + 1
                self.goal2 = self.goal2 + 1
                self.UpdatePlayerStats(name, self.f2.name)
                self.log.put("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.f2.name + "!!! --> " + self.f1.name + " vs. " + self.f2.name + ": " + str(self.goal1) + " - " + str(self.goal2))

        self.isPlaying = False

if __name__ == '__main__':
    pass

