# Find the largest of three numbers
a, b, c = map(int, input("Enter three numbers: ").split())
print("Largest number is:", max(a, b, c))

# Print the first 10 Fibonacci numbers
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print(fibonacci(10))

# Generate a multiplication table for a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")