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
        self.points = 0

    def SelectTeam(self, playersList):
        self.team.Add(playersList)

    def SelectFormation(self, formation):
        self.formation = formation()
        self.formation.Set(self.team)

if __name__ == '__main__':
    pass
