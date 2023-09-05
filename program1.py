import random
x = input("pick a number between 1 & 100: ")
y = random.randint(1,100)
print("you picked " + x + " and the number " + str(y) + " was generated")
print(f"you picked {x} and the number generated was {y}".format(x,y))
if int(x) < y:
    print("TOO LOW!")
if int(x) > y:
    print("TOO HIGH!")
if int(x) == y:
    print("CORRECT! slay.")     # random_number
