import wordle_game
import re

def main():
    x = re.search("he.lo", "hello")
    print(x)
    game = wordle_game.Game("words.txt", "guess_words.txt")
    won = False
    state = []
    while (game.canGuess()):
        guess = input("Guess #" + str(game.get_guess_num()) + ": ")
        won = game.guess(guess)
        if (won):
            print("You win after " + str(game.get_guess_num()) + " guesses!")
            break
        print("".join(game.get_state()))
        state = "".join(game.get_state())
        choices = []
        for answer in game.get_possible_answers():
            if (re.search(state, answer) is not None and answer != guess):
                choices.append(answer)
        
        print(choices)


    if (not won):
        print("Max guesses reached, the answer was: " + game.get_answer() + "!")

if __name__ == '__main__':
    main()