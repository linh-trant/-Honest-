label end_game:

    scene classroom
    show elis

    init python: 
        if renpy.exists("ILOVEYOU.txt"):
            layout.QUIT = "DON'T YOU DARE TO LEAVE ME! STAY!"

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
                message='You cannot never run away from me my dear <3',
                app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                timeout=10,  # seconds
            )  

        $ persistent.comeback = True
        $ renpy.quit()