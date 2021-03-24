loflist=int(input())
z=[]
l=[]
k=[]
count=0
list1=list(map(int,input().rstrip().split()))
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        for t in range(j+1,len(list1)):
            l.append([list1[i],list1[j],list1[t]])
for i in range(len(l)):
    a=l[i][0]
    b=l[i][1]
    c=l[i][2]
    if a+b>c and b+c>a and a+c>b:
        if len(k)==0:
            k.append(l[i])
            count=count+1
        elif len(k)!=0:
            if sum(k[0])<sum(l[i]):
                k[0]=l[i]
                count=count+1
if count>0:
    k[0]=sorted(k[0])
    print(*k[0])
else:
    print("-1")
                
        
