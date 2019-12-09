# pyfm
Python Footbal Manager

# Description
Simple football simulator where all 2019/2020 Italian Serie A's teams play against each other (home and away). All the clubs are managed by the CPU; user interaction is actually limited to setup team's rosters, tactics and chariness at the beginning of the league. User Interface is totally textual through standard output.

Features included:
 - Full 2019/2020 Serie A with all the teams and players
 - League and strikers board
 - Match statistics
 - Players match ratings
 - Match commentary with configurable speed
 - 38 rounds of home and away matches; home playing teams get bonus
 - Pitch conditions simulation (poor, just two levels: good or bad)
 - 4 different roles: Attakers, Midfielders, Defenders and GoalKeepers
 - 3 different playing field zones: Left, Center and Right
 - 4 different technical skills for each player: Attack, Midfield, Defense, GoalKeeping
 - Stamina and residual energy both defined in terms of consecutive playable matches
 - Penalizations when a player plays in a not suitable position (role, zone or both)
 - Configurable tactic and "chariness"
 - Simulated coach: at the beginning of each match he setups the team as per required tactic and chariness letting out-of-energy players sitting on the bench. Out-of-role players are adopted only when there's no other choice to get 11 players
 - Match ratings: performance of each player on each match is measured with a vote in the range 0.0 ... 10.0
 - Ball possession percentage
 - Average ratings: each single match rating of each player is taken to build at the end of each round, the Best Players board

About "chariness": it may take 3 levels:
 - 1 --> team will try to find the goal frequently exponing itself to counter-attack risks
 - 2 --> team will keep often the ball possession
 - 3 --> team will limit its attitude to attack to prevent the risk to lose the ball possession

# Requirements
 - Python 3.8

# Tested configuration
 - Windows 10
 - Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32

# How to run it
 - Open "config.py"
 - Configure MATCH_MASKS_TIMEOUT and MATCH_COMMENTARY_SPEED_TIMEOUT (seconds)
 - Run "pyfm.py"

# How to configure the teams
 - Open included "xls" file or serieA.py
 - Play with rosters, tactics, chariness and skills
 - Remember simulated coaches will select the players following the tactic chosen. Priority is always given to players who are at the top of the list so let stronger player being always at the top of their role block
