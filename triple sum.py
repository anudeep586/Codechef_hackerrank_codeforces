from itertools import combinations
lena,lenb,lenc=[int(x) for x in input().split(" ")]
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
c=list(map(int,input().rstrip().split()))
arr=[]
for i in a:
    arr.append(i)
for i in b:
    arr.append(i)
for i in c:
    arr.append(i)
l = list(combinations(arr,3))
res1=[list(ele) for ele in l]
count=0
res=[]
for i in range(len(res1)):
    if res1[i] not in res:
        res.append(res1[i])
for i in range(len(res)):
    p=res[i][0]
    q=res[i][1]
    r=res[i][2]
    if p<=q and q>=r and p in a and q in b and r in c:
        count=count+1
print(count)

