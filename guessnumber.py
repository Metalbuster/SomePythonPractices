import random
import math
#Input Upper bound
upper = int(input("Please input upper bound number: "))
#Input Lower bound
lower = int(input("Please input lower bound number: "))

target = random.randint(lower, upper)
guess = round(math.log(upper - lower + 1, 2))
print("You have %d rounds to guess the number!\n" % guess)

count = 0

while(count < guess):
    guess_input = int(input("Guess the number : "))
    
    if(guess_input == target):
        print("Correct!\n")
        break
    elif(guess_input < target):
        print("Too low!\n")
    elif(guess_input > target):
        print("Too high!\n")

    count = count + 1

if(count == guess):
    print("You lose!\n")
    print("The number is %d" % target)
else:
    print("You win!")
