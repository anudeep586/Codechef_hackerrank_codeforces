tests=int(input())
for _ in range(tests):
    n,k=[int(x) for x in input().split(" ")]
    arr=list(map(int,input().rstrip().split()))
    for i in range(sum(arr)*2):
        if arr[i]%k==0:
            arr.append(arr[i]//k)
        else:
            arr.append(0)
    print(arr)
    print(sum(arr))
