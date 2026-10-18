define m = Character("Eufrid")
define c = Character("Cordula")
define e = Character("Emil")
define s = Character("Síofra")
define em = Character("Emil & Eufrid")
define v = Character ("Man")

image MC happy = "Test2.png"
image MC sad = "Test3.png"
image Emil1 = "Emil1.png"
image Siofra1 = "Siofra.png"
image Cordula1 = "Emil1.png"
image bakery1 = "images/BakeryFinal.png"
image nothing = "images/Blank.jpg"
image town = "images/Stalls2.png"
image start = "images/PlaceholderStart.png"
image Fountain = "images/fountain2.png"
image Fountain_Night = "images/Fountain_Night.png"
image Stalls = "images/Stalls2.png"
image Stalls_Night = "images/Stalls1.png"


default visited = set()
default did_bakery = False
default did_cordula = False
default did_wander = False

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

label town_menu:
    if did_bakery and did_cordula and did_wander:
        jump MeetUp1

    menu:
        "Now that I had some free time I wanted to"

        "Go to the bakery" if not did_bakery:
            $ did_bakery = True
            jump bakery

        "Look for Cordula" if not did_cordula:
            $ did_cordula = True
            jump Search_Cordula

        "Wander around the town" if not did_wander:
            $ did_wander = True
            jump StayHere
   
label Search_Cordula:
"Cordula was a friend I have had ever since my childhood. She moved to Kleinsee when she was eight, and we had been friends ever since."
"She spent most of her free time around the fountain. It was there that she liked to play her Harmonica for tips."
scene Fountain
"Cordula was gracefully playing her Harmonica in the middle of the fountain square. She had garnered a small crowd."
# Add sound effects here. Some for crowd + possibly find a harmonica track.
"I watched her for a couple of minutes until she reached the end of her song. She then looked up and finally noticed me."

show Cordula1
#Emil is here as a placeholder
c "To what do I owe the please?"
"Cordula gave me a sly look."
m "I just finished all my preperations and wanted to see something more exciting."
c "I think anything is more exciting than setting up a table all day."
m "That's why I came to see you and not anyone else."
"Cordula gave me a playful shove." 
c "How did the setup for your parents' stall go?"
m "It was surprisingly simple. I just had to make sure the main stars of our stall were all front and center. "
m "For the placement of everything else I just played it by eye."
c "I can't wait to see it tomorrow. Are you working all the time the whole day tomorrow?"
m "Unfortunately, yes. I am working from dawn to dusk tomorrow."
"Cordula frowned." 
c "Hm... It will at least be exciting. I have already heard talk of visitors arriving."
m "It will be a lot of work. I just hope I will have some downtime at somepoint."
c "Again, at least you will be busy. You won't just be standing around all day waiting for a customer to appear."
m "I suppose that you could look at it that way."
m "Either way, I have a lot to think about."
"I started to leave."
c "See you later tonight!"

jump town_menu



