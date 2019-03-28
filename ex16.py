import random
def ranpass(a,b):
    number=[]
    for i in range(0,10):
        number.append(str(i))
    letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letter3=["!","@","#","$","%","^","&","*"]
    passx=[]
    if b == "H":
        for i in range(0,a):    
            x=random.randint(0,3)
            if x == 0:
                y=random.randint(0,10-1)
                passx.append(number[y])
            if x == 1:
                y=random.randint(0,len(letter)-1)
                passx.append(letter[y])
            if x == 2:
                y=random.randint(0,len(letter2)-1)
                passx.append(letter2[y])
            if x == 3:
                y=random.randint(0,len(letter3)-1)
                passx.append(letter3[y])
    if b == "L":
        for i in range(0,a):    
            x=random.randint(0,1)
            if x == 0:
                y=random.randint(0,10-1)
                passx.append(number[y])
            if x == 1:
                y=random.randint(0,len(letter)-1)
                passx.append(letter[y])       
    print("".join(passx))