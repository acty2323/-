#(a)+(b)
n=input("(a)+(b):Enter a positive integer  with square-number length: ")
a=False
i=1
ii=[]
while i<len(n):
	if len(n)%(i*i)==0:
		a=True
		ii+=[i]
		i+=1
	else:
		i+=1
if a==False:
	print("Not square-number length.Try again!")
#(c)
i=0
nn=list((n))
while i<len(nn):
	nn[i]=int(nn[i])
	i+=1
print("(c)Put numbers into a 1-dim list,and print out.")
print(nn)
#(d)
i=0
product=[]
while i<len(nn):
	if i==0:
		product+=[nn[0]*nn[1]]
	if (i!=0) and (i!=len(nn)-1):
		product+=[nn[i-1]*nn[i]*nn[i+1]]
	if i==len(nn)-1:
		product+=[nn[len(nn)-2]*nn[len(nn)-1]]
	i+=1
print("(d)Compute the neighbor numbers product in 1-dim list,and print out.")
print(product)
#(e)
z=max(ii)
dim=[]
for i in range(z):
	dim+=[nn[0:z]]
	del nn[0:z]
i=0
print("(e)Put numbers into a 2-dim list,and print out.")
while i<len(dim):
	print(dim[i])
	i+=1
#(f)
i=0
while i<len(dim):
	dim[i].insert(len(dim[i]),0)
	dim[i].insert(0,0)
	i+=1
dim1=[]
for i in range(len(dim[1])):
	dim1+=[0]
dim.insert(len(dim),dim1)
dim.insert(0,dim1)
print("(f)Zero padding to the 2-dim list,and print out.")
i=0
while i<len(dim):
	print(dim[i])
	i+=1
#(g)
i=1
j=1
add=[]
while i<len(dim)-1:
	j=1
	while j<len(dim[0])-1:
		add+=[dim[i][j]+dim[i-1][j]+dim[i][j-1]+dim[i+1][j]+dim[i][j+1]]
		j+=1
	i+=1
add_ans=[]
for i in range(z):
	add_ans+=[add[0:z]]
	del add[0:z]
i=0
print("(g)Compute the neighbor summation in 2-dim list,and print out.")
while i<len(add_ans):
	print(add_ans[i])
	i+=1


