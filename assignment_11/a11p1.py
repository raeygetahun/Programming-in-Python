while True:
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            break
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission.")
    except IOError as e:
        print("Error: ", e)