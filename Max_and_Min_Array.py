n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

maximum = max(arr)
minimum = min(arr)

print("Maximum element:", maximum)
print("Minimum element:", minimum)