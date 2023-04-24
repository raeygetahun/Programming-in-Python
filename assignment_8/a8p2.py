start=int(input())
end=int(input())

step=int(input())

f = open("table.txt", "w")

f.write("inch\tcm\tm\tkm")
for i in range(start,end+1,step):
    f.write("\n")
    f.write("{:.1f}\t{:.1f}\t{:.4f}\t{:.7f}".format(i, i*2.54,i*0.024,i*0.000024))
