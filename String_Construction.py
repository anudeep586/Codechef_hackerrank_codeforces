tests=int(input())
k=[]
for i in range(tests):
    str1=list(input())
    z=[]
    for i in str1:
        if i not in z:
            z.append(i)
    k.append(len(z))
for i in k:
    print(i)
    
