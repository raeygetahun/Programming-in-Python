finput=open('input.txt','r')
foutput=open('output.txt','w')

line=finput.readline()

product=ord(line[0])*ord(line[1])

foutput.write(str(product))