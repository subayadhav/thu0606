d=int(input())
e1=2
l=[]
v=[]
for e1 in range(e1,d+1):
  i=2
  while i<e1:
    if e1%i==0:
      break
    i=i+1
  if e1==i:
    l.append(e1)
for i in l:
  if d%i==0:
    v.append(i)
for i in range(0,len(v)-1):
  print(v[i],end=" ")
print(v[len(v)-1])
