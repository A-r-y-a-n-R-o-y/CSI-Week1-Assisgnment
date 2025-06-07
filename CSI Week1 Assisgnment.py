#Lower Triangle
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

#Upper Triangle
rows = int(input("Enter number of rows: "))

for i in range(rows, 0 ,-1):
    for j in range(0,i):
        print("* ", end=" ")
    print()

#Pyramid
rows = int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))
