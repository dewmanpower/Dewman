
"https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html"
import random
a = random.randint(2, 6)


z = 0 
while z != -1:
    x = input("Guess the number/exit: ")
    if x == "exit":
        print("End ")
        break
    else:
        x = int(x)
        if x > a:
            print("Too high")
            z += 1
        elif x < a:
            print("Too low")
            z += 1
        elif x == a:
            print("Your right at the " + str(z) +" guess")
            z += 1