import random

keep_going = True
guesses = 3



while keep_going:
    number = random.randint(1,5)
    guess = int(input("Pick a number between 1 and 5"))
    if guess == number:
        print ("Good job you guessed it!")
        keep_going = False
    else:
        print("It is not" , guess ,"it is", number)
        guesses = guesses - 1
        if guesses == 0:
            keep_going = False
        else:
            print("Only", guesses,"more guesses")
