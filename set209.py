a1,b=map(int,input().split())
l = list()
for x in range(a1,b+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        l.append(x)
print(len(l))
