from collections import deque
from module_queue import Queue 


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
