wt=[]
v=[]
w= int(input())
n= int(input())
for i in range(n):
	a=int(input())
	b=int(input())
	wt.append(a)
	v.append(b)
def knapsack(w,wt,v,n):
	if n==0 or w==0:
		return 0
	if (wt[n-1]>w):
		return knapsack(w,wt,v,n-1)
	else :
		return max(v[n-1]+knapsack(w-wt[n-1],wt,v,n-1),knapsack(w,wt,v,n-1))
print ( knapsack(w,wt,v,n))	