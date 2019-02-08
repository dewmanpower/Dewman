"https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html"
word = str(input("Put word:"))
a = []
b = []
for i in word:
    a.append(i)
count = len(word)-1

for j in word:
    b.append(word[count])
    count -= 1
if a == b:
    print("The word is palindrome:")
else:
    print("The word is not palindrome:")

