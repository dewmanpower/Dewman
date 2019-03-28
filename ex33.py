
"https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html"

birthday = {"Dew Man":"18/09/96","Dew Man2":"17/12/12"}
x = birthday.keys()
line = ""
for i in x:
    line = line+i+"\n"
print("We know birthdays of")
print(line)
    

tell = input("What  is the name that you want to know the birthday?:" )

print(birthday[tell])