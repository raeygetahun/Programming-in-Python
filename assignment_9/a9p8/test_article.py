from article import Article

n=int(input())


a=Article("try","28.04.2023","nothing",1,15)
b=Article("try2","28.04.2023","something",2,18)


lst=[]

for i in range(n):
    name=input("Name: ")
    date=input("date: ")
    about=input("about: ")
    number=int(input("number: "))
    price=float(input("price: "))
    temp=Article(name,date,about,number,price)
    lst.append(temp)
    
for elem in lst:
    print("hello")
    print(elem)
    