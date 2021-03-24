arr_count = int(input().strip())
arr = []
for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)
B = [] 
for i in range(len(arr) + 1):
    for j in range(i + 1, len(arr) + 1):
        sub = arr[i:j]
        B.append(sub)
res=[]
for k in B:
    if k not in res:
        res.append(k)
z=[]
for ik in range(len(res)):
    flag=0
    count=0
    for jk in range(len(res[ik])):
        if jk%2==0:
            flag=flag+res[ik][jk]
        else:
            count=count+res[ik][jk]
    asd=(count-flag)**2
    z.append(asd)
print(max(z))
    
