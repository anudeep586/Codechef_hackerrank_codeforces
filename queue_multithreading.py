import time
import threading
from collections import deque
q=deque()
def take_orders(orders):
    for i in orders:
        time.sleep(0.5)
        q.appendleft(i)
def serve_orders(orders):
    a=q.pop()
    time.sleep(2)
    print(a)

if __name__=="__main__":
    orders=['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=take_orders,args=(orders,))
    t2=threading.Thread(target=serve_orders,args=(orders,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")
