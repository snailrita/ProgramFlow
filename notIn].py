activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go the cinema")
print(activity.capitalize())
print(activity.center(40, '*'))

