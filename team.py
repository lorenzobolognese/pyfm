#-------------------------------------------------------------------------------
# Name:        team
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class Team(object):
    def __init__(self, name = ""):
        self.roster = []
        self.name = name

    def Add(self, player):
        self.roster.append(player)

if __name__ == '__main__':
    pass
