length=int(input())
arr=list(map(int,input().rstrip().split()))
day=0
while True:
    z=[]
    count=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
           z.append(i)
        else:
            count=count+1
    if count==len(arr)-1:
        break
    if len(z)>0:
        for i in range(len(z)):
            a=z[i]
            b=a-i
            arr=arr[:b]+arr[b+1:]
        day=day+1
print(day)
