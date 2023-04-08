import math

r=float(input())

def volume(radius):
    return math.pi * radius**3 * 4/3

print(volume(r))