try:
    n,k=[int(x) for x in input().split(" ")]
    count=0
    for i in range(k+1):
        n1 = list(map(int, str(n)))
        if count==k:
            print(n)
            break;
        if n1[-1]!=0:
            n=n-1
            count=count+1
        if n1[-1]==0:
            n=n//10
            count=count+1
except:pass
    
