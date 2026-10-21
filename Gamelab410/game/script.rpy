define m = Character("Eufrid")
define c = Character("Cordula")
define e = Character("Emil")
define s = Character("Síofra")
define em = Character("Emil & Eufrid")
define v = Character ("Man")
define ow = Character ("Old Woman")
define t = Character ("Visitor")

image Emil1 = "Emil1.png"
image Siofra1 = "Siofra.png"
image Cordula1 = "CordulaPlaceholder.png"
image bakery1 = "images/BakeryFinal.png"
image nothing = "images/Blank.jpg"
image town = "images/Stalls2.png"
image start = "images/PlaceholderStart.png"
image Fountain = "images/fountain2.png"
image Fountain_Night = "images/Fountain1.png"
image Stalls = "images/Stalls2.png"
image Stalls_Night = "images/Stalls1.png"
image Lake = "images/Lake1.png"
image LakeGlow = "images/LakeGlow.jpg"

default visited = set()
default investigated = set()
default did_bakery = False
default did_cordula = False
default did_wander = False
default Lake = False
default Noises = False
default ElderlyWoman = False
default WorkingMan = False
default YoungVisitor = False

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
hide Cordula1

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
m "...Good afternoon, I'm Eufrid. I'm also a vendor here. My stall is right down the way."
"I pointed towards the town center. My family had gotten a decent spot this year, despite the new entries."
s "I see..."
"I frowned a bit. It didn't seem like this woman was one for conversation." 
m "What's your name? I don't think I have seen you around these parts before." 
"I tried to keep being friendly. I wanted to make sure we left an impression on all the newcomers here, hopefully that meant they would want to return next year."
s "...Siofra."
"An interesting name to say the least. I had never heard of such a name before this." 
m "Well, tis nice to meet you, Siofra. Hopefully, I'll have some free time to check out your stall during the festival."
"Siofra gave a slight smile."
s "I hope so as well."
hide Siofra1
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
    e "Good afternoon Eufrid. What are you doing here?"
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
            e "What do you mean none of my business!"
            m "I don't think your boss would agree with that."
            e "That's not the point right now. Stop messing around."
            m "I was just wandering around. Don't be so dramatic."
            m "I was just about to leave anyways."
            e "Okay... see you later."

        "Nothing":
            e "Doesn't seem like nothing. But who am I to judge."
            m "Yeah. Who are you to judge?"
            e "... I'm just gonna get back to work."
            m "(I guess that means I should leave.)"


label after_chat:
    m "Bye! See you tonight!"
    hide Emil1
    jump town_menu

label MeetUp1:
    scene Fountain_Night
"After all that excitement, it was almost dusk. Which meant it was almost time for my favorite part of the day."

"Cordula, Emil and I had a daily tradition. Each day at dusk we would meet up in the Town Center and spend time together."

"We had been doing this since we were kids. At first it was just an excuse to ditch our chores, but now it had become a tradition."

"As I approached the center, I saw Cordula and Emil both in the distance. It seemed like I was the last to arrive today. Damn." 

show Emil1 at left
show Cordula1 at right

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
v "Tis all true you know!"
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
"I went home and immediately went to my bed. I was exhausted from all the prep work I did today and it was already fairly late." 
"I fell asleep with little struggle."
play audio "audio/Wake.mp3"
# MC bedroom Placeholder in future?
"I awoke to a wolf howling in the distance."
"It did not bother me too much, since it was just about time for me to make my way over to the stand."
"I got dressed for the day and left my home with little fanfare. "
scene town
"I left my home in a hurry. As I walked along the empty streets I heard a noise."
play audio "audio/Growl.mp3"
"It stopped me in my tracks. I looked around, but failed to see anything out of the ordinary so I continued to make my way to the stand."
scene Stalls
"Since I had prepped everything yesterday I had little to do other than get out a few items that were to be displayed directly on the counter." 
"After that was complete it was just about time for the first day of the festival to begin."
    # add bustling sfx
