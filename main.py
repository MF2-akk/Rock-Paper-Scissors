import random

objects = ["paper", "rock", "scissors"]

def SecondPlayer():
    randomIndex = random.randint(0, 2)
    return objects[randomIndex]

print("please, type 0(paper), 1(rock) or 2(scissors)")
char =int(input())


#-1 is lose, 0 is draw and 1 is win
def Rules(a, b):
    if a == objects[0] and b == objects[1]:
        return 1
    if a == objects[0] and b == objects[2]:
        return -1
    if a == objects[0] and b == objects[0]:
        return 0
    if a == objects[1] and b == objects[0]:
        return -1
    if a == objects[1] and b == objects[2]:
        return 1
    if a == objects[1] and b ==  objects[1]:
        return 0
    if a == objects[2] and b == objects[0]:
        return 1
    if a == objects[2] and b == objects[1]:
        return -1
    if a == objects[2] and b == objects[2]:
        return 0

gameResult = Rules(objects[char], SecondPlayer())

if gameResult == 1:
    print("you're win")
if gameResult == 0:
    print("draw")
if gameResult == -1:
    print("you're lose")
    
