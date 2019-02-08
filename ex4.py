"https://www.practicepython.org/exercise/2014/02/26/04-divisors.html"
x = int(input("Input the number: "))
print("The divisor is ")
y = range(2,x+1)
z=[]
for i in y:
    if x%i ==0:
        z.append(i)
print(str(z))
        