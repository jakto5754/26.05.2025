import random

def greet():
    x = input("What's your name? ")
    print("Greetings, ", x, "!", sep="")
    menu()

def menu():
    print("What would you like to do?\n1. Change username.\n2. Play a game.\n3. Exit.")
    while True:
        try:
            choice = int(input("Your choice is: "))
            if choice == 1:
                greet()
            elif choice == 2:
                guess()
            elif choice == 3:
                print("Goodbye and have a good day!")
                quit()
        except ValueError:
            print("Apologies, but i am unable to process your answer. Please try again.")

def guess():
    tries = 3
    numb = random.randint(1, 10)
    print("You have to guess a number in the range of 1 to 10. You have 3 tries. \nEach incorrect answer substracts 1 try. Guess incorrectly 3 times and you lose!")
    while True:
        try:
            guessing = int(input("Your guess is: "))
            if guessing == numb:
                print("Congratulations!")
                try_again()
            elif guessing >= numb:
                tries = tries - 1
                print("The hidden number is lesser!")
                print("You have:", tries, "tries left!")
            elif guessing <= numb:
                tries = tries - 1
                print("The hidden number is greater!")
                print("You have:", tries, "tries left!")
            if tries <= 0:
                print("Game over!")
                print("The correct number was:", numb)
                try_again()
        except ValueError:
            print("Apologies, but i am unable to process your answer. Please try again.")
            continue

def try_again():
    while True:
        print("Would you like to try again?")
        again = input("Y/N ")
        if again == "Y" or again == "y":
            guess()
        elif again == "N" or again == "n":
            menu()
        else:
            print("Apologies, but i am unable to process your answer. Please try again.")
            continue

greet()