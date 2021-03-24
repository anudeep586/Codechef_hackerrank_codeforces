s=list(input())
s=s[::-1]
z=[]
mkl=[]
for i in s:
    mkl.append(i)
for i in range(len(s)):
    a=s.count(s[0])
    b=mkl.count(s[0])//2
    c=z.count(s[0])
    if a==b and s[0] not in z:
        z.append(s[0])
        s.remove(s[0])
    else:
        if len(z)==0:
            z.append(s[0])
            s.remove(s[0])
        elif ord(s[0])>=ord(z[-1]) and c<=b-1:
            z.append(s[0])
            s.remove(s[0])
        elif a>b and ord(s[0])<ord(z[-1]) and c<=b-1:
            d=len(z)-1
            for nji in range(len(z)):
                if ord(z[d-nji])>ord(s[0]):
                    z.remove(z[d-nji])
                else:
                    break;
            z.append(s[0])
            s.remove(s[0])
        elif a==b and ord(s[0])<ord(z[-1]) and c<=b-1:
            z.append(s[0])
            s.remove(s[0])
print(''.join(z))
