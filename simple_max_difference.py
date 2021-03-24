n=int(input())
arr=[]
for _ in range(n):
    n1=int(input())
    arr.append(n1)
i=1
z=[]
while True:
    for j in range(len(arr[0:i])+1):
        if arr[j]<arr[i]:
            z.append(arr[i]-arr[j])
    if i==len(arr)-1:
        break
    i=i+1
if len(z)==0 or sum(z)<=0:
    print("-1")
else:
    print(max(z))
