'''
File: wordle_game.py
Author: Jason L'Italien

Imitates wordle game (non GUI), starts by choosing random word from wordle
answer list, this will be the answer the user looks for. Asks user for input being
their first guess, returns with either:
    1. Correct guess, game ends
    2. Incorrect guess, tells user which letters are in correct position
    and which letters are not in correct position but are in word if applicable
    3. Same as 2 but ends game after 6 guesses.

Progress 1: Created text-based wordle game:
        - Game generates random answer from list of all possible wordle answers
            (source: https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b)
        - Game allows you up to 6 guesses of words that appear in the list
            of allowed guesses (source: https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c)
        - Upon each guess, first determines which letters are in the word but not in the correct position,
            Then determines which letters are in the correct position
        - Letters that are in the word but not in the correct position are noted with a "@"
        - Letters that are in the correct position are displayed as they appear in the word, e.g.
            if the answer is: "hello"
            and the guess is: "helos"
            The game displays: ['h', 'e', 'l', '@', '#']
            Hashtag signifies that your guess at that letter is not in the correct position
            and also does not exist in the word (s is not in the correct position for the answer "hello"
            and also does not exist in the word).

Progress 2 goals:
        - Use text based wordle game as starting point for coding
            wordle solver
        - 
'''

import random

class Game:

    def __init__(self, answers_file, guesses_file):
        # guess number starts at 1 (max 6 guesses allowed)
        self._guess_num = 1
        # open text file containing list of possible answers
        answers = open(answers_file)
        # open text file containing list of possible guesses
        guesses = open(guesses_file)
        # store possible answers into list
        self._answer_list = self.read_file(answers)
        # store possible guesses into list
        self._guess_list = self.read_file(guesses)
        # variable for storing state of guess(es)
        self._state = []
        # list of guesses doesn't include possible answers for some reason (e.g. hello
        # is a possible answer but doesn't exist in the guess list), append all these
        for answer in self._answer_list:
            self._guess_list.append(answer)

        # choose random answer
        self._answer = self._answer_list[random.randint(0, len(self._answer_list)-1)]
        print(self._answer)

    def read_file(self, words_file):
        words_list = []
        for word in words_file:
            words_list.append(word.strip("\n"))
        return words_list

    def guess(self, guess):
        if (guess not in self._guess_list):
            print("Guess not allowed, try again")
            return
        if (guess == self._answer):
            return True
        else:
            retList = [x for x in "....."]
            # determine which letters are in word but not correct position
            for i in range(len(self._answer)):
                if (guess[i] != self._answer[i] and guess[i] in self._answer):
                    retList[i] = "@"
            # determine which letters are in correct position
            for i in range(len(self._answer)):
                if (guess[i] == self._answer[i]):
                    retList[i] = guess[i]
            self._guess_num+=1
            self._state = retList

    def canGuess(self):
        return self._guess_num <= 6

    def get_guess_num(self):
        return self._guess_num

    def get_answer(self):
        return self._answer

    def get_state(self):
        return self._state
    
    def get_possible_answers(self):
        return self._answer_list