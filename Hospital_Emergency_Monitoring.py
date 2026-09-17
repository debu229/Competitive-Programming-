n = int(input("Enter number of hours: "))

patients = []
for i in range(n):
    x = int(input("Enter patients: "))
    patients.append(x)

maximum = max(patients)
minimum = min(patients)
peak_hour = patients.index(maximum) + 1
average = sum(patients) / n

above_average = 0
for x in patients:
    if x > average:
        above_average += 1

print("Maximum patients:", maximum)
print("Hour of maximum:", peak_hour)
print("Minimum patients:", minimum)
print("Peak hour:", peak_hour)
print("Average patients:", average)
print("Hours above average:", above_average)