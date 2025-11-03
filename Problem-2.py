n = int(input("Enter a number: "))
series = []

for i in range(1, n * 2, 2):
    series.append(i)

print(", ".join(map(str, series)))