scene Stalls
$ renpy.notify("Festival Day 1")
"The crowds came in little time. I tended to the stall with fervor."
"Throughout the day I overheard many different conversations."

menu:
    "I focused in on talk of"

    "The Lake":
        $ Lake = True
        "I heard a couple telling a small group of people about an incident that occurred in the lake."
        "The couple resided on the lake and heard strange splashing noises last night."
        "The husband went out to investigate and saw an abnormal glow in the water."
        "As he moved closer he started hearing a melody. It supposedly had been sung in such a beautiful voice that the man could not help but move even closer."
        "He had almost made it into the water when his wife yelled at him to come back inside."
        "He immediately complied."
        

    "Mysterious Noises in the Streets":
        $ Noises = True
        "I heard a group of kids talking about noises they heard in the street last night."
        "One of the kids lives above one of the local shops, and was out late at a friend's house."
        "On his way back he walked along the main promenade by himself."
        "As he got closer to his home he started to hear a baby's cry. Worried he started to search around for the source."
        "He reached an ally that seemed to be where the sound was coming from and searched down it."
        "There he found nothing, soon after the cries stopped."
        "With nothing else to do he headed back to his home like he originally planned."

"The rest of the festival went off with little fanfare. We ended up making a record first-day selling."
"All the day-stalls around me were preparing to close, so I did the same."
"My energy was all but drained, but I still had to go and meet up with Cordula and Emil."

label Night1:
scene Fountain_Night
$ renpy.notify("Night 1")
"When I reached the fountain only Cordula had arrived. She was sitting on the fountain cleaning her harmonica."
"The sun was just about to set and the fountain was awash with the colors from the sky. She looked up as I got closer."
show Cordula1
m "Seems like Emil is the loser today."
c "Seems like it... Sorry I did not get a chance to stop by your stall today."
m "It's okay. Were you able to get a lot of tips today?"
"Cordula had been planning on playing at the fountain most of the day, which is probably how she managed to beat me here."
c "I think I got the most tips I have ever gotten. I made a good choice in bringing out my  harmonica.
C A lot of the outsiders have never seen something like it, so I was able to garner a great crowd."
# add sfx here
"A crash could be heard from the distance. I looked behind me to see Emil, fallen into a bush."
"It seemed like he had been trying to sneak up on us but had gotten too nosy. He brushed himself off then made his way over to us."
hide Cordula1
show Cordula1 at left
show Emil1 at right

e "Good evening you two. Having all this fun without me?"
"Emil tried to play it off like we hadn't seen him in a bush naught but a couple seconds ago."
c "Eufrid only arrived a couple of minutes ago. We have not had too much time to talk."
"Emil again tried to act as though he was not listening in on us. "
e "I see, well now that I am here let us truly begin!"
e "I am sure you both had as exciting days as myself. I must have made a'hundred loaves of bread."
"Emil wiped non-existent sweat off of his brow."
c "I made quite a fair bit of coin today. It seems the novelty of the harmonica is not lost on the tourists."
e "What about you Eufrid? How'd the stall go?"
m "We made a record profit! I also overheard some interesting rumours. I was thinking we could explore those tonight."
"When we were younger, we all used to try and explore anything mysterious that occurred in Kleinsee."
"Now that we were older, we of course didn't do this very often."
"But those rumours I heard today, had me intrigued."

if Lake:
    jump lake_start
else: 
    jump street_start

label lake_start:
    "I told Emil and Cordula what I heard about the lake."
    e "Sounds interesting. I can barely remember the last time I visited the lake."
    c "Tis getting quite dark. I should do well to grab a lantern."
    hide Cordula1
    hide Emil1
    "Cordula went towards her home. Leaving Emil and I alone for but a couple of minutes."
    "We casually spoke about what else occurred in our respective days."
    "It did not take long for Cordula to return. Her home was located next to the chapel in town, not too far at all from the fountain."
    scene Stalls_Night
    "We went towards the lake with Cordula's lamp lighting our way, passing by the now empty stalls as walked."
    "Eventually, we reached the shore of the lake."
