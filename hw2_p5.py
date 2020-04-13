blank="%-12s%-12s%-12s"
width=36
print(blank%("PlayerA","PlayerB","Result"))
print(blank%("Rock","Rock","Tie"))
print(blank%("Rock","Paper","PlayerB"))
print(blank%("Rock","Scissors","PlayerA"))
print(blank%("Paper","Rock","PlayerA"))
print(blank%("Paper","Paper","Tie"))
print(blank%("Paper","Scissors","PlayerB"))
print(blank%("Scissors","Rock","PlayerB"))
print(blank%("Scissors","Paper","PlayerA"))
print(blank%("Scissors","Scissors","Tie"))
print("-"*width)
a="Rock"
b="Paper"
c="Scissors"
d="bye"
t=True
while t:
	A=input("PlayerA ?")
	while A!=d:
		if A!=a or A!=b or A!=c:
			print("Invalid input.Please enter again.")
			A=input("PlayerA ?")
			
		else:
			B=input("PlayerB ?")
			if B!=a or B!=b or B!=c or B!=d:
				print("Invalid input.Please enter again.")
				B=input("PlayerB ?")
			else:
				break

	if A==d:
		break
	elif B==d:
		break
	elif A==B==(a or b or c):
		print("Outcome: Tie")
	elif A==a:
		if B==c:
			print("Outcome: PlayerA wins!")
		if B==b:
			print("Outcome: PlayerB wins!")
	elif A==b:
		if B==a:
			print("Outcome: PlayerA wins!")
		elif B==c:
			print("Outcome: PlayerB wins!")
	elif A==c:
		if B==b:
			print("Outcome: PlayerA wins!")
		elif B==a:
			print("Outcome: PlayerB wins!")