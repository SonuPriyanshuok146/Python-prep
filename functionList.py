#longest length of consecutive 1's
def longestOne(l1):
    lenn = 0
    curr = 0
    for num in l1:
        if num == 1:
            curr += 1
            lenn = max(lenn, curr)
        else:
            curr = 0
    return lenn

print(longestOne([1,1,0,1,1,1]))





#move zeroes at the end of the list
# def zeroEnd(l1):
#     l2 = []
#     for i in range(len(l1)):
#         if l1[i] != 0:
#             l2 = l2 + [l1[i]]
#         else:
#             continue
#     n = len(l1)
#     m = len(l2)
#     for i in range(m, n):
#         l2.append(0)
#     return l2

# print(zeroEnd([7,0,9,0,0,1,2]))



# def zeroEnd(l1):
#     n = len(l1)
#     pos = 0
#     for num in l1:
#         if num != 0:
#             l1[pos] = num
#             pos += 1
#     while pos < n:
#         l1[pos] = 0
#         pos += 1
#     return l1

# print(zeroEnd([7,0,9,0,0,1,2]))




#whether the given list is sorted or not?
# def is_sorted(l1):
#     for i in range(0, len(l1)-1):
#         if l1[i+1] < l1[i]:
#             return False
#         else:
#             continue
#     return True
# print(is_sorted([23,45,89,99]))





#print missing number
# def missing(l1):
#     currSum = 0
#     for num in l1:
#         currSum += num
#     n = len(l1)
#     missing = (n*(n+1)/2) - currSum
#     return missing
# print(missing([0,1,2,3,4,6,7,8]))





#you have a number in list format, and you have to add one in it.
# def sum1list(l1):
#     n = len(l1)
#     for i in range(n-1, -1, -1):
#         if l1[i] != 9:
#             l1[i] += 1
#             return l1
#         l1[i] = 0
#     return [1] + l1
    
# print(sum1list([1,9,9]))





#print sum of all element of list
# def sumele(l1):
#     sum = 0
#     for num in l1:
#         sum += num
#     return sum
# print(sumele([1,2,3,4,5]))





#print maximum element of the list

# def maxele(l1):
#     current = l1[0]
#     for i in l1:
#         if i > current:
#             current = i
#     return current

# l1 = [23,67,45,65]
# maxElement = maxele(l1)
# print(maxElement)