n=int(input())
arr=list(map(int,input().rstrip().split()))
arr=reversed(arr)
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print(*reversed(res))
