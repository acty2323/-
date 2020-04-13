a=True
print("Enter the matrix by multiple lines: ")
nn=[]
while a:
	n=input()
	if n=="q":
		a=False
	else:
		nn+=[n]
		a=True
i=0
while i<len(nn)-1:
	if len(nn[i])!=len(nn[i+1]):
		print("Invalid matrix.")
		break
	else:
		i+=1
nn1=nn[:]
i=0
j=0
l=len(nn[0])
try:
	while i <len(nn):
		j=0
		while j<l:
			if nn1[i][j]=="0":
				nn[i]="0"*l
				k=0
				while k<len(nn1):
					nn[k]=nn[k][0:j]+"0"+nn[k][j+1:]
					k+=1
				j+=1
			else:
				j+=1
		i+=1
except AttributeError:
	0
except IndexError:
	0
print(nn1)
print(nn)
i=0
while i<len(nn):
	print(nn[i])
	i+=1


