#Aryan Roy
#Lower Triangle
rows = int(input("Enter number of rows: "))

for a in range(rows):
    for b in range(a+1):
        print("* ", end="")
    print()

#Upper Triangle
rows = int(input("Enter number of rows: "))

for c in range(rows, 0 ,-1):
    for d in range(0,c):
        print("* ", end=" ")
    print()

#Pyramid
rows = int(input("Enter number of rows: "))
e = 0

for f in range(1, rows+1):
    for space in range(1, (rows-f)+1):
        print(end="  ")
   
    while e!=(2*f-1):
        print("* ", end="")
        e += 1
   
    e = 0
    print()
