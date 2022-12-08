# Program to print addition of first n odd numbers

n = int(input("Enter the number :\n"))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum += i
print(f"Sum of first {n} even numbers is:\n", sum)