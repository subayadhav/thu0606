aa=list(input())
for i in range(0,len(aa),2):
	a1[i],aa[i+1]=aa[i+1],aa[i]
print("".join(aa))
