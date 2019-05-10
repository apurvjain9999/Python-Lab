import re

file1 = open("1.txt","r")

match=input("Enter String to search for: ")
l = file1.read()
lines = l.split("\n")

flag = 0
for line in lines :
    
    
    if re.search(match,line)!=None:
        flag = 1
        print(line)
        
        


if flag!=1:
    print("The string is not present in the file ")

file1.close()
