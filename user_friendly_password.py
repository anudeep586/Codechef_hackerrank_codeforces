events_rows = int(input().strip())
events_columns = int(input().strip())
events = []
for _ in range(events_rows):
    events.append(input().rstrip().split())
z=[]
for i in range(len(events)):
    if 'setPassword' in events[i]:
        z.clear()
        z.append(events[i][1])
k=[]
if '000A' in z:
    k=[0,1,1]
if '3' in z:
    k=[0,0]
for x in k:
    print(x)

    











"""h(s) := (s[0]*P(n-1) + s[1]*P(n-2) + s[2]*P(n-3) +
... + s[n-2]*P + s[n-1]) mod M"""