label StayHere:
scene Stalls
"I went to look at the rest of the festival stalls. I hadn't been able to get a look at any while I was setting up our stall."
"This year the amount of stalls doubled. It seemed like the mayor really wanted to make sure this year had a big turnout."
"I heard he had even reached out to foreign vendors, hence why the stall numbers had doubled. I was curious to see what these new vendors had up their sleeve."
"I moved towards one of the new vendors. When I was preparing I caught a glimpse of this stall. It was full of curiosities I had never seen before." 
"As I got closer to the stall I noticed the vendor. She was also unlike anything I had seen before." 
show Siofra1
"She had ghastly features and sunken in skin. It fit her stall in some way, an odd person for an odd stall."
"The vendor looked up at me. Seemingly a little irate."
s "..."
m "...Hello, I'm Eufrid. I'm also a vendor here. My stall is right down the way."
"I pointed towards the town center. My family had gotten a decent spot this year, despite the new entries."
s "I see..."
"I frowned a bit. It didn't seem like this woman was one for conversation." 
m "What's your name? I don't think I have seen you around these parts before." 
"I tried to keep being friendly. I wanted to make sure we left an impression on all the newcomers here, hopefully that meant they would want to return next year."
s "...Siofra."
"An interesting name to say the least. I had never heard of such a name before this." 
m "Well, it's nice to meet you, Siofra. Hopefully, I'll have some free time to check out your stall during the festival."
"Siofra gave a slight smile."
s "I hope so as well."
"The way she smiled frightened me a bit. It reminded me of a rabid horse I had a run in with as a child." 
"But I wasn't one to judge off of appearances, so I tried to keep that thought out of my mind."
# have to figure out how to set this as visited/ figure out if want to force players to visit all things 
jump town_menu


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

        "None of your business":
            $ NoneOfYourBusiness = True
            e "What do you mean none of my business!"
            m "I don't think your boss would agree with that."
            e "That's not the point right now. Stop messing around."
            m "I was just wandering around. Don't be so dramatic."
            m "I was just about to leave anyways."
            e "Okay... see you later."

        "Nothing":
            $ Nothing = True
            e "Doesn't seem like nothing. But who am I to judge."
            m "Yeah. Who are you to judge?"
            e "... I'm just gonna get back to work."
            m "(I guess that means I should leave.)"


label after_chat:
    m "Bye! See you tonight!"
    jump town_menu

label MeetUp1:
    scene Fountain_Night
"After all that excitement, it was almost dusk. Which meant it was almost time for my favorite part of the day."

"Cordula, Emil and I had a daily tradition. Each day at dusk we would meet up in the Town Center and spend time together."

"We had been doing this since we were kids. At first it was just an excuse to ditch our chores, but now it had become a tradition."

"As I approached the center, I saw Cordula and Emil both in the distance. It seemed like I was the last to arrive today. Damn." 

show Emil1 at left
show Siofra1 at right

"Emil walked up to me and pointed an accusatory finger at me."
e "What took you so long? I was beside myself with worry."
"He hugged himself. He was trying to look as scared as possible, but I knew his tricks by now."

menu:
    "I..."
    "Felt Annoyed":
        "I gave him a stern glare."
        e "Woah. I was just playing around. No need to look so upset."

    "Played along":
        "I got on my hands and knees and started to beg for forgiveness."
        m "I am ever so sorry Emil. I can't believe I wasted your precious time."
        e "Hm... What shall this peasant's punishment be."

c "Cut it out you two."
# Sad sfx here. 
em "Sorry Cordula."
"Cordula's voice cut through our argument. It took us but a second to calm down before Cordula continued."

c "So, did anything interesting happen to either of you today?"
"I thought for a moment, did anything of note happen today. That woman I met at the stalls came to my mind."
"I looked toward Emil. He also seemed to be in thought."
"Before either of us could respond a hysterical voice rang out. We all looked towards the speaker. "
v "It's all true you know!"
"The man was slurring his word, he was probably just a visiting drunk."
v "I know what I saw. There was most definitely something, something demonic, or what not attacking that woman."
"At this I perked up, maybe there was some merit to this man's rambling."
"Before I could continue this line of thought someone ushered the man back into the local inn."
"For a while none of us spoke until Emil finally broke the silence."
e "I assume we will be seeing a lot more of those types of people during the festival."
"He tried to play it off as a joke, but the prospect made me worry a bit."
c "I hope not. Think of the mess that could cause."
"Emil and Cordula continued to argue about whether or not raving drunks was a good thing or a bad thing."
"I did not speak up during the conversation, I could not get my mind off of that man."
"Why would a drunken rant turn into a story like that? There had to be some truth to the story."
"Emil and Cordula had stopped arguing and were giving me curious looks."
c "Are you feeling tired? Should we leave it for today?"
"Cordula gave a concerning look, and looked towards Emil."
c "Right, Emil?" 
"Emil was staring off. When he heard Cordula's voice he seemed to remember where he was."
e "Yeah, I was getting tired too. I think I am going to head back."
"I agreed with them, and with that we parted for the day."
label Night:
    scene black



