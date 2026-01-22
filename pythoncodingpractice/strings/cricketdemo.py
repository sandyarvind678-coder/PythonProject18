# requirements 11 players need to play if 0 is come player is disqualified and coun the total runs and individual player scores

playerlist=input()



playerscore=list(map(int, input().split(",")))


scoreboard=0

individualscore=0

for i in playerlist:
    if playerscore<=0:
        print("out")
        break


    else:
        scoreboard=scoreboard+ playerscore
        individualscore=individualscore+ playerscore
        print(individualscore)
        print("player can play")

print(scoreboard)

