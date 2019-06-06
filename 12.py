a1,b = map(int,input().split())
b = b%a1
l1 = list(map(int,input().split()))
l2 = l1[-b:] + l1[:-b]
print(*l2)
