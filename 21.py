x,a1=map(int,input().split(" "))
y,b=map(int,input().split(" "))
z,c=map(int,input().split(" "))
if(x==y==z):
    print("yes")
elif(a1==b==c):
    print("yes")
elif(x==a1 and y==b and z==c):
    print("yes")
else:
    print("no")
