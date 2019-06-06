a1=input()
b=''
for i in a1:
    if i=="X":
        b+="A"
    elif i=="Y":
        b+="B"
    elif i=="Z":
        b+="C"
    else:
        b+=chr(ord(i)+3)
print(b)
