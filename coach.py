#-------------------------------------------------------------------------------
# Name:        coach
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     04/12/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

from serieA import SERIEA

def Coach(tactics, roster):
    playing = []
    end = -1
    for m in tactics.playersList:
        position = m[0]
        side = m[1]
        idx = 0
        for p in roster:
            if (position in p.role) and (side in p.side) and (idx > end):
                if p.GetEnergy() > 0:
                    playing.append(p)
                    p.SetEnergy()
                    end = idx
                    break
                else:
                    p.ResetEnergy()
            idx = idx + 1
    return playing

if __name__ == '__main__':
    for item in SERIEA:
        name, tactics, chariness, roster = item()
        play = Coach(tactics, roster)
        print(name, len(play))
        for line in play: print(name, line.role, line.name, line.energy, line.stamina)