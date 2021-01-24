name = input("Enter your name:")
print("Hello,", name,)

Q1 =input("How are you feeling?\n A.Good \n B.Bad ")
if Q1 == "A":
    print("Great! Let's get started")
else:
    print("Oh, I hope you feel better soon, Let's get started")

import time
import random
import sys
from random import randint  

print("My website has to do a lot with music so I'll ask a few questions about your interests. What my website does is takes the answers to qustions and gives musical suggestions/ facts. It also plays small mini games. ")

d1 = input("what are your main musical interests out of these options? a.Rock N' Roll  b.Pop music c.Alternative Rock  ")
if d1 == "a":
    input(" Some of the most popular rock n roll songs are Highway to hell by AC/DC, Aerosmith's Walk This Way, and Led Zeppelin's, Whole Lotta Love.)")
if d1 == "b": 
  print("Some of the most popular pop artists of 2020 were Taylor Swift, Ariana Grande,and Ed Sheeran")
else: 
  input(" The origins of alternative rock can be traced back to 1967  with the band Velvet Underground, which influenced many alternative rock bands that would come after it.")

print(" since we have to rock genres lets play Rock Paper scizzors!")

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
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


