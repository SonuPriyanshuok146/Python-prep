#Print first occurence of a uppercase character in a string using recursion
# def firstUpper(s, index = 0):
#     if index == len(s):
#         return None
#     if s[index].isupper():
#         return s[index]
#     return firstUpper(s, index + 1)
# print(firstUpper("xyzAqB"))


def firstocc(s):
    if not s:
        return None
    if s[0].isupper():
        return s[0]
    return firstocc(s[1:])
print(firstocc("xyzAqB")) 






#Convert decimal to binary using recursion
# def decToBin(n):
#     if n == 0:
#         return ""
#     return decToBin(n//2) + str(n%2)
# print(decToBin(16))





#Convert binary number to decimal using recursion
# def binaryToDec(n, idx = 0):
#     if n == 0:
#         return 0
#     return (n%10) * pow(2 , idx) + binaryToDec(n//10, idx+1)
# print(binaryToDec(1010))






#Check if array is sorted or not using recursion
# def SortCheck(arr):
#     if len(arr) <= 1:
#         return True
#     if arr[0] > arr[1]:
#         return False
#     return SortCheck(arr[1:])
# print(SortCheck([2,3,4,5,4]))


# def SortCheck(arr, n):
#     if n == 1:
#         return True
#     if arr[n-1] < arr[n-2]:
#         return False
#     return SortCheck(arr, n-1)
# print(SortCheck([2,3,4,5], 4))





#Calculate Sum of digits in a number using recursion
# def SumDigit(n):
#     if n == 0:
#         return 0
#     return SumDigit(n//10) + (n % 10)
# print(SumDigit(1234))





#Calculate power of a number using recursion
# def powerN(n, m):
#     if(m == 1):
#         return n
#     return n*powerN(n, m-1)
# print(powerN(2, 4))






#check whether a sting is palindrome or not using recursion
# def palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrome(s[1:-1])
# print(palindrome("madam"))
    






#Reverse the string using recursion
# def revString(s):
#     if(len(s) <= 1):
#         return s
#     return revString(s[1:]) + s[0]
    
# print(revString("Hello"))
    
    