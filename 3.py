n = int(input("Enter how many numbers you want to enter "))
i = 0
sum = 0
while i < n:
    a = int(input(f"Enter number {i+1}: "))
    sum= sum + a
    i += 1
print("Total sum:", sum)