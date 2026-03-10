#reduce
from functools import reduce

l1 = [1, 2, 3, 4, 5]
a = reduce(lambda x, y: x + y, l1)

print(a)





# #map
# l1 = [1, 2, 3, 4, 5]
# a = list(map(lambda x: x**2, l1))
# print(a)


#filter
# l1 = [9, 7, 6, 12, 20, 4, 3, 15]
# a = list(filter(lambda x: x > 10, l1))
# print(a)
# b = list(filter(lambda x: x%2 == 0, l1))
# print(b)


#lambda function
# a = lambda x,y,z: x+y+z

# print(a(2,3,4))





# def multiplier(factor):
#     def mulitply_by(x):
#         return factor*x
#     return mulitply_by
# a = multiplier(3)
# print(a(7))




# def outer():
#     a = 10
#     b = 20
#     def inner():
#         print(a, b)
#     inner()
        
# outer()





#global variable
# a = 100
# def fun():
#     print(a)
    
# fun()
# print(a)

# a = 100
# def fun():
#     global a
#     a = a+50
    
# fun()
# print(a)


#local variable
# def fun():
#     a = 10
#     print(a)
    
# fun() //10
# print(a) //it give error




#default arguments
# def fun(a, b = 2):
#     print(a, b)
    
# fun(1)
# fun(1, 3)




# def fun(*a, **b):
#     print(a)
#     print(b)
    
# fun(10, 20, x=15, y=20)



# #To pass any number of Keywords arguments
# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
    
# fun(age=26,desig="Data Scientist", name="Ravi")





#Keyword Arguments
# def profile(name, age, desig):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Designation: ", desig)
    
# profile(age=26,desig="Data Scientist", name="Ravi")




# def fun(*args):
#     print(args)
#     print(type(args))
    
# fun("Ravi", 26, "Data Scientist")




# def addNo(x, y):
#     return x+y

# c = addNo(2, 3)
# print(c)

# def fun():
#     print("I Love Python")
    
# c = fun() #I Love Python
# print(c)  #None

# def profile(name, age, desig):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Designation: ", desig)
    
# profile("Sonu", 26, "Data Scientist")

