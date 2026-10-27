# 1. Right angled Triangle
'''
rows = int(input("Enter the size of Rows "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
'''

# 2. Inverted Right angled Triangle
'''
rows = int(input("enter size of Row "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
'''

# 3. Pyramid 
'''
rows = int(input("Enter the size of Rows "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=' ')
    for k in range(1, 2 * i):
        print("*", end=' ')
    print()
'''

# 4. Inverted Pyramid
'''
rows = int(input("Enter Rows "))
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=' ')
    for k in range(1, 2 * i ):
        print("*", end=' ')
    print()
'''

# 5. Diamond
'''
rows = int(input("Enter Rows"))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()

for i in range(rows, 0 , -1):
    for j in range(rows - i ):
        print(" ", end= " ")
    for j in range(1, 2* i):
        print("*", end=' ')
    print()
'''

