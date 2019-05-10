#polynomial

coffi = {}
c = 0
flag = 0
k = 0
ans = 0
degree = 0

def create():
    global degree
    degree = int(input("Enter degree of the polynomial: "))
    for i in range(degree+1):
        c = int(input("Enter coefficient of the degree " + str(degree-i) + ": "))
        coffi[degree-i] = c
        
def printi():
    count = 0;
    for j in sorted(coffi,reverse=True):
                count = count + 1
                if j==0:
                    if coffi[j]<0:
                        print("",end="")
                    else:
                        print("+",end="")
                    print(str(coffi[j]) + "x" + str(j))
                else:
                    if count!=1:
                        if coffi[j]<0:
                            print("",end="")
                        else:
                            print("+",end="")
                    print(str(coffi[j]) + "x" + str(j),end="")
    
def insert():
    global coffi
    d = len(coffi)
    ins = int(input("Enter degree of the term you want to insert: "))
    c = int(input("Enter coefficient: "))
    if ins<=d:
        if coffi[ins]!=0:
            a = 1
            print("Term already exists")
            print("Want to:  1.Replace or 2.Add to existing?")
            a = int(input("Enter your choice: "))
            if a==1:
                coffi[ins] = c
            else:
                coffi[ins] = coffi[ins] + c
        elif coffi[ins]==0:
            coffi[ins] = c
    else:
        temp = {ins:c}
        coffi.update(temp)
        
def dele():
    ins = int(input("Enter degree of the term you want to delete: "))
    if ins>degree:
        print("Term does not exist")
    else:
        del coffi[ins]
    
while k!=-1:
    print("--------------- Enter -1 when you wnat to terminate the program -------------------")
    print("Select a option")
    print("1. Create a Polynomial")
    print("2. Insert a term in the Polynomial")
    print("3. Print the Polynomial")
    print("4. Delete a term in the Polynomial")
    ans = int(input("Enter your option: "))

    if ans==1:
        create();
        flag = 1
    else:
        if flag==0:
            print("First create a Polynomial")
            print("Try again!")
            continue
        else:
            if ans==2:
                insert()
            elif ans==3:
                printi()
            elif ans==4:
                dele()
            elif ans==-1:
                print("Thank You!")
                break
            else:
                print("Choose valid option")
                print("Try again!")
    
