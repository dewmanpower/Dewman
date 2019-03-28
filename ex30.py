
"https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html"

from random import randint
x = []
with open('sowpods.txt', 'r') as f:
  line = f.readline().strip()
  while line:
    x.append(line)
    line = f.readline().strip()
print("The entire file as been read!")

count = len(x)
y = randint(0,count-1)
print("The random word is "+x[y])


