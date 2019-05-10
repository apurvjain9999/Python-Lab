#file1 = open("no_conflict.txt","r")
file1 = open("conflict.txt","r")
text = file1.read()
list = ["T1","T2","T3","read(A)","write(A)","read(B)","write(B)"]
words = []
print(text)
lines = text.split("\n")
flag=0
for l in lines:
    word = l.split()
    words.append(word)
store1 = []
store2 = []
print(words)
for i in words:
    flag=0
    for j in i:
        if flag!=0:
            continue
        if j==list[0] or j==list[1] or j==list[2]:
            flag=1
            store1.append(i[2])
            store2.append(j)
file1.close()
print(store1)
print(store2)
file2 = open("output1.txt","w")
flag=0
count=0
for i in range(len(store1)):
    for index in range(len(store1)):
        if index==count:
            continue
        else:
            if store1[i]==list[3]:
                if store1[index]==list[4]:
                    if store2[index]==store2[i]:
                        break
                    else:
                        file2.write(store2[i])
                        file2.write("\t")
                        file2.write(store2[index])
                        file2.write("\n")

            if store1[i]==list[5]:
                if store1[index]==list[6]:
                    if store2[index]==store2[i]:
                        break
                    else:
                        file2.write(store2[i])
                        file2.write("\t")
                        file2.write(store2[index])
                        file2.write("\n")


            if store1[i]==list[4]:
                if store1[index]==list[3] or store1[index]==list[4]:
                    if store2[index]==store2[i]:
                        break
                    else:
                        file2.write(store2[i])
                        file2.write("\t")
                        file2.write(store2[index])
                        file2.write("\n")

            if store1[i]==list[6]:
                if store1[index]==list[5] or store1[index]==list[6]:
                    if store2[index]==store2[i]:
                        break
                    else:
                        file2.write(store2[i])
                        file2.write("\t")
                        file2.write(store2[index])
                        file2.write("\n")
        
    
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
    file4 = open("output1.txt","w")
    flag1 = 0
    for i in range(len(store2)):
        for j in range(len(store2)):
            if j>i:
                if store2[i]==store2[j]:
                    file4.write(store2[i])
                    if i != len(store2)-2 :
                        file4.write("->")
    file4.close()                    
    

                
                        
                    
        
            
            
        
    
