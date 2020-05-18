l=[]
n=int(input())
for i in range(n):
	a= int(input())
	l.append(a)
print (l)
mr=l[n-1]
l[n-1]=-1
for i in range(n-2,-1,-1):
	t=l[i]
	l[i]=mr
	if mr<t:
		mr=t
for i in range(n):
	print (l[i])
	