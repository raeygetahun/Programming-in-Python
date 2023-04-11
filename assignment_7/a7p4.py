def remover(lst):
    return [elem for elem in lst if elem]    

lst =[('b', 'c'), (), (), ('ab'), ('a', 'b'), ('a', 'b', 'c'), ('d')] 

print(remover(lst))