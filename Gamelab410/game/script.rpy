# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MC")
define f = Character("Friend1")
define s = Character("Síofra")

screen forest_path():
    add "images/FOREST.jpg"
    imagemap: 
        ground "images/FOREST.jpg"
        hotspot (242, 199, 2, 0) action Jump("scary") tooltip "Mysterious noises are coming from this area."
        hotspot (378, 172) action Jump ("nothing") tooltip "Nothing of note."

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]" xalign 0.5 yalign 0.75

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene forest_path
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "This is a test of the spot selection mechanic."
    call screen forest_path

    return
#Label scary
    scene scary
    "Ahh so scary..."
    return

#Label nothing
    scene nothing
    "Ahh so normal..."
    return
