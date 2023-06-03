filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        num1, num2 = map(int, file.readline().split())
        result = num1 / num2
    with open("division.txt", 'w') as file:
        file.write(str(result))
    print("Division result has been written to division.txt.")

except FileNotFoundError:
    print("File not found. Please enter a valid filename.")
except ValueError:
    print("Invalid file format. File should contain two integers separated by a space.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
