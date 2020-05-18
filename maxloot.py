l=[]
n=int(input())
for i in range(n):
	a=int(input())
	l.append(a)
print (l)
def maxloot(l,n):
	if n==0:
		return 0
	v1= l[0]
	if n==1:
		return v1
	v2= max(l[0],l[1])
	if n==2:
		return v2
	m=0
	for i in range(2,n):
		m= max(l[i]+v1,v2)
		v1= v2
		v2= m
	return m
print (maxloot(l,n))