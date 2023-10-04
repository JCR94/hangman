import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self,word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    '''
    Evaluates a player's guess by checking if a letter is in the word.
    If the letter is in the word, the letter will be revealed in the guessed word (stored inside self.word_guessed).
    If the letter is not in the word, the player loses one life.
    If the letter has been tried already, the game asks for a new guess.

    Parameters
    ----------
    guess : str
        A string representing a single letter.   
    '''
    def check_guess(self, guess):
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

    '''
    Asks the player for a single letter as an input.
    If the input is invalid, the method will print a corresponding message and ask the player for a new input.
    Once a valid input has been entered, check_guess is called with the input as parameter.
    '''
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                break
        self.check_guess(guess)
        self.list_of_guesses.append(guess.lower())

    '''
    Starts a game of hangman with a given list of possible words, and a default number of 5 lives.
    Parameters
    ----------
    word_list : list
        A list of possible words (strings) from which to guess.
    num_lives : int
        The number of lives the player has, i.e. false guesses required to lose the game. (default is 5)
    '''
    @classmethod
    def play_game(cls,word_list, num_lives = 5):
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break


if __name__ == "__main__":
    myList = ["banana", "lime", "lemon", "orange", "mandarin"]
    Hangman.play_game(myList)