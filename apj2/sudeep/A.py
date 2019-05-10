rows = int(input("Enter the no. of rows in A"))

for i in range(rows):
    space = rows - i - 1
    while space>0:
        space = space -1
        print(" ",end='')
    for j in range(i):
        if j == 0 or j == i-1:
            print("*",end=' ')
        elif i==rows/2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
    
