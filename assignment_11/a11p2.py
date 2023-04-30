try:
    num = int(input("Enter a number between 1 and 10: "))
    if num < 1 or num > 10:
        raise ValueError("Number is out of range!")
except ValueError as e:
    print("Error:", e)


my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[10])
except IndexError as e:
    print("Error:", e)


try:
    print("The answer is " + 42)
except TypeError as e:
    print("Error:", e)
