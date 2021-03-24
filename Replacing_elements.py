tests=int(input())
z=[]
for _ in range(tests):
    n,d=[int(x) for x in input().split(" ")]
    arr=list(map(int,input().rstrip().split()))
    m=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i!=j and j!=k and i!=k:
                    if arr[i]==arr[j]+arr[k] and arr[i]==d:
                        m=1
                        z.append("YES")
                        break
    if m!=1:
        z.append("NO")
for x in z:
    print(x)
                
