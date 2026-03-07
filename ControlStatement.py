#match-case
# day = "monday"
# match day:
#     case "sunday":
#         print("Weekend")
#     case "monday":
#         print("week day")
#     case __:
#         print("Other day.")

# x = 10
# match x:
#     case x if x > 0:
#         print("Positive Number.")
#     case x if x < 0:
#         print("Negative Number.")
#     case x if x == 0:
#         print("Zero")


food = "apple"
match food:
    case "apple" | "orange":
        print("Fruit")
    case __:
        print("Vegitable.")

        





#else in loop
# l1 = [10, 20, 30]
# for item in l1:
#     if item > 30:
#         break
#     print(item)
# else:
#     print("hello")




#pass
# l1 = [10, 20, 30]
# for item in l1:
#     if item > 20:
#         pass
#     print(item)
    




#continue
# l1 = [10, -5, -7, 11, 12, 13,-14]
# total_sum = 0
# for item in l1:
#     if item < 0:
#         continue
#     total_sum += item
# print(total_sum)




#break

# l1 = [6, 71, 4, 19, 32, 51, 64]
# total_sum = 0
# for item in l1:
#     total_sum += item
#     if total_sum > 100:
#         break
#     print(total_sum)





#While

# l1 = [10, 20, 30, 40]
# i = 0
# n = len(l1)
# while i < n:
#     print(l1[i])
#     i = i+1





#Nested loop
# players = [["Samson", "Bumra"], ["ponting","Stark"], ["Millin", "Bavnma"]];
# # for i in players:
# #     print(i)

# for a in players:
#     for b in a:
#         print(b)


#enumerate()

# l1 = [10, 20, 30, 40]
# for i, v in enumerate(l1):
#     print(i, v)



#Loops

# for item in l1:
#     print(item)

# for i in range(len(l1)):
#     print(l1[i])
    

# for i in range(0, 51, 2):
#     print(i)

# for i in range(2, 6, 2):
#     print(i)


# for i in range(2, 6):
#     print(i)

# for i in range(5):
#     print(i)


# route = ["Wakeup", "Breakfast", "Study", "Revision", "Sleep"]

# for item in route:
#     print(item)





#Nested if

# Score = int(input("Enter Score: "))
# if Score > 90:
#     if Score >= 100:
#         print("Century.")
#     else:
#         print("Hard Luck.")
# else:
#     print("Better Play next time.")





#elif

# marks = int(input("Enter marks:"))
# if marks > 90:
#     print("A1")
# elif marks > 80:
#     print("A2")
# elif marks > 70:
#     print("B1")
# else:
#     print("Other Grade.")



# num2 = 18
# if num2 > 10:
#     print("Number greater than 10.")




# num1 = 20
# if num1%2 == 0:
#     print("Even Number.")
# else:
#     print("Odd Number.")


# marks = int(input("Enter marks: "))

# if marks > 70:
#     print("Good Student.")
# else:
#     print("Work Hard!") 