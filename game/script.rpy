# The script of the game goes in this file.

# This will be a basic horror VN. The purpose of the game is making the
# main character fall in love for you and don't want you to leave. When
# you leave, technically it's horror now. 

# define 5 stages of grief
# define not a DDLC bootleg

image elis = "Elis_cut.png"
image classroom = "background.png"

define e = Character("Elis", color="#86DC3D") # Name of the main character. Envy.
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

        show text "This game contains scenes of graphic violence and brutal depictions of horror." with dissolve
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

        # Import time from Window
        from datetime import datetime

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

    $ renpy.notify(current_time)

    e "Hello? Are you okay? Why you are laying down here like this?"

    scene classroom
    show elis

    e "Are you okay? Do you need any help? What's your name?"

    python: 

        povname = renpy.input("What is your name?", length=10)
        povname = povname.strip()

        while not povname or (povname == "Elis"):
            #block of code to run not povname:
            povname = renpy.input("This is not funny. Once again, I asked, what's your name?", length=10)
            povname = povname.strip()

    e "Oh, so you are [povname]-senpai. I have heard your name pretty much today!"
    e "I am glad that I met you. My name is Elis, freshman."

    scene black
    show text "1 week later" with dissolve
    with Pause(3)

    scene classroom
    show elis

    $ renpy.notify(current_time)

    e "We have been with each other for so long! I-I am so glad."
    e "I know I have always said /'I hate you/', but... I have something to confess."

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
        e "I love you! Let's continue! I will make sure that we will be together forever!"
        jump loop

    return