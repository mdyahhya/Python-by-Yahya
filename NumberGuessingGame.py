import random
number = 20
for i in range(0,3):
    user = int(input("Guess the number :"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right, it's {number}")
        break
    elif user>number:
        print("Your Guess is too high")
    elif user<number:
        print("Your Guess is too low")
    else:
        print(f"Nice Try!, but the number is {number}")
