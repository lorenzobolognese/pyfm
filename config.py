#-------------------------------------------------------------------------------
# Name:        config
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     09/12/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from serieA import SERIEA

# Masks and commentary timeouts
MATCH_MASKS_TIMEOUT = 5.00
MATCH_COMMENTARY_SPEED_TIMEOUT = 0.25

# Best player: minimum played matches number
MINIMUM_PLAYED_MATCHES_NUMBER_FOR_BEST_PLAYERS_CLASSIFICATION = 30

# League DB to be used for the simulation
LEAGUE = SERIEA

if __name__ == '__main__':
    pass
