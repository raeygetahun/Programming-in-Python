input=int(input())

for i in range(1,input+1):
    for j in range(i):
        print(chr(65+j),end='')
    print()    
    