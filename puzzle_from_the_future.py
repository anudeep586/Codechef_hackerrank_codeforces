from itertools import combinations
tests=int(input())
k=[]
for _ in range(tests):
    arr=[]
    z=[0]
    length=int(input())
    b=int(input())
    for i in range(length):
        arr.append(0)
        arr.append(1)
    com=combinations(arr,length)
    res=[list(i) for i in com]
    for i in res:
        integers =i
        strings = [str(integer) for integer in integers]
        a_string = "".join(strings)
        a= int(a_string)
        c=(int(a)+int(b))
        res1 = [int(x) for x in str(c)]
        j=0
        while True:
            if j+1==len(res1):
                break
            else:
                if res1[j]==res1[j+1]:
                    res1.remove(res1[j])
                else:
                    j=j+1
        strings1 = [str(integer) for integer in res1]
        a_string1 = "".join(strings1)
        d= int(a_string1)
        if z[0]<d:
            z[0]=d
            x=a_string
    k.append(x)
for x in k:
    print(x)
                
                
            
        
    
