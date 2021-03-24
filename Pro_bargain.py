test=int(input())
z=[]
for i in range(test):
    a =int(input())
    b= int(input())
    while(b):
        a, b = b, a % b
    z.append(a)
for x in z:
    print(x)


    
