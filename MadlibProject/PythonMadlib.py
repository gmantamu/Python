# Testing different ways to concatenate strings in Python
# How can we add on to an existing string? How can we print it?

# Different examples:
# print("Happy " + birthday!)
# print("Happy {}".format(birthday!))
# print(f"Happy {birthday!}")

Adj = input("Input an adjective: ")
Verb1 = input("Input a verb: ")
Verb2 = input("Input a second verb: ")
Person = input("Input a person: ")

finalMadlib = f"I truly learn to program because it is {Adj}. It is always a joy to learn new code, and whenever I code, my favorite past time is to {Verb1}. \
Second only to this, I also enjoy to {Verb2} while I code. My goal is to become like {Person}, so I can be very succesfull"

print(finalMadlib)