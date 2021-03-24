a,c=[int(x) for x in input().split()]
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
z=[]
for i in range(len(b)):
    z.append(a[0]+b[i])
print(*z)
