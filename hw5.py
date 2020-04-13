lines=[]
with open("C:/Users/USER/Downloads/kobe.csv","r") as file:
	r=file.readline()
	for line in file:
		lines.append(line.split(","))
#1
dic={}
ii=0
while ii<len(lines):
	shot_dis=lines[ii][8]
	if shot_dis in dic:
		dic[shot_dis]+=1
	else:
		dic[shot_dis]=1
	ii+=1
l=[]
for key,val in dic.items():
	l+=[(val,key)]
l.sort(reverse=True)
print("Ans: ",l[0][1])
#2
dic={"Right Side(R)":0,"Center(C)":0,"Left Side(L)":0,"Left Side Center(LC)":0,"Right Side Center(RC)":0,"Back Court(BC)":0}
dic_in={"Right Side(R)":0,"Center(C)":0,"Left Side(L)":0,"Left Side Center(LC)":0,"Right Side Center(RC)":0,"Back Court(BC)":0}
ii=0
while ii<len(lines):
	shot=int(lines[ii][9])
	dic[lines[ii][11]]+=1
	dic_in[lines[ii][11]]+=shot
	ii+=1
for key in dic.keys():
	dic[key]=dic_in[key]/dic[key]
l=[]
for key,val in dic.items():
	l+=[(val,key)]
l.sort(reverse=True)
print("Ans: ",l[0][1])
#3
print("(3)Ans:")
ii=0
two=0
three=0
two_in=0
three_in=0
while ii<len(lines):
	if lines[ii][15][:3]=="SAS":
		if lines[ii][10][0]=="2":
			two+=1
			if lines[ii][9]=="1":
				two_in+=1
				ii+=1
			else:
				ii+=1
		else:
			three+=1
			if lines[ii][9]=="1":
				three_in+=1
				ii+=1
			else:
				ii+=1
	else:
		ii+=1
print("2PT Field Goal: %.3f"%(two_in/two))
print("3PT Field Goal: %.3f"%(three_in/three))
#4
print("Ans: ")
game=[]
dic={}
ii=0
while ii<len(lines):
	oppo,game_id=lines[ii][15][:3],lines[ii][2]
	if game_id not in game:
		game+=[game_id]
		if oppo in dic:
			dic[oppo]+=1
		else:
			dic[oppo]=1
	else:
		ii+=1
l=[]
for key,val in dic.items():
	l+=[(val,key)]
l.sort(reverse=True)
for i in range(0,5):
	print(l[i][1],":",l[i][0])
#5
get={}
ii=0
while ii<len(lines):
	oppo,score=lines[ii][15][:3],int(lines[ii][9])*int(lines[ii][10][0])
	if oppo in get:
		get[oppo]+=score
	else:
		get[oppo]=score
	ii+=1
for key in get.keys():
	get[key]=get[key]/dic[key]
l=[]
for key,val in get.items():
	l+=[(val,key)]
l.sort(reverse=True)
for i in range(0,5):
	print(i+1,l[i][1],"%.2f"%(l[i][0]))
#6
dic={}
ii=0
while ii<len(lines):
	game_id,time,score,oppo=lines[ii][2],int(lines[ii][3]),int(lines[ii][9])*int(lines[ii][10][0]),lines[ii][15][:3]
	if (game_id,oppo) in dic:
		if time<=3:
			dic[(game_id,oppo)]+=score
			ii+=1
		else:
			ii+=1
	else:
		dic[(game_id,oppo)]=score
		ii+=1
l=[]
for key,val in dic.items():
	l+=[(val,key)]
l.sort(reverse=True)
i=0
while i<5:
	print("id =",l[i][1][0],", vs.",l[i][1][1],":",l[i][0])
	i+=1
#7
dic={}
dic_in={}
ii=0
while ii<len(lines):
	game_day,ty,time,shot=lines[ii][13][:4],lines[ii][0],int(lines[ii][7]),int(lines[ii][9])
	if game_day not in dic:
		if time<=30 and ty=="Jump Shot":
			dic[game_day]=1
			dic_in[game_day]=shot
			ii+=1
		else:
			ii+=1
	else:
		if time<=30 and ty=="Jump Shot":
			dic[game_day]+=1
			dic_in[game_day]+=shot
			ii+=1
		else:
			ii+=1
for key in dic.keys():
	dic[key]=dic_in[key]/dic[key]
l=[]
for key,val in dic.items():
	l+=[(key,val)]
l.sort()
i=0
while i<len(l):
	print(l[i][0],": %.3f"%(l[i][1]))
	i+=1
#8
off={}
off_in={}
no_off={}
no_off_in={}
game=[]
ii=0
while ii<len(lines):
	game_id,oppo,shot,playoff,ty=lines[ii][2],lines[ii][15][:3],int(lines[ii][9]),lines[ii][5],lines[ii][10][0]
	if playoff=="0" and ty=="2":
		if game_id in game:
			no_off[oppo]+=1
			if shot==1:
				no_off_in[oppo]+=1
		else:
			game+=[game_id]
			no_off[oppo]=1
			if shot==1:
				no_off_in[oppo]=1
			else:
				no_off_in[oppo]=0
	elif playoff=="1" and ty=="2":
		if game_id in game:
			off[oppo]+=1
			if shot==1:
				off_in[oppo]+=1
		else:
			game+=[game_id]
			off[oppo]=1
			if shot==1:
				off_in[oppo]=1
			else:
				off_in[oppo]=0
	ii+=1
for key in off.keys():
	off[key]=off_in[key]/off[key]
for key in no_off.keys():
	no_off[key]=no_off_in[key]/no_off[key]
l=[]
ll=[]
ans=[]
for key,val in off.items():
	l+=[(val,key)]
for key,val in no_off.items():
	ll+=[(val,key)]
print(l)
print(ll
	)
for i in range(0,len(l)):
	if l[i][0]>ll[i][0]:
		ans+=[(l[i][0]-ll[i][0],l[i][1])]
ans.sort(reverse=True)
print(ans)
for i in range(0,5):
	print(ans[i][1],":",ans[i][0])
# 9
dic={}
ii=0
while ii<len(lines):
	game_day,score=lines[ii][13],int(lines[ii][9])*int(lines[ii][10][0])
	if game_day in dic:
		dic[game_day]+=score
		ii+=1
	else:
		dic[game_day]=score
del dic["2012/1/8"]
l=[]
for key,val in dic.items():
	l+=[(val,key)]
new_=[]
i=0
a=True
while i<len(l):
	if l[i][0]>=25:
		i+=1
		a=True
		while a:
			if l[i][0]>=25:
				i+=1
			else:
				new_.append((l[:i]))
				del l[:i]
				i=0
				a=False
	else:
		del l[i]
		i=0
i=0
dic={}
for i in range(0,len(new_)):
	dic[i]=len(new_[i])
l=[]
for key,val in dic.items():
	l+=[(val,key)]
l.sort(reverse=True)
for i in range(0,3):
	print(l[i][0],new_[l[i][1]][0][1],"~",new_[l[i][1]][-1][1])