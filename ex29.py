
"https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html"

a=[[0,0,0],
   [0,0,0],
   [0,0,0]]


    
def decided(a):
    sx = 0
    k = 0
    for i in range(0,3):
        ste=""
        for j in range(0,3):
            if a[i][j] == 0:
                sx+=1
            ste=ste+" "+str(a[i][j])
        print(ste)
    print(str(sx)+" square left")    
    for i in range(0,3):
        if a[i][0] == a[i][1] == a[i][2] == "x":
                k = 1
        elif a[0][i] == a[1][i] == a[2][i] == "x":
                k = 1
    if a[0][0] == a[1][1] == a[2][2] == "x":
        k = 1
    elif a[2][0] == a[1][1] == a[0][2] == "x":
        k = 1
    
    for i in range(0,3):
        if a[i][0] == a[i][1] == a[i][2] == "o":
                k = 2
        elif a[0][i] == a[1][i] == a[2][i] == "o":
                k = 2
    if a[0][0] == a[1][1] == a[2][2] == "o":
                k = 2         
    elif a[2][0] == a[1][1] == a[0][2] == "o":
                k = 2
    if k == 1:
        return 1
    elif k == 2:
        return 2
    elif sx == 0:
        return 0
    else:
        return 3

p1 = 0
p2 = 0
dw = 0

s=3
while s == 3:
    p = 3
    while p == 3:    
        x =str(input("Enter the coordinate for x:"))
        x = x.split(",")
        if a[int(x[0])-1][int(x[1])-1] == 0:
            a[int(x[0])-1][int(x[1])-1] = "x"
            p = 0
        else:
            print("Already place")
        s = decided(a)
        if s == 0:
            print("Draw")
            dw+=1
        elif s == 1 :
            print("P1 WIN")
            p1+=1

            
    if s == 3:
        q  = 3
        while q == 3:    
            x =str(input("Enter the coordinate for o:"))
            x = x.split(",")
            if a[int(x[0])-1][int(x[1])-1] == 0:
                a[int(x[0])-1][int(x[1])-1] = "o"
                q = 0
            else:
                print("Already place")
            s = decided(a)
            if s == 0:
                print("Draw")
                dw+=1
            elif s == 2:
                print("P2 WIN")
                p2+=1
    if s != 3:
        t=input("Want to play again Y/N: ")
        if t == "Y":
            s = 3
            a=[[0,0,0],
               [0,0,0],
               [0,0,0]]
        else:
            print("P1 WIN AT TOTAL OF "+str(p1)+" games")
            print("P2 WIN AT TOTAL OF "+str(p2)+" games")
            print("DRAW AT TOTAL OF "+str(dw)+" games")
            if p1 > p2:
                print("P1 WIN")
            elif p1 < p2:
                print("P2 WIN")
            else:
                print("DRAW")
        