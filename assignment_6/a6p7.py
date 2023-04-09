lst=[]

while True:
    temp=int(input())
    if(temp==0):
        break;
    
    lst.append(temp)
    
print('min',min(lst))
print('max',max(lst))