label lake:
    scene Lake
"This was the first time I had seen the lake at night since I was a child."
"There used to be a festival that took place near the lake, but ten years ago they stopped doing it."
"I was still young then, so I did not quite know the reason why. Even now I never searched for an answer."
show Emil1
e "Wow, the lake is a little eerie at night, ain't it?"
"Emil broke the silence, his voice shaking a bit. He had never been great with the night, even now as an adult."
"Though, I would tend to agree with what he said. There was a certain vastness to lakes in the dark." 
hide Emil1 
show Cordula1 at left
show Emil1 at right

c "Let us investigate this as quickly as possible. We all still have to work tomorrow."
"Wasting time was never Cordula's forte. With that we got to work."
hide Cordula1
hide Emil1

screen lake():
    imagemap:
        ground ("images/Lake1.png" if "Glow" in investigated else "images/Lake1.png")
        hover "images/LakeGlow.jpg"
        hotspot (966, 111, 220, 327) action Return("Boat") tooltip "Boat"
        hotspot (1577, 266, 267, 128) action Return ("Manor") tooltip "Manor"
        hotspot (17, 0, 787, 399) action Return ("Tree") tooltip "Tree"
        if "Glow" not in investigated:
            hotspot (1456, 390, 308, 162) action Return ("Glow") tooltip "?"


    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

label lake_loop:
    $ renpy.notify("Night 1 Investigation")
    call screen lake
    $ spot = _return

    if spot == "Boat":
        "In the distance, there is a boat."
        "Tis awfully late for someone to be out fishing. I wonder who it could be?"

    elif spot == "Manor":
        "The manor is illuminated by a large amount of lights. It must be expensive to upkeep."
        show Cordula1
        c "I think that is where the mayor lives."
        m "Intresesting. I don't think I have ever been in that area."
        c "The road to get there is private. There's a fence up. I don't think he wants us in his space."
        m "I see. I suppose that makes enough sense."
        hide Cordula1

    elif spot == "Tree":
        show Emil1
        e "Don't the branches on that tree make it look a bit like a flash of lightning."
        m "It is a very spindly tree, so I suppose I can see it."
        hide Emil1
        "I didn't see anything else of note on the tree."
        
    elif spot == "Glow":
        "... What is that in the distance. I didn't see it a second ago." 
        # add scary singing here. 
        show Cordula1
        c "Do you two hear that?"
        "A faint singing could be heard coming from the lake. I was unable to parse out what exactly was being sung."
        "Emil tried to speak but Cordula shushed him before he could get out what he wanted to say."
        "We all stayed quite, listening to the singing. After a couple of minutes it faded, and with that the glow also faded."

    $ investigated.add(spot)

    if len(investigated) == 4:
        jump lake_investigated

jump lake_loop

label lake_investigated:
    m "I think we looked at everything around here. Should we start heading back?"
    show Cordula1
    c "Yes, it is getting quite late."
    # consider having a forest background or something. forest pathway?
    hide Cordula1
    scene black
    "We made our way back towards the town."
    scene Stalls_Night
    "Once we arrived it took a while for anyone to speak of the glow we saw, but eventually Cordula brought it up."
    show Cordula1 at left
    show Emil1 at right 
    c "We are all in agreement that what we saw today was the same phenomenon as what Eufrid heard about today, right?"
    e "But none of us were drawn to the water. Or at least I was not. Were you two at all?"
    c "Not particularly, no."
    m "Nor, I"
    hide Emil1
    hide Cordula1
    "We walked in silence for the rest of the journey. Everyone was still contemplating what that glow meant."
    "We all separated for the night. We didn't have time to think about the implications, we all had to work tomorrow." 
    "As I made my way home I thought back to the voice we heard."
    "It had a cadence to it that I had never heard before. It was almost inhuman."
    jump EndNight1

