

def slitword(x):
    slit= x.split(" ")
    lit=[]
    rlit=[]
    for i in slit:
        lit.append(i)
    for i in range(0,len(lit)):
        rlit.append(lit[len(lit)-i-1])
    print(" ".join(rlit))   
        
