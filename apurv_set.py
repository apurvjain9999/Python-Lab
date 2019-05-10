z=set(('a','b','c'))
print(z)
y={1,2,3}
print(y)
x={2,3}
print(y.issubset(x))
print(y<x)
print(y.issuperset(x))
print(y>x)
z.add('d')
print(z)
z.remove('c')
del z;

try :
	print(z)

except :
	print("z is not defined")

finally :
	print("Thank You")

print(x.intersection(y))
print(x&y)
print(x.union(y))
print(x|y)
print(y.difference(x))
print(y-x)

print(y^x)
