def histogram(lst):
    for elem in lst:
        print("*"*elem)
        
        
n=int(input())
lst=[]

for i in range(n):
    temp=int(input())
    lst.append(temp)
    
    
histogram(lst)