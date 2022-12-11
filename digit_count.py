# Program to print count of digits in a number

n = int(input("Enter the number :\n"))
c = 0
while n > 0:
    c += 1
    n = n // 10
print("Number of digits :\n", c)
