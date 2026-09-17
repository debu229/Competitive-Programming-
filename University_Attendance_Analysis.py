n = int(input("Enter number of students: "))

attendance = []
for i in range(n):
    x = float(input("Enter attendance: "))
    attendance.append(x)

threshold = float(input("Enter attendance threshold: "))

# Students below threshold
count = 0
for x in attendance:
    if x < threshold:
        count += 1

# Lowest attendance and position
lowest = min(attendance)
position = attendance.index(lowest) + 1

# Average
average = sum(attendance) / n

print("Students below threshold:", count)
print("Lowest attendance:", lowest)
print("Position:", position)
print("Average attendance:", average)