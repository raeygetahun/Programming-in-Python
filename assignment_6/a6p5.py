def multiply(lst,val):
    return [elem*val for elem in lst]

def add(lst,val):
    return[elem+val for elem in lst]

n=int(input())
lst=[]

for i in range(n):
    temp=int(input())
    lst.append(temp)
    
print(lst)
print(multiply(lst,5))
print(add(lst,1.5))

