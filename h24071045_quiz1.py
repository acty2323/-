x=input("Enter an integer number x : ")#(1)let the user input an integer number x
x1=int(x)#convert string x to integer
y=x[::-1] #reverse x
print("Reversed: ",y)#(2)
y1=int(y)#convert string y to integer
q3=((x1+y1)**2+(x1-y1)**2)**(1/2) #compute the formula
print("Expression:%.4f"%(q3))#(3) print the result of the formula to the 4th decimal places
length=len(x) #x的字串長度
i=0 #令i=0
pro=1#令pro=1
sum=0#令sum=0
result=""
while i<length:       #當i<length時，n為x的第i個數,把pro*n當成新的pro,把sum+n當成新的sum，再把i+1當成新的i，再回去驗證i是否<length
	n=int(x[i:i+1])
	pro=pro*n
	sum+=n
	i+=1
	result=result+str(n)+""
print("Product: ",pro)#(4) #當i不小於length時,print("Product: ",pro)
if len(x)==1:
	print("Digit_Sum: ",x," = ",sum)
else:
	print("Digit_Sum: ","+".join(result)," = ",sum)
	#(5)當i不小於length時,print("Digit_Sum: ",sum)
#6.未完成
i=0 #重新令i=0
odd_s=""#令odd_sum=0
even_s=""#令even_sum=0
while i<length :
	if length%2==0:
		odd_s=odd_s+x[i]+""
		even_s=even_s+x[i+1]+""
		i+=2
	else:
		if i<length-1:
			odd_s=odd_s+x[i]+""
			even_s=even_s+x[i+1]+""
			i+=2
		elif i==length-1:
			xo=x[i]
			odd_s=odd_s+x[i]+""
			break
odd_sum=int(odd_s)
even_sum=int(even_s)
print("Odd-Even: ",odd_sum," - ",even_sum," = ",odd_sum-even_sum)


#7
i=0#重新令i=0
x2=str(x1**10)#先把x1 10次方，再變成字串x2
most_f=0
ii=0
while i<len(x2):
	f=x2.count(x2[i])
	if f>most_f:
		most_f=f
		ii=x2[i]
	i+=1
print("Frequent digit of x**10: ",ii)

result=""
while len(result)<=length :
	k=max(x)
	result=result+k+""
	x=x.replace(k,"")
print(result)




