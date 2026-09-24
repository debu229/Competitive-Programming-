n = int(input("Enter number of students: "))

names = []
for i in range(n):
    name = input("Enter student name: ")
    names.append(name)

search = input("Enter name to search: ")

if search in names:
    print("Case-sensitive: Student found at position", names.index(search) + 1)
else:
    print("Case-sensitive: Student not found")

found = False

for i in range(n):
    if names[i].lower() == search.lower():
        print("Case-insensitive: Student found at position", i + 1)
        found = True
        break

if not found:
    print("Case-insensitive: Student not found")
