
"https://www.practicepython.org/exercise/2017/01/10/32-hangman.html"


word = input("The word that want to use :")
wordl = []

for i in word:
    wordl.append(i)
line =""
gridline ="_"
gridlineset = []
linecount = 0
wordcount = 0
for i in word:
    line+="_ "
    gridline+="_"
    gridlineset.append("_")
    wordcount+=0
print("Welcome to Hangman")
print(line+"\n")
wordcount = len(wordl)
gridcount = len(gridlineset)
timeleft = 6

while timeleft != 0:
    gridcount = 0
    line=""
    guess = input("Input the letter :")
    if guess not in wordl:
        print("Incorrect")
    for i in range(0,wordcount):
        if guess == wordl[i]:
            gridlineset[i] = guess

    for i in range(0,wordcount):
        line =line+gridlineset[i]+" "
        if gridlineset[i] == "_":
            gridcount+=1
    
    timeleft -= 1    
    print(line+"\n")
    print(str(timeleft)+" guesses left")
    if timeleft == 4:
        print("_")        
        print("_l_")
    if gridcount == 0:
        timeleft = 0
        print("You win")
    if timeleft == 0:
        if gridcount != 0:
            print("The correct word is "+word)
            print("You lose")
            
        ask = input("Do you want to play again ?: Y/N ")
        if ask == "Y":
            timeleft = 6
            