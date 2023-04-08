import random
random . seed ()
minval = 1
maxval = 50
r = random . randint ( minval , maxval )
count=0
while True :
    guess = int( input (" Enter your guess : ") )
    count+=1
    if r == guess :
        print ("You got it in",count,"tries")
        break
    elif guess < r :
        print (" Your guess is too small !",count,"tries so far")
    else :
        print (" Your guess is too high !",count,"tries so far")
    print ("Bye")
