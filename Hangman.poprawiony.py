import random
import sys
import time


def start_game():
    print("It's time to play Hangman game!")
    while True:
        choice = input("Would you like to? Type yes or no.\n")
        if choice.lower() == "yes":
            break
        elif choice.lower() == "no":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("You can only type yes or no")


def guessing(name):
    f = open('countries_and_capitals.txt').readlines()
  
    chances = 5
    alphabet = "abcdefghijklmnoprstquwxyzABCDEFGHIJKLMNEOPRSTUQWXYZ"
    not_in_word = []
    word = random.choice(f)
    country_capital = word.split("|")
    capital = country_capital[1]
    secret_word = capital.replace("\n", "").replace(" ", "")
    secret_word = secret_word.upper()
    guessed_word = []

    for character in secret_word:
        guessed_word.append("-")

    start = time.time()
    while chances > 0:
        word_or_letter = input("Would you like to guess letter or whole word?\n")
        len_word = len(secret_word)
        if word_or_letter.lower() == "word":
            print(guessed_word)
            guess = input("Whats your guess? Wrong answer means -2 life points! \n ")
            if guess.upper() == secret_word:
                    print("Congratulations.You re correct")
                    stop = time.time()
                    t = stop - start
                    print("Your time is: ", round(t, 2))
                    save(name, t)
            else:
                print("You are wrong")
                chances -= 2
                if chances == 0:
                    print("You have no chances left.You lost ")
                if chances == 1:
                    print("You cant guess whole word because you have only 1 life point left.")
                else:
                    print("You have ", chances, "chances left")
                continue

        elif word_or_letter.lower() == "letter":
            print("Already used letters", not_in_word)
            print(guessed_word)
            guess = input("Whats your guess? \n ")
            if guess not in alphabet:
                print("You wrote wrong letter")
            elif guess in not_in_word:
                print("You already used this letter.")
                print("Already used letters", not_in_word)
            if guess.upper() not in secret_word:
                    chances -= 1
                    print("You lost 1 chance")
                    not_in_word.append(guess)
                    if chances > 1:
                        print("You have ", chances, "chances left")
                    elif chances == 1:
                        print("You have ", chances, "last chance")
            elif guess.upper() in secret_word:
                    print("You are correct")
                    not_in_word.append(guess)

        else:
            print("You can only type letter or word")
            continue

        for j in range(0, len_word):
                    if secret_word[j] == guess.upper():
                        guessed_word[j] = guess.upper()
                        print(guessed_word)
        if "-" not in guessed_word:
            print("You won!")
            stop = time.time()
            t = stop - start
            print("Your time is: ", round(t, 2))
            save(name, t)
            break
        if chances == 0:
            print("You lost")
            stop = time.time()
            t = stop - start
            print("Your time is: ", round(t, 2))
            save(name, t)
            break


def once_more():
    play = input("Would you like to play once more? \n")
    if play.lower() == "yes":
        main()
    elif play.lower() == "no":
        print("Good bye")
    sys.exit(0)


def save(name, t):
    score_board = open('highscores.txt', 'a')
    score_board.write("\n" + name + ":" + str(round(t, 3)))
    score_board.close()
    once_more()


def main():

        name = input("What's your name?\n")
        print("Welcome", name)
        start_game()
        print("You need to found capital of one European country.You can type only letters a-z")
        guessing(name)


if __name__ == "__main__":
    main()



