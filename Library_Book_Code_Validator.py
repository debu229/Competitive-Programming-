import re

code = input("Enter book code: ")

pattern = r'^[A-Z]{3}-[0-9]{4}-[0-9]{3}$'

if re.fullmatch(pattern, code):
    print("Valid Book Code")
else:
    print("Invalid Book Code")