n1=int(input())
l=[]
c=0 
for i in range(n1):
    l.append(list(map(int,input().split())))
if n1==1 and  l[0]==[1]:
     print('1')
else:
    for i in range(n1):
        for j in range(n1):
            if l[i][j]==1:
                if i==0 and j==n1-1:
                    if(l[i][j-1]==0 and l[i+1][j]==0):
                            c=c+1
                elif i==0 and j==0:
                    if l[i][j+1]==0 and l[i+1][j]==0:
                        c=c+1
                elif i==0 and l[i][j-1]==0 and l[i][j+1]==0 and l[i+1][j]==0:
                    c=c+1
                elif i==n1-1 and j==n1-1:
                    if l[i-1][j]==0 and l[i][j-1]==0:
                        c=c+1
                elif i==n1-1 and l[i][j-1]==0 and l[i][j+1]==0 and l[i-1][j]==0:
                    c=c+1
                elif i!=0 or i!=n1-1 and (l[i][j+1]==0 and l[i+1][j]==0 and l[i-1][j]==0 and l[i][j-1]==0):
                    c=c+1
    print(c)    
