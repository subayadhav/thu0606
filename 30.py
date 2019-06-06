a1,b,k=map(str,input().split())
k=int(k)
c=0
for i in range(0,len(a1)):
    for j in range(i,len(b)):
        if a1[i]!=b[j]:
            c=c+1 
if c>=k:
    print("yes")
else:
    print("no")
