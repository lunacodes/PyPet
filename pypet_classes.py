from __future__ import print_function
import pygame
from pygame.locals import *
# from colorama import init, Fore, Back, Style


# init() #Colorama Init

pygame.init()
clock = pygame.time.Clock()

class Pet(object):
    def __init__(self):
        self.name = name
        self.hungry = True
        self.weight = 9.5
        self.age = 5
        self.photo = '(=^o.o^=)__'

    def feed(self):
        if self.hungry == True:
            self.weight += 1
            self.hungry = False
            print("Yummy Yummy Foodz")
        else:
            print("I is no Hungry right now.  I can has fooz later plz?")


    def pet(self):
        print("^_^ Thank you for petting me ^_^")

#Red Text!!
# print(Fore.RED + 'some red text')
# print(Fore.RESET + Back.RESET + Style.RESET_ALL)

hour = 1
hungry = True
bored = True
upset_small = True
upset_big =False
violent = False
AMPM = ""
sleepy = False
awake = True
upset_counter = 0

def gameOver():
    print("You Lose \n Game Over!!")
    awake = False
    return awake
def win():
    print("You Made Me Happy!!  You are wonderful owner ^_^")
    awake = False
    return awake

print("Welcome to PyPety ^_^ \n")

while str(AMPM) != "AM" :
    AMPM = raw_input("\nIs it AM or PM? ").upper()
    if AMPM == "AM \n":
        print(AMPM)
    elif AMPM == "PM \n":
        print(AMPM)
        # break
    else:
        print("Please enter AM or PM \n")
    break
    
if hour in xrange(1,12):
    if AMPM:
        hour = input("What hour is it? (1-12) \n\n")


while awake: 
    print("The Time Is", hour, AMPM, "\n")
    
    if violent == True:
        print("PET ATTACKS YOU AND YOU DIE!!! \n\n")
        gameOver()
        awake = False
        break

    elif hungry == True:
        # print("I'm Hungry.  Feed me plz?? *cute face* \n\n")
        if upset_small == True:
            print("I'm hungry and a bit upset - feed me now?? \n\n")
        if upset_big == True:
            print("I'M HUNGRY AND UPSET - FEED ME NOW!! \n\n")
        elif upset_small == False:
            upset_small = True
        if bored == True:
            print("Bored Now *Willow Voice* \n\n")
        elif bored == False:
            bored = True
        else:
            print("I'm Hungry.  Feed me plz?? *cute face* \n\n")

    elif bored == True:
        if hungry == True:
            print("I'm Hungry & Bored.  Feed me plz?? *cute face* \n\n")
        if upset_small == True:
            print("I'm bored & a bit upset.  Fix this plz? *mild upset face* \n\n")            
        elif upset_small == False:
            upset_small = True
        if upset_big:
            print("I'M UPSET & THIS IS FUCKING BORING.  FUCKING FIX THIS!! \n\n")
        else:
            print("Bored Now *Willow Voice* \n\n")

    elif upset_small == True:
        if hungry == True:
            print("I'm hungry and a bit upset - feed me now?? \n\n")
        if bored == True:
            print("I'm bored & a bit upset.  Fix this plz? *mild upset face* \n\n")            
        else:
            print("I'm a bit upset - please fix this?")
            upset_small = False #Maybe take these two lines out??
            upset_big = True

    elif upset_big:
        if hungry == True:
            print("I'M HUNGRY AND UPSET - FEED ME NOW!! \n\n")
        if bored == True:
            print("I'M UPSET & THIS IS FUCKING BORING.  FUCKING FIX THIS!! \n\n")
        else:
            print("I'M REALLY UPSET - FIX THIS!!")
            upset_counter += 1
            if upset_counter >= 2:
                violent = True

    else:
        win()
        awake = False
        break

    print("Menu: \n\n",
          "1.  Feed \n",
          "2.  Pet \n",
          "3.  Play \n",
          "4.  Ignore \n",
          "5.  Throw \n",
          "6.  Talk \n \n")

    choice = input("What would you like to do? (Enter 1-5) \n")
    if choice == 1:
        print("FOODZ - YAY!! \n\n")
        hungry = False
    if choice == 2:
        print("Awww, you pet me *happy face* \n\n")
        upset_small = False
    if choice == 3:
        print("PLAY TIMEZ!!!  HAPPY ^_^ :) ^_^")
        bored = False
        upset_small = False
    if choice == 4:
        if hungry == True:
            print("HUNGRY \n")
        if upset_small == True:
            print("You're Making Me MAD!!\n")
            upset_small = False
            upset_big = True
        if bored == True:
            print("BORED NOW: \n")

        print("\n")
    if choice == 5:
        print("WHY THE FUCK WOULD YOU THROW ME?!?!")
        hungry = True
        bored = True
        upset_big = True
        violent = True

    if choice == 6:
        print("That's nice that you're talking to me ... but you're really not that interesting...")
        bored = True

    hour +=1
    # print(hour)

    if hour > 12:
        hour = hour - 12
        print(hour)
    if (hour -1 == 0) and AMPM =="AM":
        AMPM = "PM"
        print(hour, AMPM) #Maybe pull this out of the if statement b/c redundancy
    elif (hour -1 == 0) and AMPM =="PM":
        print(hour, AMPM)

    # else:
    #     gameOver()
    #     awake = False
    clock.tick(60)
    pygame.time.delay(1000)

    if awake == True:
        print("\n Next Turn \n \n")
