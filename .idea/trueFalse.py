if 0:
    print("True")
else:
    print("false")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you a person with no name?")
