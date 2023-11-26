import random

arr = []
for i in range(0,3):
    arr.append([])
    for j in range(0,3):
        arr[i].append("-")
print(arr)

user = input("Choose x | o : ")
if user == "x":
    computer = "o"
else:
    computer = "x"

while 1:
    row = int(input("Input row 0 - 2 : "))
    col = int(input("Input col 0 - 2 : ")) 
    if arr[row][col] == "-" or arr[row][col] != computer:
        arr[row][col] = user
    else:
        print("Already added")
        continue
    while 1:
        row = random.randint(0,2)
        col = random.randint(0,2)
        print(row,col)
        if arr[row][col] == "-" : #and arr[row][col] != computer and arr[row][col] != user :
            arr[row][col] = computer
            break  
    for each in arr:
        print(each)
    