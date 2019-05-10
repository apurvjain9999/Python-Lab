import mymodule

a = int(input("Enter side 1 of rectangle "))
b = int(input("Enter side 2 of rectangle "))

result = mymodule.rectangle(a,b)
print("Area of Rectangle is -",end=' ')
print(result)

r = int(input("\nEnter radius of circle & Sphere "))

result = mymodule.circle(r)
print("Area of Circle is -",end = ' ')
print(result)

result = mymodule.sphere(r)
print("\nArea of Sphere is - ",end = ' ')
print(result)

b = int(input("\nEnter base of triangle "))
h = int(input("Enter height of triangle "))

result = mymodule.triangle(b,h)
print("Area of Triangle is -",end = ' ')
print(result)
        

        
