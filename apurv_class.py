class xyz:
    def __init__(self):
        self.__left=10
        self.right=20
    def fun(self,a):
        self.right=a

x=xyz()
try:
    print(x.right)
    print(x.left)

except:
    print("x.left is private")
x.fun(30)
print(x.right)
a=[1,2,3]
b=iter(a)
print(next(b))
print(next(b))
print(next(b))

