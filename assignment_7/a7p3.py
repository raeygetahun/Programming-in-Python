
def product(v,w):
    sum=0
    for i in range(len(v)):
        sum+=v[i]*w[i]
        
    return sum

n=int(input())
lst1=[]
lst2=[]

for i in range(n):
    temp=float(input())
    lst1.append(temp)
    
    
for i in range(n):
    temp=float(input())
    lst2.append(temp)
    
tuple1=tuple(lst1)
tuple2=tuple(lst2)

print(product(tuple1,tuple2))
    
    