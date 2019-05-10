
string = input("Enter a pararaph")

list1 = string.split()
freq = [list1.count(c) for c in list1]
print(dict(zip(list1,freq)))
