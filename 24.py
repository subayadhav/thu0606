a1=input()
b=0
for i in a1:
    if 48<ord(i)<57:
        b+=1
if b==len(a1):
    print("yes")
else:
    print("no")
