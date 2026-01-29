import random
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Take a guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"You got it! The number was {number}.")
        break
