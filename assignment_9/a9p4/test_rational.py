from rational import Rational

num=int(input())
den=int(input())

a=Rational(num,den)

num=int(input())
den=int(input())

b=Rational(num,den)

print(a.numerator(),b.numerator())
print(a.denominator(),b.denominator())

c=a.__add__(b)
print(c)