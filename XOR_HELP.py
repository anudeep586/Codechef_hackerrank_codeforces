t=int(input())
for _ in range(t):
    n=int(input())
    if (n-1)%4==0:
        print("1")
    elif(n==2):
        print("3")
    elif(n==3 or ((n-3)%4==0)):
        print("0")
    elif(n%4==0):
        print(n)
    elif(n-2)%4==0:
        print(n+1)
