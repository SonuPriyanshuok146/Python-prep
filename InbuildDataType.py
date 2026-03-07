#Inbuilt data structure

#dictionary
# d1 = {'a':1, 'b':2, 'c':4}
# print(d1['b'])

players = {'Samson': 97, 'Tilak': 25, 'Hardik': 89}
# for i in players.keys():
#     print(i)

# for i in players.values():
#     print(i)

# for i in players.items(): #it give key value pairs
#     print(i)

students = {'Ravi', 'Aditya', 'Neha'}
# d2 = dict.fromkeys(students)
# print(d2)

d3 = dict.fromkeys(students, 0)
# print(d3)











#frozenSet
# s1 = frozenset({1, 2, 3, 4})

# s2 = frozenset({3, 5, 8})
# a = s1.union(s2)
# b = s1.difference(s2)
# c = s1.intersection(s2)
# d = s1.isdisjoint(s2)
# print(a)
# print(b)
# print(c)
# print(d)








#Set
# s1 = {10, 7.4, "Hello", 15}
# s1.remove(7.4)
# s1.update({7.4,23})

# s2 = {3, 5, 8}
# a = s1.union(s2)
# b = s1.difference(s2)
# c = s1.intersection(s2)
# d = s1.isdisjoint(s2)
# print(a)
# print(b)
# print(c)
# print(d)










#tuple
# t1 = (10, 17.4, 81, 100, 41.3)
# print(type(t1))
# print(t1[3])
# print(t1[-5])
# t1[1] = "hello" # it through error due to tuple is immutable
# print(t1)

# print(t1[2:4])










#list
# a = [10, 17.4, "hello", 61]
# print(type(a))
# print(a[2]) #Access
# print(a[-3]) #Access
# a[0] = 70 #Modify
# print(a)
# print(a[1:3])

# print(a[: : -1])

# l1 = [10, 20, 30, 40]
# l1.append(90)
# print(l1)
# l1.insert(1, 50)
# print(l1)

# l1.remove(20)
# print(l1)

# l1.clear()
# print(l1)
# del l1[:]
# print(l1)

# del l1[1]
# print(l1)

# l1.pop()
# print(l1)





#slicing
# str1 = "Hello world"
# print(str1[2:6])
# print(str1[2:])
# print(str1[:4])
# print(str1[2:-6])

# print(str1[10: -11: 1])
# print(str1[:])
# print(str1[2: 9: 2])

#Reversal of string
# print(str1[: :-1])

#lower upper
# a = str1.upper()
# print(a)

# a = str1.lower()
# print(a)

# str2 = "I love Python."
# a = str2.replace("Python", "Java")
# print(a)






#string
# str1 = "Hello"
# str2 = "Hello"

# print(type(str2))
# print(str1[2])
# print(str1[-1])

# print(str1[0])



#imaginary
# a = complex(3, 4)
# print(a.real)
# print(a.imag)



#int

# a = 10
# print(id(a))

# a = 4
# print(id(a))