from __future__ import print_function
import pygame
from pygame.locals import *
from colorama import init, Fore, Back, Style

init() #Colorama init
pygame.init()
clock = pygame.time.Clock()

pet_type = 0
pet_name = ""

class Pet(object): 
    def __init__(self):
        self.name = pet_name    
        self.hungry = True
        self.hungry_counter = 2
        self.starved = False
        self.bored = True
        self.bored_counter = 2
        self.upset = False
        self.upset_counter = 0
        self.violent = False
        self.violent_counter = 0
        self.sleepy = False 
        self.awake = True
        self.weight = 5.0
        self.age = 5
        self.photo = '(=^o.o^=)__'

    def stats(self): 
        print(Fore.CYAN + self.name + "\n", self.photo + "\n", "Weght: ", self.weight, "\n")
        if self.hungry == True:
            print("Hungry\n")
        if self.bored == True:
            print("Bored Now \n")
        if self.upset == True:
            print("Upset\n")
        if self.awake == True:
            print("Awake\n")
        elif self.awake == False:
            print("Asleep\n")
        if self.sleepy == True:
            print("Sleepy\n")
        print("\n")

    def upset_check(self): 
        if self.upset_counter < 0:
            self.upset_counter = 0 
        elif self.upset_counter > 0:
            if self.upset_counter == 1:
                print(Fore.CYAN + "Meh")
            elif self.upset_counter < 3:
                print(Fore.CYAN + "I'm kinda upset right now ... please make this better?")
            elif self.upset_counter == 4:
                print(Fore.CYAN + "I'M REALLY UPSET - FIX THIS NOW!!")
            elif self.upset_counter == 5:
                print(Fore.CYAN + "FIX THIS NOW GODS DAMNIT - YOU FUCKING TERRIBLE OWNER!!")
            elif self.upset_counter >= 6:
                print(Fore.CYAN + "Now you're gonna die")
                self.violent = True 

    def bored_check(self): 
        if self.bored_counter <= 0:
            self.bored_counter = 0
        elif self.bored_counter >= 0:
            if self.bored_counter <= 2:
                print(Fore.CYAN + "\nBored Now")
            elif self.bored_counter == 3:
                print(Fore.CYAN + "\nLook, I like you and all, but you're really not That Interesting")
            elif self.bored_counter >= 4:
                self.upset_counter += 1
                print(Fore.CYAN + "Bored Count >= 4")
    
    def violent_check(self): 
        if self.violent_counter <= 0:
            self.violent_counter = 0
        elif self.violent_counter > 0:
            if self.violent_counter <= 2:
                print(Fore.CYAN + "\nViolent Now")
            elif self.violent_counter == 3:
                print(Fore.CYAN + "\nLook, I like you and all, but you're really not That Interesting")
            elif self.violent_counter < 5:
                self.upset_counter += 1
                print(Fore.CYAN + "\nYou're boring - Fuck Off")
            elif self.violent_counter >= 6:
                self.violent == True

    def hungry_check(self):
        if self.hungry_counter <= 0:
            self.hungry_counter = 0
        elif self.hungry_counter >= 0:
            if self.hungry_counter <= 2:
                print(Fore.CYAN + "Could you feed me?")
            elif self.hungry_counter == 3:
                print(Fore.CYAN + "Yo!  You're Ok & All, but Feed Me!!")
            elif self.hungry_counter < 6:
                self.upset_counter += 1
                print(Fore.CYAN + "FEED ME NOW")
            elif self.hungry_check >= 6:
                self.starved = True

    def feed(self):
        if self.hungry == True:
            self.weight += 1
            self.hungry = False
            print(Fore.CYAN + "\nYummy, Yummy Foodz")
        else:
            print(Fore.CYAN + "\nI am no Hungry right now.  I can has foodz later plz?")

    def pet(self):
        print(Fore.CYAN + "\n^_^ Thank you for petting me ^_^")
        self.upset_counter -= 1
        
        self.upset_check()
        
    def play(self):

        print(Fore.CYAN + "\n^_^ Yay!!  Let's Play ^_^ ")
        self.upset_counter -= 2
        self.bored_counter -= 2
        self.weight -= 1

        self.upset_check()
        self.bored_check()

    def ignore(self):
        print(Fore.CYAN + "\nWow - Fuck You. Pay attention to me")
        
        if self.upset_counter == 2:
            self.upset_counter += 1
        elif self.upset_counter >= 3: 
            self.upset_counter += 1.5
        self.bored_counter += 1
        self.hungry_counter += 1

    def throw(self):
        print(Fore.CYAN + "\nWHY THE FUCK WOULD YOU THROW ME???!")
        self.upset_counter += 2
        self.violent_counter += 2

    def talk(self):

        self.bored_counter -= 1
        self.hungry_counter += 1

