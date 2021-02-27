import random

print ("Number guessing game")

number = random.randint(1, 20)

chances = 0

print("Guess a number between 1 and 20")

while(chances < 5):
    guess = int(input())

    if (guess == number):
        print("Congratulations you won!!!")
        break
    elif guess < number:
        print("Your guess is low and kindly select a higuer number", guess)
    else:
        print("Your guess is high and kindly select a lower number", guess)

    chances = chances + 1
else:
    if not chances < 5:
        print("You lose!! The number is", number)