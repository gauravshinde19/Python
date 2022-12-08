# Program to print addition of first n numbers

n = int(input("Enter the number :\n"))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"Sum of first {n} numbers is:\n",sum)
