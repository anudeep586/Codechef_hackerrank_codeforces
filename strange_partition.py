tests=int(input())
k1=[]
for _ in range(tests):
    n,k=[int(x) for x in input().split(" ")]
    arr=list(map(int,input().rstrip().split()))
    c=0
    z=[]
    w=0
    v=0
    for i in range(len(arr)):
        a=arr[i]
        if a%k==0:
            b=a//k
        else:
            b=(a//k)+1
        c=c+b
    z.append(c)
    arr1=[arr[0]+arr[1]]
    for j in range(len(arr[2:])):
        arr1.append(arr[2+j])
    arr2=[arr[-1]+arr[-2]]
    for j in range(len(arr[:-2])):
        arr2.append(arr[j])
    for i in range(len(arr1)):
        a=arr1[i]
        if a%k==0:
            b=a//k
        else:
            b=(a//k)+1
        w=w+b
    z.append(w)
    for i in range(len(arr2)):
        a=arr2[i]
        if a%k==0:
            b=a//k
        else:
            b=(a//k)+1
        v=v+b
    z.append(v)
    k1.append([min(z),max(z)])
for x in k1:
    print(*x)
    
    
    
    
    
