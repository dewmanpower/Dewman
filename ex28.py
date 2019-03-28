
"https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html"

def findmax(a,b,c):
    x = a
    if b > x:
        x = b
    if c > x:
        x = c
    print(x)
