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

class Club(object):
    def __init__(self, name, tactics, chariness, roster):
        self.name = name
        self.tactics = tactics()
        self.chariness = chariness
        self.roster = roster

        self.played = 0
        self.draw = 0
        self.won = 0
        self.lost = 0
        self.points = 0
        self.goalFor = 0
        self.goalAgainst = 0

    def SelectTeam(self, tactics, chariness, playersList):
        self.tactics = tactics
        self.tactics.Set(playersList, chariness)

if __name__ == '__main__':
    pass
