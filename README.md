# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Table of contents:
- [Installation requirements](#installation-requirements)
- [How to run the game](#how-to-run-the-game)
- [How to play](#how-to-play)
- [File structure](#file-structure)
- [License information](#license-information)

## Installation requirements

The only requirement is a verson of Python (preferably Python 3) being installed on your computer.

## How to run the game

To run a demo of the game, enter the following line in a terminal

> python hangman

if you're in the same directory as the README.md file, or

> python milestone5.py

if you're inside the lowest hangman directory.

Alternatively, use a python compiler/interpreter to run milestone.py for you.

## How to play

The game first generates a random word. Then it keeps asking you for a single letter as an input.

Every right guess you make, i.e. the letter you guessed is in the word, you unlock that letter in the guessed word. Otherwise you lose a life.

You win the game when once you unlock all the letters in the guessed word. If your life drops to 0, you lose.

Have fun!

## File structure

```bash
.
├── hangman
│   ├── __main__.py     # __main__.py allows to run directory
│   ├── __pycache__
│   ├── milestone.py    # 1st version of code
│   ├── milestone2.py   # 2nd version of code
│   ├── milestone3.py   # 3rd version of code
│   ├── milestone4.py   # 4th version of code, has playable loop.
│   └── milestone5.py   # 5th version of code, final version.
└── README.md

```

## License Information

TBD