#problem1-1
s1="spam"
s2="ni!"
print("The Knights who say," + s2) #(a)
print(3 * s1 + 2 * s2) #(b)
print(s1[1]) #(c)
print(s1[1:3])
print(s1[2]+ s2[:2])
print(s1 + s2[-1] )
print(s2[len(s2)//2] )

#problem1-2
s1="spam"
s2="ni!"
s3=s2.replace("n","N")
print(s3) #(a)
print(s2+s1+s2) #(b)
s4="S"+s1[1:]
print(3*(s4+s3)) #(c)
print(s1[:3]+"n") #(d)
#problem1-3
print("Looks like %s and %s for breakfast" % ("spam", "eggs") ) #(a)
print("There is %d %s %d %s" % (1, "spam", 4, "you")) #(b)
print("Hello %s %s" % ("Suzie", "Programmer") ) #(c).
print("%0.2f %0.2f" % (2.3, 2.3468) )#(d)
print("%7.5f %7.5f" % (2.3, 2.3468)) #(e)
print("Time left %02d:%05.2f" % (1, 37.374)) #(f)
print("%3d" % (14) ) #(g).

#problem1-6
thief=1
liar=1
while thief<=4:
	if liar==1:
		thief=1 
		thief=3 
		thief=4 
		liar=3
	if liar==2:
		thief!=1 
		thief!=3 
		thief=4 
		liar=3
	if liar==3:
		thief!=1 
		thief=3 
		thief!=4 
		liar=3
	if liar==4:
		thief!=1
		thief=3 
		thief=4 
		liar!=3
	if thief==liar:
		print("The thief is", thief)
		break
	thief=thief+1