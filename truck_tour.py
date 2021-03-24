length=int(input())
arr=[]
z=[]
for _ in range(length):
    a,d=[int(x) for x in input().split(" ")]
    arr.append([a,d])
    for i in range(len(arr)):
            if arr[i][0]>arr[i][1]:
                z.append([(arr[i][0]-arr[i][1]),i])
k=0
w=0
for i in range(len(z)):
    if k<z[i][0]:
        k=z[i][0]
        w=z[i][1]
print(w)
            
                
                
