d={}
a={}
n= int(input("enter number "))
for i in range(n):
	key= input("enter key")
	value=input("enter value")
	d[key]=value
print(d)
for key,value in d.items() :
	if value not in a.values():
		a[key]= value
print(a)