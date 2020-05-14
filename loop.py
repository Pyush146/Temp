n= int(input())
if (n%2)==0 :
	print ("even")
else :
	print ("odd")
for i in range(2,n) :
	if (n%i)==0 :
		print ("not prime")
		break
else :
	print ("prime")
p=n
r=0
s=0
while (n>0) :
	d=n%10
	r= r*10+d
	s=s+d*d*d
	n=n//10
print ("for palindrome")
if p==r :
	print ("Palindrome")
else :
	print ("Not Palindrome")
print ("for armstrong")
if p==s :
	print ("Armstrong")
else :
	print ("Not Armstrong")
