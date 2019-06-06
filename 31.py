a1=input()
b=[]
for i in a1:
    if i not in b:
        b.append(i)
if len(b)>1:
    if a1.count(b[0])==a1.count(b[1]):
        print("yes")
    else:
        print("no")
else:
    print("no")
