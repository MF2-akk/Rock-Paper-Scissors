import random

objects = ["paper", "rock", "scissors"]

def second_player() -> str:
    randomIndex = random.randint(0, 2)
    return objects[randomIndex]


while True:
    try:
        char = int(input("please, type 0(paper), 1(rock) or 2(scissors"))
        if 0 <= char <= 2:
            break
        else:
            print("Invalid input. Please, enter 0, 1, or 2")
    except ValueError:
        print("Invalid input. Please enter a number")

#-1 is lose, 0 is draw and 1 is win
def rules(a, b) -> int:
    if a == b:
        return 0
    if (a == "paper" and b == "rock") or \
       (a == "rock" and b == "scissors") or \
       (a == "scissors" and b == "paper"):
           return 1
    else:
        return -1

rival_choice = second_player()

gameResult = rules(objects[char], rival_choice)

print("Your rival chose is " + rival_choice)

if gameResult == 1:
    print("you're win")
if gameResult == 0:
    print("draw")
if gameResult == -1:
    print("you're lose")
    
