
"https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html"

a = int(input("Number of rows: "))
b = int(input("Number of columns: "))


for i in range(0,a):
    x=" ---"
    y="|   "
    v=" ---"
    w="|   "
    for j in range(0,b-1):
        v=v+x
    for k in range(0,b):
        w=w+y
    print(v)
    print(w)
print(v)
