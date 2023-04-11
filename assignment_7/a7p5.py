tu=()

while True:
    temp=int(input())
    if temp<0:
        break;
    tu+=(temp,)
    
reversed_tu = tu[::-1]

print(reversed_tu)

