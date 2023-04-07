ch=input()

while(not ch.isupper()):
    ch=input("Uppercase only try again: ")


n=int(input())

while(n<0 or n>32):
    n=int(input("try again : "))

for i in range(n):
    print(chr(ord(ch)+i),end='')