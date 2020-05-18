l=[]
n=int(input("enter number :"))
for i in range(n):
	a= int(input())
	l.append(a)
l.sort()
tup= tuple(l)
print (tup)