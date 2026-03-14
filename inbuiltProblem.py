#Merge two list into dictionary
l1 = [1, 2, 3]
l2 = ['a', 'b','c']
dictionary = dict(zip(l2,l1))
print(dictionary)




#check whether a tuple is palindrome or not
# t1 = (1, 2, 3, 2, 1)
# # print(t1[::-1] == t1)
# if t1 == t1[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




#check whether a list is a subset of other list or not
# l1 = [1, 2, 3]
# l2 = [1, 2, 3, 4, 5]
# print(set(l1).issubset(set(l2)))





# l1 = [1, 2, 3]
# l2 = [1, 2, 3, 4, 5]
# flag1 = True
# flag2 = True
# for i in range(len(l1)):
#     if l1[i] in l2:
#         continue
#     else:
#         flag1 = False
#         break
    
# for i in range(len(l1)):
#     if l1[i] in l2:
#         continue
#     else:
#         flag2 = False
#         break
# if flag1 or flag2:
#     print("list is a subset of other list.")
# else:
#     print("list is not a subset of other list")





#Rotate a list (right rotation by k)
# l1 = [1, 2, 3, 4, 5]
# k = 2
# print(l1[-k:]+l1[:-k])
    





# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# diff = abs(l1[0]-l1[1])
# for i in range(len(l1)-1):
#     curr = abs(l1[i]-l1[i+1])
#     if(curr > diff):
#         diff = curr
# print(f"Max difference between two consecutive element: {diff}")






#count odd & even elements in list
# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# evenSum = 0
# oddSum = 0
# for i in range(len(l1)):
#     if l1[i] % 2 == 0:
#         evenSum += l1[i]
#     else:
#         oddSum += l1[i]
# print(f"Even Sum in list: {evenSum}\nOdd Sum in list: {oddSum}")




#reverse a list
# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# print(l1[::-1]) #slicing


# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# l1.reverse()
# print(l1)


# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# rev = []
# for i in range(len(l1)-1, -1, -1):
#     rev.append(l1[i])
# print(rev)





#check if all element in a list are unique
# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# if len(l1) == len(set(l1)):
#     print("unique element in list present.")
# else:
#     print("Duplicate element also present.")





# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# a = list(dict.fromkeys(l1))
# print(a)





#remove duplicate element from list
# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# s = list(set(l1))
# print(s)


# l1 = [1, 2, 2, 1, 7, 3, 7, 6, 9]
# a = []
# for i in l1:
#     if i not in a:
#         a.append(i)
# print(a)




#largest element in a list
# l1 = [2, 9, 6, 4, 3, 11]
# largest = l1[0]
# for item in l1:
#     if item > largest:
#         largest = item
# print(largest)


# l1 = [2, 9, 6, 4, 3, 11]

# print(max(l1))





# n = int(input("How many value: "))
# l = []
# for i in range(n):
#     l.append(int(input("Enter element: ")))

# sum = 0

# for item in l:
#     sum += item
# print(f"Sum of item: {sum}")




# n = int(input("How many value: "))
# l = []
# for i in range(n):
#     l.append(int(input("Enter element: ")))

# print(sum(l))




# l1 = [10, 20, 30, 40, 50]

# sum = 0

# for item in l1:
#     sum += item
# print(f"Sum of item: {sum}")