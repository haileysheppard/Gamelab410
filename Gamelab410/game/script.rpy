define m = Character("Eufrid")
define c = Character("Cordula")
define e = Character("Emil")
define s = Character("Síofra")

image MC happy = "Test2.png"
image MC sad = "Test3.png"
image Emil1 = "Emil1.png"
image bakery1 = "images/BakeryFinal.png"
image placeholder1 = "images/placeholder1.png"
image placeholder2 = "images/placeholder2.jpg"
image nothing = "images/Blank.jpg"
image town = "images/PLACEHOLDERTOWN.png"
image start = "images/PlaceholderStart.png"
image Fountain = "images/Fountain.png"

default visited = set()

screen Nothing():
    imagemap:
        ground "start"
        hotspot (613, 240, 620, 510) action Jump("dialogue") tooltip "..."

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

screen forest_path():
    imagemap:
        ground "images/BakeryFinal.png"
        hotspot (233, 345, 419, 191) action Return("Bread")      tooltip "Bread"
        hotspot (660, 164, 406, 177) action Return("Jars")       tooltip "Jars"
        hotspot (664, 628, 372, 108) action Return("Pastries")   tooltip "Pastries"
        hotspot (0, 611, 394, 247)   action Return("FreshBread") tooltip "Fresh Bread"

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

label start:
    "Freedom and Life are earned by those alone who conquer them each day anew."
    "To live is to keep moving forward, no matter what."
    "The world does not wait for anyone."
    
    call screen Nothing
    m "What is that...?"

label dialogue:
    m "..."
    "You need to get moving"
    m "..."
    "There is no point in standing around."
    m "..."

    jump town

label town: 
    scene town
    "The year was 18xx. The town of Kleinsee was busy preparing for its biggest event of the year. The PLACEHOLDER Festival."
    "The Festival brought in guests from all across the country."
    "The PLACEHOLDER Festival was a yearly event that took place over the course of three days. It was full of local foods and fun."
    "On the final day, there is a large dance that involves both the townsfolk and any visitors. That was what made the final day the most popular."

    m "And with that preparations for tomorrow are complete!"
    "I had just finished up all my prep work for the festival. This year I was helping my parents with their stall for the festival."
    "I normally just had a minor vending role but this year they let me participate in the whole set-up."
    m "Now that I have some free time I might as well wander around for a bit."

    menu:
        "Now that I had some free time I wanted to"

        "Go to the bakery":
            jump bakery
        
        "Look for Cordula":
            $ Search_Cordula = True
            jump Search_Cordula

        "Wander around the town":
            $ stayhere = True
            jump StayHere
        
   
label Search_Cordula:
"Cordula was a friend I have had ever since my childhood. She moved to Kleinsee when she was eight, and we had been friends ever since."
"She spent most of her free time around the fountain. It was there that she liked to play her Harmonica for tips."
scene Fountain
"Cordula was gracefully playing her Harmonica in the middle of the fountain square. She had garnered a small crowd."
# Add sound effects here. Some for crowd + possibly find a harmonica track.
"I watched her for a couple of minutes until she reached the end of her song. She then looked up and finally noticed me."

show Emil1
#Emil is here as a placeholder
c "To what do I owe the please?"
"Cordula gave me a sly look."
m "I just finished all my preperations and wanted to see something more exciting."
c "I think anything is more exciting than setting up a table all day."
m "That's why I came to see you and not anyone else."
"Cordula playfully shoved me. This type of banter was normal between  us."



return

label bakery:
    scene bakery1

label bakery_loop:
    call screen forest_path
    $ spot = _return

    if spot == "Bread":
        m "Wow, it looks like they are prepping a lot."
        m "I guess it makes sense, the festival starts tomorrow..."
        m "Maybe I should've done more prep..."

    elif spot == "Jars":
        m "I see these jars everyday yet I still don't know what they are for."

    elif spot == "Pastries":
        m "Wow, that smells divine."
        m "I wonder if they could sneak me a piece..."

    elif spot == "FreshBread":
        m "Looks freshly made."
        m "I wonder if they made it."

    $ visited.add(spot)

    if len(visited) == 4:
        jump all_viewed

    jump bakery_loop

label all_viewed:
    m "They don't seem to be coming back anytime soon. I should probably leave."
    play audio "audio/Door.mp3"
    m "?"
    show Emil1
    e "Hello Eufrid. What are you doing here?"
    "This is just the person I was looking for."
    "This is Emil. We have known each other since we were kids."
    "He has been working at the bakery since he was fourteen. If he's feeling nice he will sneak Cordula and I some treats."
    e "Eufrid...?"
    m "Sorry, what were you saying?"
    e "I was just asking you what you are doing here."
    
    menu:
        "How should I respond"

        "Just wandering around":
            e "I guess that makes sense."
            m "Well, I guess I should get a move on. Wouldn't want to distract you."
            e "Don't worry about it! It was nice to see you!"
            jump after_chat

        "None of your business":
            $ NoneOfYourBusiness = True
            e "What do you mean none of my business!"
            m "I don't think your boss would agree with that."
            e "That's not the point right now. Stop messing around."
            m "I was just wandering around. Don't be so dramatic."
            m "I was just about to leave anyways."
            e "Okay... see you later."
            jump after_chat

        "Nothing":
            $ Nothing = True
            e "Doesn't seem like nothing. But who am I to judge."
            m "Yeah. Who are you to judge?"
            e "... I'm just gonna get back to work."
            m "(I guess that means I should leave.)"

            jump after_chat

label after_chat:
    m "Bye! See you tonight!"

    