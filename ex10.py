
"https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html"
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


cx = []

for i in range(0,len(a)):
    if a[i] not in cx :
        cx.append(a[i])
for i in range(0,len(b)):
    if b[i] not in cx :
            cx.append(b[i])

x = sorted(cx)
print(x)