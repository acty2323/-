s=input("Enter a string :")
i=len(s)
ii=i
f=0
e=ii-1
while f<e:
	e=ii-1
	while f<e and ii>1:
		if s[f]!=s[e]:
			print(s[f:e+1])
			ii=ii-1
		elif (s[f]==s[e]) and (s[f:e+1]!=s[f:e+1:-1]):
			ii=ii-1
		elif (s[f]==s[e]) and (s[f:e+1]==s[f:e+1:-1]):
			
			break
	if (s[f]==s[e]) and (s[f:e+1]==s[f:e+1:-1]):

		break
	f+=1
	ii=i
ss=s[f:e+1]
print(ss)
print("Length is",len(ss))
