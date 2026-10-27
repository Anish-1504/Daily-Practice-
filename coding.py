"""
largest = int(input("Enter number 1: "))

for i in range(2, 6):
    num = int(input(f"Enter number {i}: "))

    if num > largest:
        largest = num

print("Largest number is:", largest)
"""

num = int(input("Enter a num: "))

for i in range(1, num+1):
    if i <= 0 :
        print("Not Prime")
    else :
        if i >= 1 and num // i == 0:
            print("Prime")