n=int(input())
m=int(input())
c=input()

def print_rectangle(n, m, c):
    for i in range(n):
        for j in range(m):
            print(c,end="")
        print()

print_rectangle(n,m,c)