p=input("Enter a paragraph")
list=p.split(' ')
print(list)
j={u:list.count(u) for u in list}
print(j)