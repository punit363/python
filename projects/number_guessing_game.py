#Objective
#Give user instructions when the game begins
#ask them if they want to start the game (y/n)
#if n then end the loop
#if y then input to enter a number
#after each assumption
#reply with higher or lower
#save the input to a list and count the number of attempts
#when their guess is correct display the no of attemps, their choices and the final number

import random

is_the_guess_correct = False

def number_comparator(guess,number) :
    # global is_the_guess_correct // iteration-1
    if guess < number :
        return False, "Oops! your guess is too small, think of a bigger number. \n"
    elif guess > number :
        return False, "Oops! your guess is too big, think of a smaller number. \n"
    elif guess == number :
        # is_the_guess_correct = True // iteration-2
        return True, "Shabash! Your guess is correct."

def guess_the_number():
    no_of_attempt = 1
    number = random.randint(1,10)
    print("We have thought of a number.\n ")
    while True:
        try:
            guess = int(input("Guess what it is: \n"))
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Please enter a valid number. \n")

    is_the_guess_correct, comparision_result = number_comparator(guess,number)
    print(comparision_result)
    print(f"Total no of attemps : {no_of_attempt}") if is_the_guess_correct else None

    if not is_the_guess_correct :
        while True:
            no_of_attempt += 1
            guess = int(input("Try once more. what is it this time : "))
            is_the_guess_correct, comparision_result = number_comparator(guess,number)
            print(comparision_result)
            if is_the_guess_correct :
                print(f"Total no of attemps : {no_of_attempt}")
                break    
    


print("""Welcome to the Number Guessing Game!
      
Here are the Rules:
      
when you start the game the system assumes a number, you are given a chance to guess what that number is.
The system compares that guess to the original number and tells wheather your number is greater or lesser than the orignal number, giving another chance to guess the number.
This keeps on repeating till you have identified the number. You objective is to identify the number in the least possible time \n""")

start_game = input("Would you like to start the game? (y/n) : ")

guess_the_number() if start_game.lower() == "y" else print("Thankyou!")