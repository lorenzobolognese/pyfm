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
    homeRounds = []
    awayRounds = []

    teams = len(board)
    rounds = teams - 1
    for i in range(0, int(teams/2)):
        home.append(board[i])
        away.append(board[rounds - i])

    for i in range(0, rounds):
        for j in range(0, int(teams/2)):
            homeRounds.append([away[j], home[j]])
            awayRounds.append([home[j], away[j]])

        # List items rotation
        pivot = home[0]
        riporto = away.pop()
        away.insert(0, home[1])
        home.pop(0)
        home.append(riporto)
        home[0] = pivot

    return (homeRounds + awayRounds)

if __name__ == '__main__':
    league = ["A", "B", "C", "D"]
    print(Draw(league))
