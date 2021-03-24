n=int(input())
arr=list(map(int,input().rstrip().split()))
left=[]
right=[]
p=arr[0]
for i in range(len(arr)):
    if p>arr[i]:
        left.append(arr[i])
    if p<arr[i]:
        right.append(arr[i])
left.append(p)
for x in right:
    left.append(x)
print(*left)
