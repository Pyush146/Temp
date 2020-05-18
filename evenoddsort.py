a=[]
n=int(input())
for i in range(n):
	p=int(input())
	a.append(p)
print (a)
def sort(a,n):
	l= 0
	r= n-1
	k=0
	while (l<r):
		while(a[l]%2!=0):
			l+= 1
			k+= 1
		while(a[r]%2==0 and l<r):
			r-=1
		if (l<r):
			a[l],a[r] =a[r],a[l]
	odd = a[:k]
	even = a[k:]
	odd.sort(reverse= True)
	even.sort()
	odd.extend(even)
	return odd
result= sort(a,n)
for i in result :
	print (str(i)+" ")
			