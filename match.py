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

class Match(object):
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

        self.goal1 = 0
        self.goal2 = 0
        self.attackCounter1 = 0
        self.shootCounter1 = 0
        self.attackCounter2 = 0
        self.shootCounter2 = 0

    def ShowStats(self):
        print()
        print("MATCH STATS")
        print()
        print(self.f1.name)
        print("Attacks: " + str(self.attackCounter1))
        print("Shoots: " + str(self.shootCounter1))
        print("Goals: " + str(self.goal1))

        print()
        print(self.f2.name)
        print("Attacks: " + str(self.attackCounter2))
        print("Shoots: " + str(self.shootCounter2))
        print("Goals: " + str(self.goal2))
        print()

    def Challenge(self, equilibrium):
        overAll1 = self.f1.GetOverall()
        attack1 = self.f1.GetAttack()
        midfield1 = self.f1.GetMidfield()
        defense1 = self.f1.GetDefense()
        goalkeep1 = self.f1.GetGoalkeep()

        overAll2 = self.f2.GetOverall()
        attack2 = self.f2.GetAttack()
        midfield2 = self.f2.GetMidfield()
        defense2 = self.f2.GetDefense()
        goalkeep2 = self.f2.GetGoalkeep()

        draw = equilibrium*(overAll1 + overAll2)

        stats = random.randint(0, draw + midfield1 + midfield2)
        if (stats < draw): return 0, "", ""
        elif (stats < draw + midfield1): res = 1
        else: res = 2

        if (res == 1):
            stats = random.randint(0, attack1 + defense2)
            if (stats < attack1):
                strike, role, name = self.f1.GetStrike()
                stats = random.randint(0, strike + goalkeep2)
                if (stats < strike): return 1, role, name
                else: return -11, role, name
            else: return -10, "", ""
        elif (res == 2):
            stats = random.randint(0, attack2 + defense1)
            if (stats < attack2):
                strike, role, name = self.f2.GetStrike()
                stats = random.randint(0, strike + goalkeep1)
                if (stats < strike): return 2, role, name
                else: return -21, role, name
            else: return -20, "", ""

    def Play(self):
        eq = random.randint(1, 3)
        ## print("Equilibrium: " + str(eq))
        for minute in range(1, 91):
            time.sleep(0.5)
            res, role, name = self.Challenge(eq)
            if res == 0: print("Minute:" + str(minute) + " --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == -10:
                self.attackCounter1 = self.attackCounter1 + 1
                print("Minute:" + str(minute) + " --> " + self.f1.name + " ATTACK STOPPED --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == -11:
                self.attackCounter1 = self.attackCounter1 + 1
                self.shootCounter1 = self.shootCounter1 + 1
                print("Minute:" + str(minute) + " --> " + name + " (" + role + "), " + self.f1.name + " SHOOT SAVED --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == -20:
                self.attackCounter2 = self.attackCounter2 + 1
                print("Minute:" + str(minute) + " --> " + self.f2.name + " ATTACK STOPPED --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == -21:
                self.attackCounter2 = self.attackCounter2 + 1
                self.shootCounter2 = self.shootCounter2 + 1
                print("Minute:" + str(minute) + " --> " + name + " (" + role +  "), " + self.f2.name + " SHOOT SAVED --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == 1:
                self.attackCounter1 = self.attackCounter1 + 1
                self.shootCounter1 = self.shootCounter1 + 1
                self.goal1 = self.goal1 + 1
                print("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.f1.name + "!!! --> " + str(self.goal1) + " - " + str(self.goal2))
            if res == 2:
                self.attackCounter2 = self.attackCounter2 + 1
                self.shootCounter2 = self.shootCounter2 + 1
                self.goal2 = self.goal2 + 1
                print("Minute:" + str(minute) + " --> " + name + " (" + role + "), GOAL " + self.f2.name + "!!! --> " + str(self.goal1) + " - " + str(self.goal2))

        return self.goal1, self.goal2

if __name__ == '__main__':
    pass

