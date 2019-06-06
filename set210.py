a1,b=map(str,input().split())
count=0
for i in range(0,len(a)):
  if(a[i]!=b[i]):
    count=count+1
if(count==1):
  print("yes")
else:
  print("no")
