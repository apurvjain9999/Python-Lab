import matplotlib.pyplot as plt
file = open("1.txt","r")
string = file.read()
file.close()
file = open("3.txt","w+")
count = 0
list1 = string.split()
freq = [list1.count(c) for c in list1]
for i in list1:
    count = count + 1
file.write("Total words are " + str(count))
per = []
for i in freq:
    per.append((i/count)*100)

file.write(str(dict(zip(list1,per))))
list3 = []
count = 0
for i in freq:
    list3.append(count)
    count = count + 1
plt.barh(list1,per)
plt.xlabel("Percentage")
plt.ylabel("Words")
plt.show()
file.close()
