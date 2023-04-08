str=input()

while True:
    a=int(input())
    b=int(input())
    
    if a>len(str) or b>len(str) or a>b: 
        print("invalid input")
    else:
        print(str[a:b+1])
        break