
f=open("C:/Users/stat/Downloads/kobe.csv","r")
lines=[]
for line in f:
	lines.append(line.strip())
#1
def shot_made_flag():
	correct=[]
	i=0
	while i < len(lines):
		if lines[i][9]==0:
			i+=1
			continue
		elif lines[i][9]==1:
			correct+=[i]
			i+=1
	return correct
def shot_type(correct):
	p3=0
	for i in correct:
		if lines[i][10][0]=="2":
			continue
		elif lines[i][10][0]=="3":
			p3+=1
	return p3
correct=shot_made_flag()
p3=shot_type(correct)
print("(1): ",p3)
#2
correct=shot_made_flag()
correct1=set(correct)
def opponent(a):
	o={}
	i=0
	while i<len(lines):
		if lines[i][15]==a:
			o+={i}
			i+=1
		else:
			i+=1
	return o
def combined_shot_type(b):
	c={}
	i=0
	while i<len(lines):
		if lines[i][1]==b:
			c+={i}
			i+=1
		else:
			i+=1
	return c
o=opponent("NYK")
c=combined_shot_type("Dunk")
u=(correct&o&c)
print("(2): ",len(u)/len(o))
#3未完成
correct=shot_made_flag()
correct1=set(correct)
def game_day():
	i=0
	month=[]
	while i<len(lines):
		l=lines[i][13].find("/")
		r=lines[i][13].rfind("/")
		m=int(lines[i][13][l:r+1])
		
		i+=1
	return month
month=game_day()
M=0
m=12
for h in month:
#4未完成
ans={
"POR":len(opponent("POR"))
"UTA":len(opponent("UTA"))
"VAN":len(opponent("VAN"))
"LAC":len(opponent("LAC"))
"HOU":len(opponent("HOU"))
"SAS":len(opponent("SAS"))
"DEN":len(opponent("DEN"))
"SAC":len(opponent("SAC"))
"IDA":len(opponent("IDA"))
"NYK":len(opponent("NYK"))
"DET":len(opponent("DET"))
"SEA":len(opponent("SEA"))
"IND":len(opponent("IND"))
"MIN":len(opponent("MIN"))
"PHI":len(opponent("PHI"))
'CHI':len(opponent('CHI'))
"BOS":len(opponent("BOS"))
"ATL":len(opponent("ATL"))
"WAS":len(opponent("WAS"))
"MEM":len(opponent("MEM"))
"PHX":len(opponent("PHX"))
for key in ans:
	if value >M:
		M=value 

 





