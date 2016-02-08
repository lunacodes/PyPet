#!/usr/bin/env python3
""" PyPet - A Virtual Pet Game In Python - You must take care of your pet.  
    Inspired by things like Tamagotchi 

    Since this is terminal based, I plan to add in color, probably via the Colorama Module
    In the future, I'll write a Javascript version of this game, so people can play it on the web
    
    Non-working at present.  See "Design Notes.txt" and/or "Readme.md" for more info
"""

class Pet(object):
    """Factory Class to Produce Pets"""
    
    def __init__(self, name, key):
        self.name = name
        self.hungry = True
        self.starved = False
        self.bored = False
        self.upset = False
        self.violent = False
        self.sleepy = False

        self.key = key        
        self.messages = {
            'hungry': "I'm Hungry!!",
            'bored': "*Your pet says in a voice, strangely remiminiscent of Willow* Bored Now",
            'upset'  : "UGH - what the hell?!",
            'awake'  : "Alright, alright - I'm awake already",
            'asleep' : "Your pet is in a deep sleep",
            'sleepy' : "Your pet looks like it could really use a rest..."
        }


        def message_output(self, key):
            self.key = key
            print(self.messages[self.key])

class Cat(Pet):
    """ Everybody wants to be a Cat """
    
    def __init__(self, name, key):
        # super(Pet, self).__init__()
        self.name = name
        self.key = key
        
        pass


class Rat(Pet):
    """ Rats are so much nicer than Mice """
    
    def __init__(self):
        super(Rat, self).__init__()
        self.arg = arg
        
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

    cat_pet = Cat('harry', 'hungry')
    Cat.message_output('hungry')

if __name__ == '__main__':
    game_loop()

