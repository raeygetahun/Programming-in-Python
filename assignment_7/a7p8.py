def push(lst,elem):
    lst.append(elem)
    return lst

def pop(lst):
    lst.pop(-1)
    return lst
    
def empty(lst):
    return []
stack = [1, 2, 3, 4, 5]
print(stack)
stack=push(stack,6)
print(stack)
stack=pop(stack)
print(stack)
stack=empty(stack)
print(stack)