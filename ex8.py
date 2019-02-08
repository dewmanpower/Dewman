
"https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html"

x = 0
while x == 0:
    p1 = str(input("Type1: "))
    p2 = str(input("Type2: "))
    if p1 == p2:
        print("draw")
    elif p1 == "scissor" :
        if p2 == "papper" :
            print("p1 win")
        else:
            print("p2 win")
    elif p1 == "papper" :
        if p2 == "hammer" :
            print("p1 win")
        else:
            print("p2 win")
    elif p1 == "hammer" :
        if p2 == "scissor" :
            print("p1 win")
        else:
            print("p2 win")
    else:
        print("Try again")
    t = str(input("Con? Y/N:"))
    if t == "Y":
        x = 0
    else:
        x = 1
        print("Thankyou for playing")