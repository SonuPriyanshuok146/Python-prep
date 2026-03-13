n = int(input("Enter number n: "))
num = 1
for i in range(n,0,-1):
    for j in range(1, i+1):
        if i==j or i == n or j == 1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()






#Hollow right angle triangle
# n = int(input("Enter number n: "))
# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if i == j or i == n or j == 1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()






#Floyd's triangle
# n = int(input("Enter number n: "))
# num = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()



#print patter in number
# n = int(input("Enter number n: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()




#Inverted pyramid pattern
# n = int(input("Enter number of rows: "))

# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end="   ")
#     print()






#pyramid pattern
# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end="   ")
#     print()




#Inverted right angle triangle
# n = int(input("Enter number of rows: "))

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




#right angle triangle
# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




#Rectangle
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# for i in range(rows):
#     for j in range(cols):
#         print("*", end=" ")
#     print()




#print hollow square
# n = int(input("Enter size of row(or Column): "))

# for i in range(n):
#     for j in range(n):
#         if(i == 0 or i == n-1 or j == 0 or j == n-1):
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()



#Print plain square with *
# n = int(input("Enter size of row(or Column): "))

# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()