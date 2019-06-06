a1=input()
b=''
for i in a1:
    if i.isupper():
        b+=i.lower()
    if i.islower():
        b+=i.upper()
print(b)
