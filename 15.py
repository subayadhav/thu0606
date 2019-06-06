s1=input()
m=list(s1)
dict = {i:m.count(i) for i in m}
maximum = max(dict, key=dict.get)  
print(maximum)
