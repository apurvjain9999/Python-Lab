import matplotlib.pyplot as plt
file = open("1.txt","r")
str = file.read()
file.close()
list1 = str.split()
freq = [list1.count(d) for d in list1]
print(dict(zip(list1,freq)))

#dic = dict(zip(list1,freq))
total = 0

for i in list1:
    total += 1

print(total)

per = []
for i in freq:
    per.append((i/total)*100)

print(dict(zip(list1,per)))
file = open("3.txt","w+")
file.write(str(dict(zip(list1,per))))

li = []
count = 0
for i in freq:
    li.append(count)
    count+=1
print(li)
plt.barh(list1,per)
plt.ylabel("percentage")
plt.xlabel("word")
plt.show()
file.close()
