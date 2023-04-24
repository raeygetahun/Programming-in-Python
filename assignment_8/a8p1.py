start=int(input())
end=int(input())

step=int(input())

print("inch     cm")
for i in range(start,end+1,step):
    print("{:.1f}\t{:.1f}".format(i, i*2.54))
