"https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html"

def prime(number="Input the number: "):
    setnum = []
    for i in range(1,number+1):
        if number%i == 0:
            setnum.append(i)
    if len(setnum)==2:
        return("The number is prime")
    else:
        return("The number is not prime")
    