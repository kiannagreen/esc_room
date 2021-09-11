import random
import time
from playsound import playsound
from visuals_temp.francis_hold import digitalholdleft, digitalholdright

# Limits user to four guesses
guesses_remaining = 4

# Randomly choose winning number
winning_number = random.randint(1, 10)


digitalholdleft()
digitalholdright()
print("You have four attempts to guess the correct number. Good luck...")

while guesses_remaining > 0:

    while True:
        try:
            guess = int(input("\nGuess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                break  # Exit 'while True' loop
            else:
                playsound("esc_assets/music/Rossfatal.mp3")
                print("Your guess was NOT a number between 1 and 10. Try again.")
        except:
            playsound("esc_assets/music/Rossfatal.mp3")
            print("Your guess was NOT an integer. Try again.")

    # Decrease guess counter by one each time to limit to four guesses.
    guesses_remaining -= 1
    if guess == winning_number:
        print("You guessed the correct number.")
        time.sleep(2)

        print("Ross frowns and slowly fades into nothing.")
        time.sleep(2)

        print(
            "A door appears and you walk through it to find your friend unharmed. You both eventually found an exit through the basement that led to the outside world. You made your way back to the front of the cabin, jumped into your car and drove away. You never looked back."
        )
        time.sleep(5)

        print("EPILOGUE")
        time.sleep(3)

        print(
            "After that day, you finished out the rest of your senior year and graduated from college. You left Portland for good and went onto become a professional seat filler."
        )
        time.sleep(3)

        print("You never stepped foot into another cabin again.")
        time.sleep(3)

        print(
            "After that day, your friend dropped out of college. They wound up moving to Los Angeles and went on to become a writer. "
        )
        time.sleep(3)
        print(
            "They publish a novel about their experience and it was turned into a motion picture starring Nicolas Cage."
        )
        time.sleep(3)
        print("Unfortunately, the ratings were bad. You never saw it. ")
        time.sleep(3)

        guesses_remaining = 0
    elif guesses_remaining == 0:
        print(
            "\nYou are out of tries! The winning number was:",
            winning_number,
            "\n\nBetter luck next time!",
        )
        time.sleep(2)

        print(
            "Ross smiles and vanished into thin air. Suddenly a door appears in front of you and you walked through it."
        )
        time.sleep(3)

        print(
            "You were immediately transported back to the inside of your car, with your friend driving and you in the passenger seat. You wrapped your arms around them tightly, hugging them and saying, 'Im so glad you're safe'."
        )
        time.sleep(4)

        print(
            "'What are you talking about? We've been driving through this abandoned forest this whole....'"
        )
        time.sleep(2)

        print("BOOM!")
        time.sleep(2)

        print(
            "Suddenly your friend hits a pothole and the car lurches forward. Your friend's glasses go flying out the window."
        )
        time.sleep(3)

        print(
            "'This happened already...,' you say to yourself as you watch them go retrieve their glasses."
        )
        time.sleep(3)

        print(
            "Suddenly, someone grabs you from behind and you're tossed into a bag. You faintly hear your friend yell after you."
        )
        time.sleep(3)

        print(
            "You scratch at the bag and you make a small hole to see outside. You look out and see Ross smiling at you. 'I did say better luck next time....'"
        )
        time.sleep(3)

        print("EPILOGUE")
        time.sleep(3)

        print(
            "To your horror, you realized you were stuck in a never ending loop, bound to repeat this cycle over and over again."
        )
        time.sleep(2)

        print(
            "As time went on, you never made it out and eventually became part of the game."
        )
        time.sleep(2)

        print("Till this day, you have no idea where your friend is...")
        time.sleep(2)

    elif guesses_remaining == 1:
        playsound("esc_assets/music/Rossfatal.mp3")
        print(
            "\nSorry, that is not the correct number. Try again! You have one try remaining."
        )
    else:
        playsound("esc_assets/music/Rossfatal.mp3")
        print(
            "\nSorry, that is not the correct number. Try again! You have {} tries remaining.".format(
                guesses_remaining
            )
        )
