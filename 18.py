num1=int(input())
r=[]
a=0
count=0
for i in range(num1):
    c=input()
    r.append(c)
for i in r:
	for j in i:
		a+=ord(j)
	if(a==612):
		count+=1
	a=0
print(count)
