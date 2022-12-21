# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# This will be a basic horror VN. The purpose of the game is making the
# main character fall in love for you and don't want you to leave. When
# you leave, technically it's horror now. 

# define 5 stages of grief
# define not a DDLC bootleg

define e = Character("Elis") # Name of the main character. Envy.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Test the framework. Completed."

    # This ends the game.

    return
