finput=open('numbers.txt','r')

numbers = [int(line) for line in finput]

sum  = sum(numbers)
    
print(sum)