length=int(input())
arr=[]
z=[]
m=[]
for _ in range(length):
    y,str1=[str(x) for x in input().split(" ")]
    arr.append([int(y),str1])
    z.append(int(y))
for i in range(len(arr)//2):
    arr[i][1]='-'
arr.sort(key=lambda tup: tup[0]) 
print(*[x[1] for x in arr])


                                        
                                        
