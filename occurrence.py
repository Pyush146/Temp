def Count(tup,b) :
	return tup.count(b)
l=[]
n= int(input())
for i in range(n) :
	a= int(input())
	l.append(a)
tup = tuple(l)
print (tup)
b= int(input())
print (Count(tup,b))

