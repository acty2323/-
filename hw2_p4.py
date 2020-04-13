n=input("Input an integer number: ")
n1=int(n)
x0,x1=(0,1)
if n1==0:
	x=0
if n1==1 or n1==2:
	x=1
while n1>=3:
	x0,x1=(x1,x0+x1)
	n1=n1-1
	x=x0+x1 
print("The %s-th Fibonacci Sequence number is"%(n),x)