label street_start:
if Noises:
    "I told Cordula and Emil what I heard about mysterious noises in the street."
    show Cordula1 at left
    show Emil1 at right
    c "Sounds intriguing. I was unable to hear such a noise last night though."
    "Cordula lived next to the local chapel. It was also located near the main square."
    c "Still I think we should try and investigate. What do you all think?"
    e "I see no reason not to. It is too early to go to bed quite yet."
    m "I agree, I am rather curious about these noises. It could be just a kid's ramblings, or it could be something much deeper than that."
    hide Emil1
    hide Cordula1
    "With that we went off to the town to question other residents and visitors."
    "Gas lamps lined the streets, illuminating the night."
    "They had only been installed recently, most likely to help this year's festival."
    "We soon reached our destination and began to start our questioning."

label Questioning1:
    $ renpy.notify("Night 1 Questioning")
    if ElderlyWoman and WorkingMan and YoungVisitor:
        jump EndQuestioning1

    menu:
        "Who should I question?"

        "Elderly Woman" if not ElderlyWoman:
            $ ElderlyWoman = True
            "We walked towards an elderly woman. I vaguely recognized her, she had lived in this town for a long time. She might have some interesting information."
            m "Good evening, we were just wondering if you heard any strange noises last night?"
            ow "The only thing I heard last night was my worthless husband's ramblings."
            "I flinched a bit. I didn't expect her to be so honest about that type of thing. Emil started to whisper to me."
            show Emil1
            e "I do not think she has any information about this. She seems too focused on her personal life."
            "I whispered back."
            m "It certainly seems that way."
            hide Emil1
            jump Questioning1

        "Working Man" if not WorkingMan:
            $ WorkingMan = True
            show Cordula1
            "Cordula seemed to recognize this man, so she took the initiative."
            c "Good evening sir, would you mind if we spoke for a moment?"
            v "I do not see why not? What is the matter?"
            "Cordula seemed to have this handled, so I elected to let her converse with this man."
            c "Last night, did you hear anything out of the ordinary?"
            v "Last night I was working at the Inn all night. I was a welcomer for all the new guests." 
            v "I personally did not hear anything but I heard talk from guests about a strange voice near the entrance of town." 
            "We all gave each other looks. This was the type of information we were looking for. The man continued."
            v "From what I understand it sounded like a young woman, but the voice was strained and raspy."
            v "Quite a frightening tale if you ask me."
            hide Cordula1
            "Cordula bid the man farewell."
            jump Questioning1

        "Young Visitor" if not YoungVisitor:
            $ YoungVisitor = True
            "Emil walked up to a young woman. She seemed to be from out of town, or at least she had an air to her like she was." 
            show Emil1
            e "How do you do?"
            "He attempted to put on a suave act. Cordula and I shared a knowing look."
            "The traveler seemed surprised by Emil's attitude. But none the less spoke with him."
            t "I am doing quite fine, thank you. This town is such a beauty."
            "Emil conversed with the woman for a considerable amount of time." 
            "After an unquantifiable amount of time Emil finally asked the woman about the noises."
            t "I did hear something strange on the way back to the Inn last night."
            t "It sounded like a combination of cuckoo and a goat. It was quite a thing to hear late at night."
            t "It gave me a fright, so I hurried back to the Inn."
            e "I see, that must have been hard for you."
            hide Emil1
            "Emil went back to sweet talking the woman while Cordula and I thought of what to do next." 
            jump Questioning1

label EndQuestioning1:
    "After we spoke to everyone we went over what we found out."
    "We parted for the day on that note, all of us had to work in the morning. So we had to wait to figure out what to do next. There was no need to rush things."
    "I walked home thinking about what I learned today."
    jump EndNight1

label EndNight1:
    scene black
    $ renpy.notify("End of Night 1")
    "With that I reached my home and went to bed."
    "End of Game for now! :D"
    return