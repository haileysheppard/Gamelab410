define m = Character("MC", image="Test")
image MC happy = "Test2.png"
image MC sad = "Test3.png"
define f = Character("Friend1")
define s = Character("Síofra")

image scary = "images/scary.jpg"
image nothing = "images/nothing.jpg"

screen Nothing():
    imagemap:
        ground "images/Blank.jpg"
        hotspot (613, 240, 620, 510) action Jump("dialogue") tooltip "..."

    $ tooltip = GetTooltip()
    
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

screen forest_path():
    imagemap:
        ground "images/bakery.png"
        # hover "images/FOREST_hover.jpg"   # optional: shows a highlight on hover

        # hotspot (x, y, width, height)
        hotspot (242, 199, 120, 100) action Jump("scary") tooltip "Mysterious noises are coming from this area."
        hotspot (378, 172, 120, 100) action Jump("nothing") tooltip "Nothing of note."

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

# The game starts here.

label start:
    show MC happy
    m "..."
    m "There's nothing here"
    call screen Nothing
    m "What is that...?"


label dialogue:
    show MC sad
    m "Huh?"
    m "Where is this...?"
    call screen forest_path

label scary:
    scene scary
    "Ahh so scary..."
    return

label nothing:
    scene nothing
    "Ahh so normal..."
    return