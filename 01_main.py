import random 
import pygame

def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

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

while True:
    print(f"Emoji: {emoji}")
    guess = input(f"What does this Emoji mean?: ").strip().lower()

    if guess == meaning:
        print(f"🎉 You guessed it right!! 🙌")
        print("🌟🌟🌟🌟🌟🌟🌟\n")
        score += 1
        play_sound("audio/win.wav")
        emoji, meaning = random.choice(list(emoji_dict.items()))

    elif guess == "exit":
        print(f"Thanks for playing!! Score: {score}")
        play_sound("audio/tie.wav")
        break 
    else:
        hint_meaning = random.randint(1,len(meaning)-1)
        print(f"❗Wrong guess!! Hint: {meaning[:hint_meaning]}\n")
        play_sound("audio/lose.wav")
