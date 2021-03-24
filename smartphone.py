try:
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    arr=sorted(arr)
    arr=arr[::-1]
    for i in range(len(arr)):
        arr[i]=arr[i]*(i+1)
    print(max(arr))
except:pass
        
