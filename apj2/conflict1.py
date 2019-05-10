users =int(input("Enter number of users"))
accounts = int(input("Enter number of accounts"))
i=0
list = []

while i<users:
    ch = "T"
    ch = ch + str(i+1)
    list.append(ch)
    i=i+1

print(list)

list1 =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
while i<accounts:
    ch1 = list1[i]
    ch2 = "read(" + ch1 + ")"
    list.append(ch2)
    ch3 = "write(" + ch1 + ")"
    list.append(ch3)
    i=i+1

print(list)
words = []
file1 = open("input.txt","w")
i=1
while i!=0:
    ans=0
    str=input("Enter Transaction")
    file1.write(str)
    file1.write("\n")
    word=str.split()
    words.append(word)
    ans=int(input("Want to Enter More? Y:0, N:1"))
    k=ans
    if k!=0:
        break
    else:
        continue
         
file1.close()
print(words)
print(store1)
print(store2)
file2 = open("output.txt","w")
flag=0
count=0
k=len(list)
k=k-users
for i in range(len(store1)):
    for index in range(len(store1)):
        j=k
        if index==count:
            continue
        else:
            flag1=1
            while j<len(list):
                if store1[i]==list[j-1]:
                    if store1[index]==list[j]:
                        if store2[index]==store2[i]:
                            flag1=0
                            break
                        else:
                            file2.write(store2[i])
                            file2.write("\t")
                            file2.write(store2[index])
                            file2.write("\n")
                if store1[i]==list[j]:
                    if store1[index]==list[j-1] or store1[index]==list[j]:
                        if store2[index]==store2[i]:
                            flag1=0
                            break
                        else:
                            file2.write(store2[i])
                            file2.write("\t")
                            file2.write(store2[index])
                            file2.write("\n")
                j=j+2
            if flag1==0:
                break
    count=count+1
    
file2.close()

file3 = open("output.txt","r")
str = file3.read()
list1=str.split("\n")
check=0
for i in range(len(list1)):
    for j in range(len(list1)):
        if j==i:
              continue
        elif list1[i]==list1[j]:
            print("Conflict")
            check=1
            break
        else:
            continue
    if check==1:
        break
file3.close()

if check!=1:
    print("No Conflict")
    file4 = open("output.txt","w")
    flag1 = 0
    for i in range(len(store2)):
        for j in range(len(store2)):
            if j>i:
                if store2[i]==store2[j]:
                    file4.write(store2[i])
                    if i != len(store2)-2 :
                        file4.write("->")
    file4.close() 

