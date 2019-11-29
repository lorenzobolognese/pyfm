#-------------------------------------------------------------------------------
# Name:        player
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     29/11/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

class Player(object):
    def __init__(self, roles, positions, power, name = "John Doe"):
        self.roles = roles
        self.positions = positions
        self.power = power
        self.name = name

    def GetPerformance(self, fieldRole, fieldPosition, isShooting = False):
        if fieldRole in self.roles: r = 100
        else: r = 50
        if fieldPosition in self.positions: p = 100
        else: p = 50
        if isShooting == True:
            if fieldRole == "A": s = 100
            elif fieldRole == "C": s = 85
            else: s = 70
        else: s = 100
        return self.power*(r/100)*(p/100)*(s/100)

if __name__ == '__main__':
    pass
