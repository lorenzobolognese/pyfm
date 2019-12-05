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

ROLES_LOOKUP_CHAIN = ["D", "M", "A"]

def Coach(tactics, roster):
    playing = []

    # Playing players: set the team
    lookup = 0
    while len(playing) < 11:
        end = -1
        for m in tactics.playersList:
            position = m[0]
            side = m[1]
            found = False
            while (found == False):
                idx = 0
                for p in roster:
                    if (position in p.role) and (side in p.side) and (idx > end) and (p not in playing):
                        if p.GetEnergy() > 0:
                            playing.append(p)
                            p.SetEnergy()
                            end = idx
                            break
                    idx = idx + 1

                if idx >= len(roster):
                    # No eligible player for the role: search for another one of other role...
                    position = ROLES_LOOKUP_CHAIN[lookup]
                    if lookup < 2: lookup = lookup + 1
                    else: lookup = 0
                    end = -1
                else: found = True

    # Not playing players: take a rest and recover energy!
    for p in roster:
        if (p not in playing): p.ResetEnergy()

    return playing

if __name__ == '__main__':
    for item in SERIEA:
        name, tactics, chariness, roster = item()
        play = Coach(tactics, roster)
        print(name, len(play))
        for line in play: print(name, line.role, line.name, line.energy, line.stamina)