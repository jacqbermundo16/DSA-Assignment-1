
#Assignment 1:
#Create a program that will print your nickname using only asterisk character (*)

#Steps
# create an empty nested list for each letter of the name
# create a code that stores "*" that will print each letter
    #specify the conditions to form the letter
#create a code that print each letter altogether to form the name


name = "JACQ"

# create an empty nested list for each letter of the name
printJ = [[" " for i in range(6)] for j in range(6)]
printA = [[" " for i in range(6)] for j in range(6)]
printC = [[" " for i in range(6)] for j in range(6)]
printQ = [[" " for i in range(6)] for j in range(6)]

# create a code that stores "*" that will print each letter
# code for J
for row in range(6):
    for col in range(6):
        #specify the conditions to form the letter
        if (row<5  and col==5) or (row==5 and (col>0 and col<5)) or (row==4 and col==0):
            printJ[row][col] = "*"

# code for A
for row in range(6):
    for col in range(6):
        #specify the conditions to form the letter
        if ((row==0 or row==3)  and (col>0 and col<5)) or (row!=0 and (col==0 or col==5)):
            printA[row][col] = "*"

# code for C
for row in range(6):
    for col in range(6):
        #specify the conditions to form the letter
        if ((row==0 or row==5) and col>0) or ((row!=0 and row!=5) and col==0):
            printC[row][col] = "*"

# code for Q
for row in range(6):
    for col in range(6):
        #specify the conditions to form the letter
        if ((row==0 or row==5) and (col>0 and col<4)) or ((row!=0 and row!=5) and (col==0 or col==4)) or (row==5 and col==5) or (row==3 and col==3) or (row==4 and col==4):
            printQ[row][col] = "*"

#create a code that print each letter altogether to form the name
for i in range(6):
    for j in range(6):
        print(printJ[i][j], end = " ")
    print(end = "  ")
    for j in range(6):
        print(printA[i][j], end = " ")
    print(end = "  ")
    for j in range(6):
        print(printC[i][j], end = " ")
    print(end = "  ")
    for j in range(6):
        print(printQ[i][j], end = " ")
    print()