#You have a list. to find the greatest number

l1 = [10, 4, 19, 11, 23]
largest = l1[0]
for i in range(1, len(l1)):
    if l1[i] > largest:
        largest = l1[i]
print("Largest number in list:",largest)




# l1 = [10, 4, 19, 11, 23]
# largest = l1[0]
# for i in l1:
#     curr = i
#     if curr > largest:
#         largest = curr
        
# print("Largest number in list:",largest)
    





#take input from user, check whether its palindrome or not.

# num = int(input("Enter the integer: "))
# rev_num = 0
# val = num
# while num != 0:
#     q = num % 10
#     rev_num = rev_num*10 + q
#     num //= 10
  
# if val == rev_num:  
#     print("Palindrome number.")
# else:
#     print("Not a Palindrome number.")






#Take a input from user(number) and print the reverse of it.

# num = int(input("Enter the integer: "))
# rev_num = 0
# while num != 0:
#     q = num % 10
#     rev_num = rev_num*10 + q
#     num //= 10
    
# print("Reverse of num:",rev_num)