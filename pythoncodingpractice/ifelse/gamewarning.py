#if player playing more than 1 hours continously the game send the light warning the game
#if player playing more than 2 hours continously the game send the strict warning the game
#if player playing more than 3 hours continously the game send the last level warning high level the game
#if player playing more than 4 hours continously the game shut down the game


playername=input()

a=int(input())
b=int(input())
c=a+b
level1=c
if (10<=level1):
        print("warn the player to take a break")
        exit()
else:
    print("proceed the player to take a next game")


d=int(input())
e=int(input())

f=c+d+e
level2=f


if (20<=level2):
    print("warn the player to take a break before start new game")
    exit()
else:
    print("proceed the player to take a next game")


g=int(input())
h=int(input())

i=f+g+h
level3=i

if (30<=level3):
    print("give signal red to stop the game and come back after 6 hours")
    exit()
else:
    print("proceed the player to take a next game")


j=int(input())
k=int(input())

l=i+j+k
level4=l


if (40<=level4):
    print("terminate the game immediately and don't allow for next 48 hours")
    exit()
else:
    print("proceed the player to take a next game")