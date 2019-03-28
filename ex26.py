
"https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html"

#a= input("List the outcome: ")

a = [[0, 2, 1],
	[2, 1, 0],
	[1, 2, 1]]
x = 0

for i in range(0,3):
    if a[i][0] == a[i][1] == a[i][2] == 1:
            x = 1
    elif a[0][i] == a[1][i] == a[2][i] == 1:
            x = 1
if a[0][0] == a[1][1] == a[2][2] == 1:
    x = 1
elif a[2][0] == a[1][1] == a[0][2] == 1:
    x = 1

for i in range(0,3):
    if a[i][0] == a[i][1] == a[i][2] == 2:
            x = 2
    elif a[0][i] == a[1][i] == a[2][i] == 2:
            x = 2
if a[0][0] == a[1][1] == a[2][2] == 2:
            x = 2         
elif a[2][0] == a[1][1] == a[0][2] == 2:
            x = 2
             
            
if x == 1:
    print("P1 win")
elif x == 2:
    print("P2 win")
else:
    print("Draw")
    