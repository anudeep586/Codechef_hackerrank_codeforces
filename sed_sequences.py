try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length,k=[int(x) for x in input().split(" ")]
        arr=list(map(int,input().rstrip().split()))
        count=0
        kl=[]
        for ik in range(2,length*2+1):
            if ik%2==0:
                kl.append(ik)
        if sum(arr)%k==0:
            z.append(count)
        else:
            for j in range(len(arr)):
                l=[]
                for i in range(len(kl)):
                    asd=arr[j]
                    arr[j]=kl[i]
                    if sum(arr)%k==0:
                        count=count+1
                        l.append(count)
                        break;
                    else:
                        count=count+1
                        arr[0]=asd
                if len(l)>0:
                    z.append(count)
                    break;
    for x in z:
        print(x)
except:pass

