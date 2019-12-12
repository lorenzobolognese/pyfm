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

# User interface: print to standard output or text file
PRINT_TO_STANDARD_OUTPUT = True
PRINT_TO_TXT_FILE = True
TXT_FILE_PATH_AND_NAME = "c:\Temp\pyfm.txt"

# League DB to be used for the simulation
LEAGUE = SERIEA

if __name__ == '__main__':
    pass
