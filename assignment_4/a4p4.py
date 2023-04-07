arr=[]

for i in range(10):
    temp=int(input())
    if temp==-9:
        break
    arr.append(temp)


total=sum(arr)
avg=total/len(arr)

print("The average is",int(avg))