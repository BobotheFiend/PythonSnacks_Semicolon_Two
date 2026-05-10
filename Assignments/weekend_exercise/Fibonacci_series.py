number = 20
first = 0
second = 1

print(f"Fibonacci sequence: ");

for count in range (2, 20+1):
    next = first + second
    print(next,end=" + ")
    first = second
    second = next

print(f"\nThe first twenty fibonacci series = {next}")
