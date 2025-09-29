from random import randrange

'''
Generate a random number from a range of 0 to 10
To adjust the range edit the values within the parentheses ()
The first number controls the lower bounds and the second controls the higher bounds
'''

("Yo yo yo, welcome to the Number Guessing Game!")
print("You must guess the random number between 0 and 100. If you guess correctly within 10 tries you win!")

while True :
    random_number = randrange(0, 100)
    attempts = 0
    max_attempts = 10
    success = False
    while attempts < max_attempts:
        attempts += 1
        guess = int(input("Guess the random number between 0 and 100: "))
        if guess == random_number:
            print(f"Congratulations! You guessed the number {random_number} correctly.")
            print(f"It took you {attempts} tries.")
            success = True
            break
        else:
            if attempts < max_attempts:
                
                if guess > random_number:
                    print("Incorrect guess. Too high! Try again.")
                else:
                    print("Incorrect guess. Too low! Try again.")
            else:
                print(f"No more attempts. The correct number was {random_number}. You lose!")
    while True:
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Pardon? Enter 'y' or 'n'.")

    if play_again == "n":
        print("Thanks for playing! Byeeee!")
        break

print("Completed by, Daniel Arterbury")