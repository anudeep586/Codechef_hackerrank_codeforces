from itertools import permutations
tests=int(input())
z=[]
for _ in range(tests):
    length=int(input())
    red=list(map(str,input().rstrip().split()))
    blue=list(map(str,input().rstrip().split()))
    red1=[''.join(p) for p in permutations(red[0])]
    blue1=[''.join(p) for p in permutations(blue[0])]
    count=0
    count1=0
    count2=0
    for i in range(len(red1)):
        if int(blue1[i])>int(red1[i]):
            count=count+1
        elif int(blue1[i])<int(red1[i]):
            count1=count1+1
        elif int(blue1[i])==int(red1[i]):
            count2=count2+1
    if count>count1 and count>count2:
            z.append("BLUE")
    elif count1>count and count1>count2:
            z.append("RED")
    elif count2>count1 and count2>count:
        z.append("EQUAL")
for x in z:
    print(x)
    
    
   
                
