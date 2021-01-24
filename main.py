name = input("Enter your name:"")
print("Hello,", name, ")

Q1 =input("How are you feeling? A.Good \n B.Bad")
if q1 =="A":
    input("That's good, Let's get started!")
import time
import random
import sys
from random import randint  

print("My website has to do a lot with music so I'll ask a few questions about your interests. What my website does is takes the answers to qustions and gives musical suggestions/ facts. It also plays small mini games. ")

d1 = input("what are your main musical interests out of these options? a.Classic rock  B.Pop music c.Alternative Rock  ")
if d1 == "a":
    input(" Some of the most popular rock n roll songs are Highway to hell by AC/DC, Aerosmith's Walk This Way, and Led Zeppelin's, Whole Lotta Love since we are talking about rock lets play rock paper scizzors.") 
    t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("It's a Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
