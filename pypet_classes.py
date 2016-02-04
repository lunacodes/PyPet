#!/usr/bin/env python3
""" PyPet - A Virtual Pet Game In Python - You must take care of your pet.  
    Inspired by things like Tamagotchi 

    Since this is terminal based, I plan to add in color, probably via the Colorama Module
    In the future, I'll write a Javascript version of this game, so people can play it on the web
    """

class Pet(object):
    """Factory Class to Produce Pets"""
    
    def __init__(self, name):
        # super(Pet, self).__init__()
        pass


class Cat(Pet):
    """ Everybody wants to be a Cat """
    
    def __init__(self):
        super(Cat, self).__init__()
        self.name = name
        self.hungry = True
        self.starved = False
        self.bored = False
        self.upset = False
        self.violent = False
        self.sleepy = False
        pass

class Mouse(Pet):
    """ How Very Mousy """

    def __init__(self):
        super(Mouse, self).__init__()
        self.arg = arg
        pass
                        

class Bunny(Pet):
    """ Buns are the cutest :) """
    
    def __init__(self):
        super(Bunny, self).__init__()
        self.arg = arg
        pass


class Turtle(Pet):
    """ Slow & Steady wins the race """
    
    def __init__(self):
        super(Turtle, self).__init__()
        self.arg = arg
        pass
        
        
def intro():
    print("Welcome to PyPet!")
    print("What type of pet would you like to be?")
    print("")
    
def menu(pet_choice):
    """Things you can do with your Pet"""

def game_loop():
    print("Welcome to PyPet")



