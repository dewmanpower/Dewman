
"https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html"

def fibonacci(seq):
    x = 1
    y = []
    for i in range(1,seq+1):
        if i < 2 and i > 0 :
            x = 1
            
        elif i == 2:
            x = 1
        else:
            x = y[len(y)-1]+y[len(y)-2]
        y.append(x)     
    return "The sequence of "+str(seq)+" will get the fibonacci of "+str(y[len(y)-1])
         
def fibonacci2(seq):
    x = 1
    y = 2
    c = 1
    for i in range(1,seq+1):
        if i < 2 and i > 0 :
            x = 1
            
        elif i == 2:
            x = 1
        else:
            y = x
            x = x+c
            c = y
            
    return "The sequence of "+str(seq)+" will get the fibonacci of "+str(x)           