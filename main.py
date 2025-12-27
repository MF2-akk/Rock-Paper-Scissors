import random

objects = ["paper", "rock", "scissors"]

def second_player() -> str:
    randomIndex = random.randint(0, 2)
    return objects[randomIndex]

char =int(input("please, type 0(paper), 1(rock) or 2(scissors)"))

if char > 2 or char < 0:
   print("please, try again")
   char = int(input("please, type 0(paper), 1(rock) pr 2(scissors)"))
   if char >2 or char < 0:
              quit()

#-1 is lose, 0 is draw and 1 is win
def rules(a, b) -> int:
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

gameResult = rules(objects[char], second_player())
if gameResult == 1:
    print("you're win")
if gameResult == 0:
    print("draw")
if gameResult == -1:
    print("you're lose")
    
