
"https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html"

a=[[0,0,0],
   [0,0,0],
   [0,0,0]]


    
def decided(a):
    sx = 0
    for i in range(0,3):
        ste=""
        for j in range(0,3):
            if a[i][j] == 0:
                sx+=1
            ste=ste+" "+str(a[i][j])
        print(ste)
    print(str(sx)+" square left")    
    if sx == 0:
        return 0
    else:
        return 3
            
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

        