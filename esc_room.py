from os import name
import time
from playsound import playsound
import random
import sys
import cprint
from esc_assets.visuals.esc_title_art import titleart
from esc_assets.visuals.critical_error import rosscrit
from esc_assets.visuals.francis_hold import digitalholdright, digitalholdleft
from esc_assets.story.smichaud_esc_room import sheanee_story

# This is draft one of the joint hackweek project, presented by (in alphebetical order): Kianna Green, Sheanee Michaud, Quill Cruz.
# We'll be creating a "Choose your own adventure" story using python, hope you enjoy your time exploring!
# here lies our "room" template, which is the module where the player is located, consisting of a story_p, action_p, and two responses, response1, or response2.

# eventloop A (bucket test)

# should add some input expectation here so pressing any key actually dismisses the start screen. Maybe typing in "start" has unintended consequences.

# gameplay loop execution

# Here's the fun ascii intro card and title music!!

titleart()
playsound("esc_assets/music/gamesound.wav")

if input() == ("start"):
    time.sleep(0.5)
    print("Off to a bad start.")
    time.sleep(0.5)
    print(
        "Your first, and perhaps most vital lesson to learn here will be 'Read the words on your screen'."
    )
    print("A simple lesson maybe, but an important one.")
    print("Come back when you are ready.")
    sys.exit()
else:
    print("You have made a grave error. There is no turning back now...")

import esc_assets.story.beginning

import esc_assets.story.story

import esc_assets.story.roomA

# Sheanee's added part -- start
# Room A1's story, action, choice (in a list), and responses (in a list)
sheanee_story(esc_assets.story.beginning.name)

# Ross appears, maybe says a few things
print("Ross appears and says 'Hi camper!")
time.sleep(2)
print(
    "Looks like you're looking to get out of here, right? If you solve my game, you can take your friend and leave this place for good!"
)
time.sleep(3)

# Ross guessing game function here from the riddle.py
import esc_assets.story.riddle

# Sheanee's added part - End
