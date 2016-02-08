# PyPet - A Virtual Pet Game in Python

*PyPet is a work-in-progress, inspired by Thinkful's [Create A PyPet tutorial](https://www.thinkful.com/learn/intro-to-python-tutorial/Creating-Your-Pypet).*  
  
*Originally designed improvisationally, PyPet is currently being refactored using a more top-down approach.*

*(I hope to have a new working version up soon!)*

<br>
##Version 2.0
PyPet is going through a major Refactoring - *See [Design Planning](https://github.com/lunacodes/PyPet/blob/master/Design%20Planning.txt) for more info*

In the meantime:    

* *`pypet_classes.py` is currently in a non-working state.*
* *Check Out `pypet_classes_v1-2.py` if you are interested in the previous state of the game.*


##Version 1.2

####What's New:

 * Choose up to 5 Different Animals
 * Changed Version Numbering Scheme
 * Colored Terminal Output so Game is easier to Read
  

####Features to Implement for Version 1.3 (Deprecated): 
&nbsp;&nbsp;&nbsp;&nbsp; **1. &nbsp;**  Provide a Menu Option to choose between Polite Pets & Vulgar/Intense Pets<br>
&nbsp;&nbsp;&nbsp;&nbsp; **2. &nbsp;**  Implement Weight & Sleepy Functions<br>
&nbsp;&nbsp;&nbsp;&nbsp; **3. &nbsp;**  Weight: will be related to Boredom, Mood & Food<br>
&nbsp;&nbsp;&nbsp;&nbsp; **4. &nbsp;**  Sleepy: will improve some stats (Bored, Upset, Violent).  Will make others (Hungry) worse<br>
&nbsp;&nbsp; **4a. &nbsp;**  The Sleepy mechanic will take into account that sleeping beyond Noon or Midnight will cause a Bug in the AMPM Switch Structure<br>
&nbsp;&nbsp;&nbsp;&nbsp; **5. &nbsp;**  Implement a 1-10 Scale (instead of 1-5) for all the Counters to give the player Extended Gameplay<br>
&nbsp;&nbsp;&nbsp;&nbsp; **6. &nbsp;**   Work on Implementing a System so that Every Animal Type does not need to be Instantiated at the beginning of the File.  Instead, only the Player's choice will be Instantiated.  This could possibly be done with Global Variables.<br>
&nbsp;&nbsp;&nbsp;&nbsp; **7. &nbsp;**  Include a Violence Warning from the System, when the Pet is highly inclined towards Violence.  This indicates the the player has not been treating their Pet Well.<br>
&nbsp;&nbsp;&nbsp;&nbsp; **8. &nbsp;**  Develop Differentiated Output Messages from the Hungry/Bored/Upset/Violent Checks, based on the Animal the player chose:<br>
&nbsp;&nbsp; **8a. &nbsp;**  This could be achieved by defining each check for each animal separately within the class (and then using player_pet_choice) to call the appropriate function<br>
&nbsp;&nbsp; **8b. &nbsp;**  This could also be achieved by creating Subclasses for each Pet Type that inherit from the Pet Class


####Bugs to Fix for Version 1.3:
&nbsp;&nbsp;&nbsp;&nbsp; **1. &nbsp;**  bored_check() outputs comments that are too similar/all the same<br>
&nbsp;&nbsp;&nbsp;&nbsp; **2. &nbsp;**  Violence is not initiated soon enough.  Based on the violence_counter, it should come into play after the 3rd Throw action, but it is not coming into play until the 4th.<br>
&nbsp;&nbsp;&nbsp;&nbsp; **3. &nbsp;**  Check if Pygame's clock.tick() function is actually needed<br>
&nbsp;&nbsp; **3a. &nbsp;**  Move "Time/AMPM adjustment" into a Function if possible


##Version 1.0:
*A Virtual Pet Game for Python* (Deprecated)

**The current version:** *a very rough, command line-based, working draft that has not implemented the classes yet.*

**Version 2:** *will implement classes & refactor code in a logical & efficient manner.  It will also incorporate Colored Terminal Text.*

**Version 3:** *will add a Graphical Element with either Pygame or Kivy*
