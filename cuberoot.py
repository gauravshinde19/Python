# Program to print cube root of a given number

n = int(input("Enter the perfect cube number :\n"))
for i in range(1, n+1):
    if n % i == 0:
        if n == i * i * i:
            print(f"Cube root of {n} is {i}")
            break
else:
    print("This is not perfect cube number")