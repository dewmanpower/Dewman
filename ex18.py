
"https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html"

from random import randint
c=[]
h=[]
for i in range(0,4):
            h.append(randint(0,9))
while len(c) != 4:
    a = input("Enter the number: ")
    if a == "exit" :
        break
    else:
        y=int(a)
        
        c=[]
        d=[]
        g=0
        g2 = 3
        while  int(y) > 0:
            g=g+1
            j = y%10
            y = y/10
            y=int(y)
            if j== h[g2]:    
                c.append(j)
            elif j in h and j!=h[g2]:
                d.append(j)
            g2 = g2-1

        print("cow is: "+str(len(c)))
        print("bull is: "+str(len(d)))
        print(h)

