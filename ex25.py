
"https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html"

from random import randint
x= ""
a=0
b=100
z=1
while x != "correct":
    y=randint(a,b)
    print(y)
    x = input("Answer: ")
    if x == "Too high":
        b = y+1
    elif x == "Too low":
        a = y-1
    elif x == "correct":
        print("Number of attempt: "+ str(z))
    elif x == "close":
        print("Number of attempt: "+ str(z))       
        break
    else:
        print("wrong input")
        z=z-1
    z=z+1