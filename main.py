from data import HANGMANPICS, words
import random

rand_word = random.choice(words)
rand_word_list = [data for data in rand_word]
guess_list = ['_' for data in rand_word_list]
print('WELCOME TO HANGMAN')
save = 0
LIVE = len(HANGMANPICS) - 1
user_word = []

game = True
while game:
    guess = input('guess the word: ')
    if guess not in user_word:
        user_word.append(guess)
    elif guess in user_word:
        print('you have answered that before')
        continue
    for data in range(len(rand_word_list)):
        if guess == rand_word_list[data]:
            guess_list[data] = guess
    if guess not in rand_word_list:
        save += 1
        LIVE -= 1
    if "_" not in guess_list:
        print('you win!')
        game = False
    print(HANGMANPICS[save])
    print(f'your life is {LIVE} left')
    print(guess_list)
    if save == 6:
        print("you lose")
        print(f'Random word is {rand_word}')
        game = False
