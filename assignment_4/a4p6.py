n=int(input())
m=int(input())
c=input()

def print_frame(n,m,c):
    for i in range(n):
        for j in range(m):
            if i==0 or i==n-1 or j==0 or j==m-1:
                print(c,end="")
            else:
                print(" ",end="")
                
        print()


print_frame(n,m,c)