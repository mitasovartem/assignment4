import random

def generate_secret_word(word_list):
    return random.choice(word_list)

def guesses_check(secret, guess):
    if len(guess) != len(secret):
        return []
    result = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            result.append("correct")
        elif guess[i] in secret:
            result.append("present")
        else:
            result.append("absent")
    return result

def display_number(guess, result):
    display = []
    for i in range(len(guess)):
        letter = guess[i]
        status = result[i]
        display.append(f"{letter} - {status}")
    return "\n".join(display)

def play_game(word_list, max_tries = 6):
    secret_word = generate_secret_word(word_list)
    word_length = len(secret_word)
    tries_left = max_tries

    print("Welcome to Wordle!")
    print(f"Guess the {word_length}-letter word. You have {tries_left} tries.")

    while tries_left > 0:
        guess = input(f"Attempt {max_tries - tries_left + 1}/{max_tries} – Enter guess: ").lower()
        if len(guess) != word_length:
            print(f"Wrong length, it is expected to be {word_length} letters.")
            continue

        if guess == secret_word:
            print("You win!")
            return

        result = guesses_check(secret_word, guess)
        print("Result:", display_number(guess, result))
        tries_left -= 1

    print(f"You lose! The word was: {secret_word}") 

def game_loop():
    words = ['apple',    'bread','candy',    'dream','eagle','flame','grape','house','input','joker']
    while True:
        play_game(words)
        loop = input("Want to play again? Type 'yes' or 'no': ").lower()
        if loop != 'yes':
            print("Goodbye and thank you for playing!")
            break

game_loop()