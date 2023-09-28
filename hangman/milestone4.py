import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list) # random word from the list, this is the word to be guessed.
        self.word_guessed = ["_"]*len(self.word) # list of the letters of the word, with ) for each letter not yet guessed.
        self.num_letters = len(set(self.word)) # number of unique letters in the word that have not yet been guessed.
        self.list_of_guesses = [] # list of the guesses that have already been tried.

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i in range(0,len(self.word_guessed)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
            print(f"Guessed word: {self.word_guessed}")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            
            if self.num_letters == 0:
                print(f"Congratulations, you won. The correct word was {self.word}")
                break
            elif self.num_lives == 0:
                print(f"You lost. The correct word was \"{self.word}\".")
