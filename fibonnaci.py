def fibonacci(n):
if n == 0 or n == 1:
return n else:
return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number of Fibonacci numbers to generate: "))
for i in range(n):
print(fibonacci(i), end=' ')
print("\nThe", n, "th Fibonacci number is:", fibonacci(n-1))