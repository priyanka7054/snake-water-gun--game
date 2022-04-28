# SNAKE-WATER-GUN GAme

import random

def gameWin(comp, me):
    if comp==me :
        return None    
    elif comp=='s':
        if me=='w':
            return False
        elif me=='g':
                return True
    elif comp=='w':
        if me=='g':
            return False
        elif me=='s':
                return True
    elif comp=='g':
        if me=='s':
            return False
        elif me=='w':
                return True

    
print("comp turn : snake(s) water(w) or gun(g)?")
randomNo = random.randint(1,3)
print(randomNo)
if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w' 
elif randomNo == 3:
    comp = 'g'       

me = input("my turn : snake(s) water(w) or gun(g)?")

print(f"computer chose {comp}")
print(f"you chose {me}")

a = gameWin(comp,me)
if a ==None:
    print("the game is a tie!")
elif a:
    print("You win!") 
else:
    print("You Lose!")       
