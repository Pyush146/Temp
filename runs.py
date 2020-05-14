a= int(input())
b= int(input())
c= int(input())
s1= a/60
s2= b/60
s3= c/60
r1= s1*120
r2= s2*120
r3= s3*120
x1= int(r1/6)
x2= int(r2/6)
x3= int(r3/6)
print ("Strike rate :")
print (s1*100,s2*100,s3*100)
print ("runs in 120 balls")
print (r1,r2,r3)
print ("Number of maximum sixes")
print (x1,x2,x3)