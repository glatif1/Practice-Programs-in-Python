import random

actualguessesTaken = 0
print("This is the number guessing game!!!")


number = random.randint(1, 20)
print(' the number is between 1 and 20.')
continuegame='y'
while actualguessesTaken < 6:
    while continuegame =='y':
        Playerguess = int(input("Enter your guess:"))
        actualguessesTaken = actualguessesTaken + 1
        if Playerguess < number:
            print('Your guess is too low.')
        if Playerguess > number:
            print('Your guess is too high.')
        if Playerguess == number:
            print("That is correct! You got it in", actualguessesTaken,"guesses!")

            exit()
            continuegame = input("Would you like to continue?'y' or 'n':").lower()




if Playerguess != number:
    print('Too many guesses. The number was ', number)
    print("You took",actualguessesTaken,"guesses")