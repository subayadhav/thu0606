a1,b1=list(map(str,input().split()))
l=len(set(a1)) 
l1=len(set(b1))
if l==l1:
	print ("yes") 
else:
	print ("no")
