#-------------------------------------------------------------------------------
# Name:        berger
# Purpose:
#
# Author:      Lorenzo Bolognese
#
# Created:     05/12/2019
# Copyright:   (c) Lorenzo Bolognese 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

def Draw(board):
    home = []
    away = []

    teamNumber = len(board)
    rounds = len(board) - 1
    if not teamNumber % 2 == 0: board.append('REST SHIFT')
    i = 0
    while i < rounds:
        j = 0
        while j < (teamNumber / 2):
            home.append([board[j], board[rounds - j]])
            away.append([board[rounds - j], board[j]])
            j = j + 1
        i = i + 1
    home.extend(away)
    return home

if __name__ == '__main__':
    pass