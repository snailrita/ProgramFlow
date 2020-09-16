answer = 5

print("Please guess number between 1 and 10")
guess = int(input())

if guess != answer:
    print("This is not the answer, try again!")
    guess = int(input())
    if guess == answer:
        print("You guessed it right!")
    elif guess < answer:
        print("Your answer is too low")
    else:
        print("Your answer too high")
else:
    print("You guessed from the first time!")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# else:
#     print("You got it first time")

