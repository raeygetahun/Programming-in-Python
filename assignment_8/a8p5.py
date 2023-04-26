from collections import deque

class Queue:
    def __init__(self,lst=None):
        if lst is None:
            self.lst = []
        else:
            self.lst = lst
    
    def enqueue(self,elem):
        self.lst.append(elem)
        
    def dequeue(self):
        if self.lst:
            return self.lst.pop(0)
        
    def printq(self):
        print(self.lst)
        

list_queue= Queue()
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
list_queue.enqueue("Terry")
queue.append("Graham")          # Graham arrives
list_queue.enqueue("Graham")
print(queue.popleft())                 # The first to arrive now leaves
print("from list",list_queue.dequeue())
print(queue.popleft())                 # The second to arrive now leaves
print("from list",list_queue.dequeue())
