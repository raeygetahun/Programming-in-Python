def overlapping(list1,lst2):
    for elem in list1:
        if elem in lst2:
            return True
    return False

lst1 = []
lst2 = []
while True:
    temp = int(input())
    if temp < 0:
        break
    lst1.append(temp)


lst2 = []
while True:
    temp = int(input())
    if temp < 0:
        break
    lst2.append(temp)


if overlapping(lst1, lst2):
    print("The two lists are overlapping.")
else:
    print("The two lists are not overlapping.")