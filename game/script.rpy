﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# This will be a basic horror VN. The purpose of the game is making the
# main character fall in love for you and don't want you to leave. When
# you leave, technically it's horror now. 

# define 5 stages of grief
# define not a DDLC bootleg

define e = Character("Elis") # Name of the main character. Envy.
define p = Character("[povname]")

# The game starts here.

define a = 0 # To make Ren'Py treat this as Python, add a $
define first_time = True

label splashscreen:

    if not persistent.shown_warning:
        # Show warning here
        $ persistent.shown_warning = True

    scene black

    show text "This is a demo. Final may game be subject to change." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    return



label start:

    init python:
        import math
        import os

        # Import real username from Window

        from os import getlogin
        device_username = getlogin()
        user = device_username.split(" ",1)[0]
        user_uppercase = str.upper(user)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    python: 

        povname = renpy.input("What is your name?", length=10)
        povname = povname.strip()

        while not povname:
            #block of code to run not povname:
            povname = renpy.input("Once again, I asked, what's your name?", length=10)
            povname = povname.strip()

    e "Welcome, [povname]."
    e "I am glad that I met you."

    jump loop

    label loop: 
        e "I love you, do you love me?"

        menu: 
            "I love you.":
                $ first_time = False
                jump continue_choice

            "I am leaving you.":
                jump end_game

    label continue_choice:
        e "I love you! Let's continue!"
        jump loop

    # This ends the game.

    return