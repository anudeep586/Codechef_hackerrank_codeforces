from itertools import permutations
tests=int(input())
for _ in range(tests):
    n,k=[int(x) for x in input().split(" ")]
    arr=list(map(int,input().rstrip().split()))
    arr=sorted(arr)
    res=[]
    for size in range(len(arr)):
        res1=list(permutations(arr,size))
        mkl=[list(ele) for ele in res1]
        res.append(mkl)
    print(res)
