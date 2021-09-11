import time

action_pA1 = "Which door do you walk through? Type 'red' to walk through the red door or 'blue' to walk through the blue door: "
user_actionA1 = ["red", "blue"]
responseA1 = [
    """As you open the red door and take your first step, you realize there's no floor to step on and you fall down a hole. 
Luckily, you fall onto a mattress. As you stand to get your balance, you notice you're in a kitchen.""",
    """You walk through the blue door and make your way into another room. You notice you're in a dining room. """,
]

story_p_2 = (
    "You see Alex sitting in the middle of the room, smiling, with a book in her hand."
)
action_pA2 = "You walk up to her and she hands you the book. Do you take the book and open it or do you throw the book across the room? Type 'take' to take the book or type 'throw' to throw the book across the room: "
user_actionA2 = ["take", "throw"]
responseA2 = [
    "You take the book and open it. You realize it's empty and there's nothing inside. You decide to give it back to Alex.",
    "You throw the book across the room and Alex laughs.",
]

story_p_3 = "She says, 'That book is the key to your escape'. Before you can grab the book, it suddenly disappears. Alex then turns to you and says, 'In order to advance to the next room, you need to solve this riddle. Do not cheat. Cheaters will be punished.'"
action_pA3 = "What is the answer to my riddle, 'Where does today come before yesterday'. (Note: the answer is only one word): "
user_actionA3 = ["dictionary", "dictionary"]
responseA3 = [
    "'You solved my riddle!' A door magically appears and you walk through it.",
    "You got it wrong. You fall through a hole that takes you to a different room.",
]

while True:

    action = input(action_pA1)

    if (action) == (user_actionA1[0]):
        time.sleep(1)
        print(responseA1[0])
        time.sleep(2)
        break

    elif (action) == (user_actionA1[1]):
        print(responseA1[1])
        time.sleep(2)
        break

    else:
        print("THAT IS NOT A VALID OPTION. Try again...")
        time.sleep(2)


print(story_p_2)
time.sleep(2)
while True:

    action = input(action_pA2)

    if (action) == (user_actionA2[0]):
        print(responseA2[0])
        time.sleep(2)
        break

    elif (action) == (user_actionA2[1]):
        print(responseA2[1])
        time.sleep(2)
        break

    else:
        print("THAT IS NOT A VALID OPTION. Try again...")
        time.sleep(2)


print(story_p_3)
time.sleep(2)
while True:

    action = input(action_pA3)

    if (action) == (user_actionA3[0]):
        print(responseA3[0])
        time.sleep(2)
        break

    else:
        print(responseA3[1])
        time.sleep(2)
        break