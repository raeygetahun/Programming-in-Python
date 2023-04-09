name=input()

finput=open(name,'r')


for line in finput:
    words=line.split()
    count=len(words)
    print(count)