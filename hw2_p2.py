n=int(input("Input the range number: "))
k=2
while k<=n:
	i=1
	sum=0
	while i<=k:
		if k%i==0:
			sum+=i
		i+=1
	if sum==2*k:
		print(k)
	k+=1

	
	

		

