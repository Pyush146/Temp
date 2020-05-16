def swap(l,x,y):
	l[x],l[y] = l[y],l[x]
def perm(l,i):
	if (i == len (l)):
		print (l) 
	else :
		for j in range(i,len(l)):
			swap(l,i,j)
			perm(l,i+1)
			swap(l,i,j)
l= list(input())
perm(l,0)

		