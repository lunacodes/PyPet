# PyPet

A Virtual Pet Game for Python

This game is a work-in-progress, designed in a bottom-up fashion.  Originally inspired by the Thinkful.com Pypet Tutorial

#Version 2.0:
    Game is going through a major Refactoring
    See "Design Notes.txt" for more
    
    pypet_classes is currently in a non-working state.
    Check Out pypet_classes_v1-2.py if you are interested in the previous state of the game.

# Version 1.2:

What's New:
    Choose up to 5 Different Animals
    Changed Version Numbering Scheme
    Colored Terminal Output so Game is easier to Read

Features to Implement for Version 1.3:
    Provide a Menu Option to choose between Polite Pets & Vulgar/Intense Pets
    
    Implement Weight & Sleepy Functions
        Weight: will be related to Boredom, Mood & Food

        Sleepy: will improve some stats (Boredom, Upset, Violent) & make others Worse (Hungry).  The Sleepy mechanic will take into account that sleeping beyond Noon or Midnight will cause a Bug in the AMPM Switch Structure
    
    Expand Play Function so that it brings up a menu of sub-functions & you can vary the way you play with the Cat.  This mechanic will adjust the counter differently

    Implement a 1-10 Scale (instead of 1-5) for all the Counters to give the player Extended Gameplay
    
    Work on Implementing a System so that Every Animal Type does not need to be Instantiated at the beginning of the File.  Instead, only the Player's choice will be Instantiated.  This could possibly be done with Global Variables.

    Include a Violence Warning from the System, when the Pet is highly inclined towards Violence.  This indicates the the player has not been treating their Pet Well.

    Develop Differentiated Output Messages from the Hungry/Bored/Upset/Violent Checks, based on the Animal the player chose:
        This could be achieved by defining each check for each animal separately within the class (and then using player_pet_choice) to call the appropriate function

        This could also be achieved by creating Subclasses for each Pet Type that inherit from the Pet Class


Bugs to Fix for Version 1.3:
    bored_check() outputs comments that are too similar/all the same

    Violence is not initiated soon enough.  Based on the violence_counter, it should come into play after the 3rd Throw action, but it is not coming into play until the 4th.

    Check if Pygame's clock.tick() function is actually needed

    Move Time/AMPM adjustment into a Function if possible

#Version 1.0:
A Virtual Pet Game for Python

The current version is a very rough, command line-based, working draft that has not implemented the classes yet.

Version 2 will implement classes & refactor code in a logical & efficient manner.  It will also incorporate Colored Terminal Text.

Version 3 will add a Graphical Element with either Pygame or Kivy
