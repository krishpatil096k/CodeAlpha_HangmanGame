import random

code_alpha = ["apple", "brain", "cloud", "drive", "eagle"]
 
code_alpha = random.choice(code_alpha)
guessed = []
wrong_guesses = 0
max_wrong = 6

 
display = ["_" for _ in code_alpha]

print("🎯 Welcome to Hangman Game!")
print("Word to guess:", " ".join(display))

while wrong_guesses < max_wrong and "_" in display:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed:
        print("⏳ Already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in code_alpha:
        for i in range(len(code_alpha)):
            if code_alpha[i] == guess:
                display[i] = guess
        print("✅ Correct! ", " ".join(display))
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess. Attempts left: {max_wrong - wrong_guesses}")
        print(" ".join(display))

 
if "_" not in display:
    print("🎉 You win! The word was:", code_alpha)
else:
    print("💀 Game Over! The word was:", code_alpha)
