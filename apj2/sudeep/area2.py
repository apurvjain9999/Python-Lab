import mymodule
choice = 0

while choice != 5:
    print("\n\n1.Rectangle")
    print("2.Circle")
    print("3.Triangle")
    print("4.Sphere")
    print("5.Exit")


    choice = int(input("\nEnter your choice "))

    if choice == 1:
        a = int(input("Enter side 1 of rectangle "))
        b = int(input("Enter side 2 of rectangle "))
        result = mymodule.rectangle(a,b)
        print("Area of Rectangle is -",end=' ')
        print(result)
    elif choice == 2 or choice == 4:
        r = int(input("\nEnter radius of circle & Sphere "))

        result = mymodule.circle(r)
        print("Area of Circle is -",end = ' ')
        print(result)

        result = mymodule.sphere(r)
        print("\nArea of Sphere is - ",end = ' ')
        print(result)
    elif choice == 3:
        b = int(input("\nEnter base of triangle "))
        h = int(input("Enter height of triangle "))

        result = mymodule.triangle(b,h)
        print("Area of Triangle is -",end = ' ')
        print(result)
        
    else:
        exit
        
        
    

    








        

        
