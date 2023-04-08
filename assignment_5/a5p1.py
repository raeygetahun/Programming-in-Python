ltr=float(input())
gal=float(input())

def to_liter(galllon, cup):
    return galllon*3.7854 + cup*0.2366

print(to_liter(gal,ltr))