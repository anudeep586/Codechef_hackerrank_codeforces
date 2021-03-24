tests=int(input())
for _ in range(tests):
    n,k=[int(x) for x in input().split(" ")]
    arr=list(map(int,input().rstrip().split()))
    arr=sorted(arr)
    arr=arr[::-1]
    if sum(arr)<2*k:
        print(-1)
    elif sum(arr)==2*k:
        print(len(arr))
    elif sum(arr)>2*k:
        i=0
        sa=0
        t=0
        while i<n:
            sa=sa+arr[i]
            if sa>=k:
                break
            for j in range(i+1,n):
                if arr[j]>=(k-sa):
                    t=1
            if t==1:
                sa=sa+arr[j]
                temp=arr[j]
                arr[j]=arr[i+1]
                arr[i+1]=temp
                a=i
        i=a
        sb=0
        m=0
        print(arr)
        while i<n:
            sb=sb+arr[i]
            if sb>=k:
                break
            for j in range(i+1,n):
                if(arr[j]>=(k-sb)):
                    m=1
        if m==1:
                sb=sb+arr[j]
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if m!=1:
            for j in range(i+1,n):
                if (arr[m]<(k-sb)):
                    break
            temp=arr[m]
            arr[m]=arr[i+1]
            arr[i+1]=temp
        print(arr)
        










        
                
            
            
    
