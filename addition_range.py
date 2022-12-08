# Program to print addition of numbers between range given by user

n1 = int(input("Enter the first number :\n"))
n2 = int(input("Enter the second number :\n"))
sum = 0
for i in range(n1, n2+1):
    sum += i
print(f"Sum of numbers between {n1} to {n2} is:\n",sum)
