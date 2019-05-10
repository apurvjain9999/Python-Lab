import random

print("Enter your option")
st=int (input("Press 1 to start the game, and any key to exit"))

while st==1:
			b=int(input("Player 1: \nPress1 to start throw the dice\n"))
			
			if b==1:
					x=random.randint(1,6)
					
			else :
					x=0
			
			print("Player 1: " + str(x))
			
			b=int(input("Player 2: \nPress1 to start throw the dice\n"))
			
			if b==1:
					y=random.randint(1,6)
					
			else :
					y=0
			print("Player 2: " + str(y))
				
			b=int(input("Player 1: \nPress1 to start throw the dice\n"))
			
			if b==1:
					z=random.randint(1,6)
					
			else :
					z=0
			print("Player 3: " + str(z))
				
			b=int(input("Player 1: \nPress1 to start throw the dice\n"))
			
			if b==1:
					w=random.randint(1,6)
					
			else :
					w=0
			print("Player 4: " + str(w))
					
			print("\n")
			
			if ((x>y) and (x>z) and(x>w)):
				print("Player 1 wins")
				
			elif ((y>x) and (y>z) and(y>w)):
				print("Player 2 wins")
				
			elif ((z>x) and (z>y) and(z>w)) :
				print("Player 3 wins")
				
			else :
				print("Player 4 wins")
				
			st=0
			st=int(input("Want to start the game again ? \nPress 1 to start the game or any key to exit"))
                                     
print("\nThanks for playing the game\n")

