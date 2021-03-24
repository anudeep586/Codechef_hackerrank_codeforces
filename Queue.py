from collections import deque
class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,data):
        self.buffer.appendleft(data)
    def dequeue(self):
        self.buffer.pop()
    def peek(self):
        print(self.buffer[-1])
if __name__=="__main__":
    Q=Queue()
    length=int(input())
    for i in range(length):
        arr=list(map(int,input().rstrip().split()))
        if arr[0]==1:
            Q.enqueue(arr[1])
        elif arr[0]==2:
            Q.dequeue()
        elif arr[0]==3:
            Q.peek()
            
        