Cat = Pet()
Rat = Pet()
Mouse = Pet()
Bunny = Pet()
Turtle = Pet()

def intro(pet_name):
    print(Fore.RED + "Heya - Welcome to Pypet!!\n") 
    print(Fore.GREEN + ' (=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          '(=^o.o^=)' + "\n",
          )

    print(Fore.RED) 
    print("What type of pet would you like to play?" + Fore.GREEN + " \n\n1.  Cat\n2.  Rat\n3.  Mouse\n4.  Bunny\n5.  Turtle\n")
    pet_type = input("") 
    print(str(pet_type)) 
    print(Fore.RED)
        pet_name = raw_input("\nWhat would you like to call your Cat? \n\n" + Fore.GREEN)
        player_pet_choice = Cat
        Cat.name = pet_name
    if pet_type == 2:
        pet_name = raw_input("\nWhat would you like to call your Rat? \n" + Fore.GREEN)
        player_pet_choice = Rat
        Rat.name = pet_name
    if pet_type == 3:
        pet_name = raw_input("\nWhat would you like to call your Mouse? \n" + Fore.GREEN)
        player_pet_choice = Mouse
        Mouse.name = pet_name
    if pet_type == 4:
        pet_name = raw_input("\nWhat would you like to call your Bunny? \n" + Fore.GREEN)
        player_pet_choice = Bunny
        Bunny.name = pet_name
    if pet_type == 5:
        pet_name = raw_input("\nWhat would you like to call your Turtle? \n" + Fore.GREEN)
        player_pet_choice = Turtle
        Turtle.name = pet_name

    print(Fore.CYAN + '\n\n' + pet_name + ' says "Hello"\n\n\n')
    print(Fore.RED + "Let's set the Time! \n")
    hour = input("What's the Hour? (1-12) \n" + Fore.GREEN) 
    AMPM = raw_input(Fore.RED + "\nIs it AM or PM? \n" + Fore.GREEN).upper() #This should cause a bug later on, if the user inputs more than two characters... easy enough to fix, just get the slice of it
    print("\n")
    
    game_loop(player_pet_choice, pet_type, pet_name, hour, AMPM, Cat)


def menu(player_pet_choice): 
    print(Fore.RED + "Menu: \n\n",  
      Fore.GREEN + "1.  Feed \n",
      "2.  Pet \n",
      "3.  Play \n",
      "4.  Ignore \n",
      "5.  Throw \n",
      "6.  Talk \n \n")

    choice = input(Fore.RED + "What would you like to do? (Enter 1-5) \n" + Fore.GREEN)
    
    if choice == 1:
        player_pet_choice.feed()
    if choice == 2:
        player_pet_choice.pet()
    if choice == 3:
        player_pet_choice.play()
    if choice == 4:
        player_pet_choice.ignore()
    if choice == 5:
        player_pet_choice.throw()
    if choice == 6:
        player_pet_choice.talk()


def game_over_check(pet, pet_violent, pet_starved, game_running): #Add in checks for Starvation & Stuff
    if pet_violent:
        print(pet, "Is Violent", pet_violent)
        print(pet, "Killed You.  You Lose")
        return False
    if pet_starved:
        print(pet, "Has Starved")
        print("You Have Killed", pet, "\nYou Lose")
        return False

    return game_running, True


def game_loop(player_pet_choice, pet_type, pet_name, hour, AMPM, Cat):
    turn = 0
    game_running = True
    while game_running:

        time = [hour, AMPM]
        player_pet_choice.violent_check()
        player_pet_choice.bored_check()
        player_pet_choice.hungry_check()
        player_pet_choice.upset_check()

        turn += 1 

        print("The Time is", time[0], time[1], "\n")
        print(Fore.RED + "Turn", turn, "\n")

        player_pet_choice.stats()

        menu(player_pet_choice)
        hour += 1

        if hour >= 12:
            if hour == 12:
                if AMPM == "AM":
                    AMPM = "PM"
                elif AMPM == "PM":
                    AMPM = "AM"

            elif hour > 12:              
                hour -= 12

        clock.tick(60) 
        pygame.time.delay(3000)
        game_running = game_over_check(player_pet_choice.name, player_pet_choice.violent, player_pet_choice.starved, game_running)
        
        if game_running == False:
            break


if __name__ == "__main__":
    intro(pet_name)