#-------------------------------------------------------------------------------
# Name:        club
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from team import Team
from formation import Formation

class Club(object):
    def __init__(self, name = ""):
        self.team = Team(name)
        self.formation = Formation()
        self.chariness = 0
        self.played = 0
        self.draw = 0
        self.won = 0
        self.lost = 0
        self.points = 0
        self.goalFor = 0
        self.goalAgainst = 0

    def SelectTeam(self, tactics, chariness, playersList):
        self.team.Add(playersList)
        self.formation = tactics()
        self.formation.Set(self.team, chariness)

if __name__ == '__main__':
    pass
