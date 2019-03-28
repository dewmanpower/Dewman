
"https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html"

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
while gridcount != 0:
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
    print(line+"\n")
    
        
        
    
        
