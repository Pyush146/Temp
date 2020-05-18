l=[]
c=0
s=" "
n= int(input())
for i in range(n):
	a=input()
	l.append(a)
print (l)
t= tuple(l)
for i in t:
	if t.count(i)>c :
		c=t.count(i)
for i in t:
	for j in t:
		if (t.count(i)==c and t.count(j)==c and i!=j):
			if i<j :
				s=i
			elif i>j :
				s=j
print ("Winner", s)