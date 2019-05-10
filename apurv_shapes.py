import apurv_shapes_module

i=1
while(i!=5):
	print("Main Menu")
	print("1. Rectangle")
	print("2. Circle")
	print("3. Triangle")
	print("4. Sphere")
	print("5. Exit")
	a=int(input("Select Correct Option: "))
	
	if(a==1):
		l=int(input("Enter Length of the Rectangle: "))
		b=int(input("Enter Breadth of the Rectangle: "))
		area=apurv_shapes_module.rectangle(l,b)
		print("Area = " + str(area))
	
	elif(a==2):
		r=int(input("Enter Radius of the Circle: "))
		area=apurv_shapes_module.circle(r)
		print("Area = " + str(area))
		
	elif(a==3):
		b=int(input("Enter Length of the Base of the Triangle: "))
		h=int(input("Enter Height of the Triangle: "))
		area=apurv_shapes_module.triangle(b,h)
		print("Area = " + str(area))
		
	elif(a==4):
		r=int(input("Enter Radius of the Sphere: "))
		area=apurv_shapes_module.sphere(r)
		print("Area = " + str(area))
		
	elif(a==5):
		print("Thank You")
		break
	
	else :
		print("Wrong Option")
		print("Try Again!")
		continue