import re

file_name = input("")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        email_addresses = re.findall(r"\b[A-Za-z]+\.[A-Za-z]+@jacobs-university\.de\b", content)
        if email_addresses:
            print("Email addresses found:")
            for email in email_addresses:
                print(email)
        else:
            print("cant find")
except FileNotFoundError:
    print("enter a valid file name.")
