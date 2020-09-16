name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age <= 31:
    print("You can go on a holiday, {0}!".format(name))
else:
    print("Sorry you cannot go on a holiday!".format(name))

print("*" * 80)

if age < 18 or age > 31:
    print("Sorry you cannot go on a holiday, {0}!".format(name))
else:
    print("You can go on a holiday, {0}!".format(name))