v,w=map(int,input().split())
x1=v*w
b=[]
for i in range(1,x1+1):
    if i%v==0 and i%w==0:
        b.append(i)
print(min(b))
