#Get's users name 
name = input("Enter your name:")
print("Hello,", name,)

#Asks the first question 
Q1 =input("How are you feeling?\n A.Good \n B.Bad ")
if Q1 == "A":
    print("Great!")
else:
    print("Oh, I hope you feel better soon")

#Asks the second question 
Q2 =input("Does music interest you\n A.yes \n B.no ")
if Q2 == "A":
    print("Great! Let's get started")
else:
    print("Oh,Well, I'm going to ask you about it anyway")

#Asks the third question 
Q3 =input("Do you prefer new or old music? \n A.New \n B.Old ")
if Q3 == "A":
    print("Cool!Post Malone was the top artist of 2020")
else:
    print("Cool! The Beatles were at the top of the chain in the 60's")

#imports new modules
import time
import random
import sys
from random import randint  
#about website 
print("My website has to do a lot with music so I'll ask a few questions about your interests. What my website does is takes the answers to qustions and gives musical suggestions/ facts. It also plays a small mini game. ")

#Asks the fourth question 
Q4 = input("what are your main musical interests out of these options? a.Rock N' Roll  b.Pop music c.Alternative Rock  ")
if Q4 == "a":
    input(" Some of the most popular rock n roll songs are Highway to hell by AC/DC, Aerosmith's Walk This Way, and Led Zeppelin's, Whole Lotta Love.)")
if Q4 == "b": 
  print("Some of the most popular pop artists of 2020 were Taylor Swift, Ariana Grande,and Ed Sheeran")
else: 
  input(" The origins of alternative rock can be traced back to 1967  with the band Velvet Underground, which influenced many alternative rock bands that would come after it.")
#5th question/ mini game 
print(" since we have multiple rock genres lets play Rock Paper scizzors!")


#create a list of play options
t = ["Rock", "Paper", "Scissors"]

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

