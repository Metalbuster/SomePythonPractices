import random

#Target number
target = random.randint(1000,9999)
#Guess number
guess = 0
#Tries
count = 0

while(guess != target):
    #Guess number
    count = count + 1
    guess = int(input("Guess your 4 digits number: "))

    target_string = str(target)
    guess_string = str(guess)
    show_digit = ['X']*4

    for i in range(0, 4):
        if(guess_string[i] == target_string[i]):
            show_digit[i] = guess_string[i]
            
    print("Your progress: \n")
    for j in show_digit:
        print(j, end=' ')
    print("\n")

if(guess == target):
    print("You are correct! It takes %d tries to guess correctly!\n" % count)
    