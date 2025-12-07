from random import randint
print("Welcome to the Number Guessing Game")
print("Im goint to think of a number between 1 and 100 and you havet to guess it in a given number of chances.")
print("Choose your difficulty:")
print("1. easy: 20 chances")
print("2. medium: 10 chances")
print("3. hard: 5 chances")
diff = input("Enter your choice: ")
if diff == "1":
    print("You have selected the easy difficulty.")
    print("Let's start the game")
    rand_num = randint(1, 100)
    chances = 0
    guess = int(input("Enter your guess: "))
    chances += 1
    while chances != 20:
        if guess < rand_num:
                chances += 1
                print("Incorrect! The number is greater than", guess)
                guess = int(input("Enter your guess: "))
        elif guess > rand_num:
                chances += 1
                print("Incorrect! The number is less than", guess)
                guess = int(input("Enter your guess: "))
        elif guess == rand_num:
                chances += 1
                print("Congratulations!, you got it in", chances - 1, "attempts")
                break
    if chances == 20:
        print("Sorry, you have run out of chances")
elif diff == "2":
    print("You have selected the medium difficulty.")
    print("Let's start the game")
    rand_num = randint(1, 100)
    chances = 0
    guess = int(input("Enter your guess: "))
    chances += 1
    while chances != 10:
        if guess < rand_num:
                chances += 1
                print("Incorrect! The number is greater than", guess)
                guess = int(input("Enter your guess: "))
        elif guess > rand_num:
                chances += 1
                print("Incorrect! The number is less than", guess)
                guess = int(input("Enter your guess: "))
        elif guess == rand_num:
                chances += 1
                print("Congratulations!, you got it in", chances - 1, "attempts")
                break
    if chances == 10:
        print("Sorry, you have run out of chances.")
elif diff == "3":
    print("You have selected the hard difficulty.")
    print("Let's start the game")
    rand_num = randint(1, 100)
    chances = 0
    guess = int(input("Enter your guess: "))
    chances += 1
    while chances != 5:
        if guess < rand_num:
                chances += 1
                print("Incorrect! The number is greater than", guess)
                guess = int(input("Enter your guess: "))
        elif guess > rand_num:
                chances += 1
                print("Incorrect! The number is less than", guess)
                guess = int(input("Enter your guess: "))
        elif guess == rand_num:
                chances += 1
                print("Congratulations!, you got it in", chances - 1, "attempts")
                break
    if chances == 5:
        print("Sorry, you have run out of chances.")
        
                
    

