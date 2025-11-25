import random 
import pygame
from inputimeout import inputimeout, TimeoutOccurred
import os

pygame.mixer.init()

def play_sound(file):
    if os.path.exists(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    else:
        print(f"❗Sound file not found: {file}")

emoji_dict = {
    "😂": "laughing",
    "😢": "crying",
    "🔥": "fire",
    "❤️": "love",
    "👍": "thumbs up",
    "😎": "cool",
    "🤖": "robot",
    "🎉": "celebration",
    "🥺": "puppy eyes",
    "💩": "poop"
}

print("🎮 Welcome to 'Guess the Emoji' Game!")
print("Type exit to exit anytime!!\n")

score = 0
emoji, meaning = random.choice(list(emoji_dict.items()))
wrong_attempts = 0

while True:
    print(f"Emoji: {emoji}")

    try:
        guess = inputimeout(prompt = "What does this Emoji mean?: ", timeout = 7).strip().lower()

        if guess == meaning:
            print(f"🎉 You guessed it right!! 🙌")
            print("🌟🌟🌟🌟🌟🌟🌟\n")
            score += 1
            wrong_attempts = 0
            play_sound("audio/win.wav")
            emoji, meaning = random.choice(list(emoji_dict.items()))

        elif guess == "exit":
            print(f"Thanks for playing!! Score: {score}")
            play_sound("audio/exit.wav")
            break 
        else:
            wrong_attempts += 1
            play_sound("audio/lose.wav")

            if wrong_attempts >= 5:
                print(f"\n❌ 5 wrong tries! The correct answer was: '{meaning}' 😅\n")
                emoji, meaning = random.choice(list(emoji_dict.items()))
                wrong_attempts = 0

            else:
                hint_meaning = random.randint(1,len(meaning)-1)
                print(f"❗Wrong guess!! Hint: {meaning[:hint_meaning]}\n")

    except TimeoutOccurred:
        print(f"\n⌛Too Slow! The Correct answer was {meaning}")
        emoji, meaning = random.choice(list(emoji_dict.items()))



# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Aaban-Khan/emoji-guessing-game.git
# git push -u origin main