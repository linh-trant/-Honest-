# The script of the game goes in this file.

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
        
    label end_game:
        if (a==0):
            if first_time:
                e "Already?"
                e "Who doesn't love me?"
            $ a = math.ceil(a + 1)
            e "This must be mistaken! Please choose again!"
            jump loop
        
        if (a==1):
            $ a = math.ceil(a + 1)
            e "You are joking right... Are you sure?"
            jump loop

        if (a==2):
            $ a = math.ceil(a + 1)
            e "[povname]..."
            jump loop

        else:
            if renpy.windows:
                e "THE PATHETIC WINDOW USER!"
                e "[user_uppercase]! I KNOW MORE THAN YOU DO!"
            e "ENOUGH! DIE!"
            
            python:
                import plyer
                from plyer import notification

                notification.notify(
                    title='Elis',
                    message='You cannot never run away from me my dear [user] <3',
                    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                    timeout=10,  # seconds
                ) 
            
            return

    # This ends the game.

    return
