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