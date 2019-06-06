a,r=map(int,input().split())
c=0
for j in range(a,r+1):
  k=2
  while k<=r:
    if j==k*k:
       c=c+1 
       break
    k+=1
print(c)
