n = int(input("Enter a number: "))

if n % 2 == 0:
    n -= 1  # for even, use previous odd count

series = [i for i in range(1, n * 2, 2)]
print(", ".join(map(str, series)))
