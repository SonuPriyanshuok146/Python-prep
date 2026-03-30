#Recursion : Whenever a function calls itself.

# def fun(n):
#     if n > 0:
#         print(n)
#         fun(n-1)
# fun(5)



# def fun(n):
#     if n == 0:
#         return
#     print("Entering: ", n)
#     fun(n-1)
#     print("Exit: ", n)
# fun(3)


# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)

# fun(5)






# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*fact(n-1)
# a = int(input("ENter number that you want to calculate factorial: "))
# result = fact(a)
# print(f"factorial of {a}: {result}")




# def sumN(n):
#     if n == 0:
#         return 0
#     return n + sumN(n-1)

# n = int(input("Enter n to sum upto n: "))
# result = sumN(n)
# print(f"Sum upto {n} is {result}")





#count number of digits in a number using recursion
# def digitCount(data):
#     if data == 0:
#         return 0
#     return 1 + digitCount(data//10)
# val = digitCount(2345)
# print(val)






#print fibonacci number using recursion
# def fibN(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibN(n-1) + fibN(n-2)

# print(fibN(5))

# def fibN(n):
#     if n <= 1:
#         return n
#     return fibN(n-1) + fibN(n-2)

# print(fibN(5))







#practice: tail recursion
# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n-1)
# fun(5)






#practice: head recursion
# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n)
# fun(5)





#Reverse a number using recursion
# def revN(n):
#     if n == 0:
#         return 0
#     q = n % 10
#     return q * (10 ** (len(str(n)) - 1)) + revN(n // 10)

# print(revN(2345))


def revnum(n, rev = 0):
    if n == 0:
        return rev
    return revnum(n // 10, rev*10 + n % 10)
print(revnum(7429))
