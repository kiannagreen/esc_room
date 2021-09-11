import time
import random
from esc_assets.story.easteregg import picture

# Sheanee added here - Start
# Room A1's story, action, choice (in a list), and responses (in a list)
def sheanee_story(name):
    story_roomA1 = {
        "story": "When making your way into this room, you see Francis and this is a pleasant surprise!",
        "action": "Francis hands you a hammer. Enter 'take hammer' to take the hammer or 'turn down hammer' to have him hang onto it: ",
        "choice": [
            "take hammer",
            "turn down hammer",
        ],
        "response": [
            "You chose to take the hammer and graciously take it from Francis.",
            "You chose to turn down the hammer and tell Francis 'no thank you'.",
        ],
    }

    # Room A2's story, action, choice (in a list), and responses (in a list)
    story_roomA2 = {
        "story": "Francis mentions 'Hey, are you doing okay? Maybe you need to sit down.'",
        "action": "A chair suddenly appears. Enter 'sit' to sit down on the chair or 'no thanks' to keep standing: ",
        "choice": [
            "sit",
            "no thanks",
        ],
        "response": [
            "You mention to Francis 'thank you' and take a seat.",
            "You mention to Francis 'no thanks' and remain standing.",
        ],
    }

    # Room A3's story, action, choice (in a list), and responses (in a list)
    story_roomA3 = {
        "story": "Francis turns to door that also suddenly appears. He says, 'Is this where you wanted to go? Wanna take this drink with you for the road?'",
        "action": "To take the drink, enter 'sure' or to decline the drink enter 'no thanks': ",
        "choice": [
            "sure",
            "no thanks",
        ],
        "response": [
            "You let Francis know you're thankful for the drink and take it. You slowly make your way through the door and into the next room.",
            "You tell Francis you're good and decline the drink. Waving goodbye to Francis, you slowly make your way through the door and into the next room.",
        ],
    }

    # Room B1's story, action, choice (in a list), and responses (in a list)
    story_roomB1 = {
        "story": "This next room is so dark! You begin to say that outloud when a flashlight turns on and Dylan appears!",
        "action": "You're surprised! Type 'scream' to scream in surprise or 'stare' to stare at Dylan in silence: ",
        "choice": [
            "scream",
            "stare",
        ],
        "response": [
            "You scream when seeing Dylan and this makes him jump in surprise.",
            "You stare at Dylan in silence.",
        ],
    }

    # Room B2's story, action, choice (in a list), and responses (in a list)
    story_roomB2 = {
        "story": "Dylan gives a laugh. 'Sorry I scared you, "
        + name
        + ". Wanna take this flashlight? It's kinda dark.'",
        "action": "To take the flashlight, enter 'yes' or to have Dylan continue to hold the flashlight, enter 'no thanks': ",
        "choice": [
            "yes",
            "no thanks",
        ],
        "response": [
            "Dylan says 'Here you go' and hands you the flashlight.",
            "Dylan says 'No worries, I can hang on to it.'",
        ],
    }

    # Room B3's story, action, choice (in a list), and responses (in a list)
    story_roomB3 = {
        "story": "The floor suddenly shakes. 'Is that an earthquake?' Dylan asks.",
        "action": "Enter 'not sure' if you want to tell Dylan you're not sure or enter 'maybe' to let him know you think it's an earthquake: ",
        "choice": [
            "not sure",
            "maybe",
        ],
        "response": [
            "You let Dylan know you're not sure and as he opens his mouth to respond, he and the flashlight suddenly disappear.",
            "You let Dylan know you think it's an earthquake. Just as he's about to respond, he and the flashlight suddenly disappear.",
        ],
    }

    # Easter egg function here
    # def checkEE():

    # Loop
    def room(story, action, choice, response):
        """
        Goes through the loop of reading the story to the player, asking the player for their input, printing their response.

        Args:
        story(str): Displays the digression in the room
        action(str): Prompts player for the action they'd like to take
        choice(str): 2 options player can choose
        response(str): Reiterates what the player would like to do
        """

        # testing easter egg, set value to 0
        # ee = 0
        while True:
            print(story)
            time.sleep(2)
            user_choice = input(action)
            if user_choice == choice[0]:
                print(response[0])
                # testing easter egg -- add part about incrementing easter egg
                ee = round(random.uniform(0.1, 3.5), 2)
                # Test what the ee number is by showing output
                print(ee)
                if ee > 1:
                    picture()
                else:
                    break
                # End easter egg test
                time.sleep(2)
                break
            elif user_choice == choice[1]:
                print(response[1])
                # testing easter egg -- add part about incrementing easter egg
                ee = round(random.uniform(0.1, 3.5), 2)
                # Testing ee value to ensure code fires
                print(ee)
                if ee > 1:
                    picture()
                else:
                    break
                # End easter egg test
                time.sleep(2)
                break
            elif (
                user_choice == "alex"
                or "francis"
                or "ross"
                or "dylan"
                or "imandra"
                or "michael"
            ):
                picture()
                break
            else:
                print(
                    "Some force hinders your attempt, and despite your efforts you cannot will this action to be. Choose "
                    + "'"
                    + choice[0]
                    + "'"
                    + " or "
                    + "'"
                    + choice[1]
                    + "'"
                )
                time.sleep(2)

    # List of rooms
    story_parts_room = [
        story_roomA1,
        story_roomA2,
        story_roomA3,
        story_roomB1,
        story_roomB2,
        story_roomB3,
    ]

    # Actual game play. Goes through the loop of each room/digressions defined in story_parts_room variable above
    for room_story in story_parts_room:
        room(
            room_story["story"],
            room_story["action"],
            room_story["choice"],
            room_story["response"],
        )


# Sheanee added here - End
