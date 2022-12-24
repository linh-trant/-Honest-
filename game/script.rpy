# The script of the game goes in this file.

# This will be a basic horror VN. The purpose of the game is making the
# main character fall in love for you and don't want you to leave. When
# you leave, technically it's horror now. 

# define 5 stages of grief
# define not a DDLC bootleg

define e = Character("Elis", color="#4b6043") # Name of the main character. Envy.
define p = Character("[povname]")


define a = 0 # 
define first_time = True

label splashscreen:

    if not persistent.shown_warning:
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

    scene bg room

    show eileen happy

    python: 

        povname = renpy.input("What is your name?", length=10)
        povname = povname.strip()

        while not povname or (povname == "Elis"):
            #block of code to run not povname:
            povname = renpy.input("This is not funny. Once again, I asked, what's your name?", length=10)
            povname = povname.strip()

    e "Welcome, [povname]."
    e "I am glad that I met you. My name is Elis."

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

    return