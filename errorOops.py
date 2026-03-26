#Polymorphism
class Animal:
    def sound(self):
        print("Hello")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("meow")

def get_sound(Animal):
    Animal.sound()
get_sound(Dog())
get_sound(Cat())

        





#Inheritence
# class A:
#     def eat(self):
#         print("Eating")
# class B:
#     def sleep(self):
#         print("Sleeping")
# obj1 = A()
# obj2 = B()
# obj1.eat()


# class A:
#     def eat(self):
#         print("Eating")
# class B(A):
#     def sleep(self):
#         print("Sleeping")
# obj1 = A()
# obj2 = B()
# obj2.eat()




#Encapsulation
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def withdraw(self, amount):
#         self.balance -= amount
#     def deposit(self, amount):
#         self.balance += amount
#     def display(self):
#         print(self.balance)
# b1 = BankAccount(500)
# b2 = BankAccount(1000)
# b3 = BankAccount(100)
# b1.deposit(500)
# b1.withdraw(200)
# b1.display()





#class
# class student:
#     def __init__(self, name, rollno, cls):
#         self.name = name
#         self.rollno = rollno
#         self.cls = cls
# stud1 = student("Deb", "123", "10")
# stud2 = student("Sumit","491", "12")
# print(stud1.name)






#try except else finally
# try:
#     a = int(input("Enter number: "))
#     c = 10/a
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("Elese block")
# finally:
#     print("Finally")





#try finally
# try:
#     a = int(input("Enter number:"))
#     c = 10/a
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("Hello")





#try exception
# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     c = a/b
# except Exception as e:
#     print(e)
# print(a+b)
# print(a*b)


# try:
#     l1 = [10, 20, 30, 40]
#     num = int(input("Enter number:"))
#     i = l1.index(num)
#     print(i)
#     print(num/i)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except ValueError:
#     print("Value Error")
# except Exception as e:
#     print(e)





#Exception Handling
# a = 10
# b = 0
# print(a+b)
# print(a/b)
# print(a-b)




#Index Error
# l1 = [10, 20, 30]
# print(l1[7])





#Attribute Error
# s = "hello"
# s.reverse()




#Name Error
# print(a)




#ZeroDivision Error
# a = 10
# b = 0
# c = a/b





#Value Error
# a,b = 1,2,3,4
# num = int("abcd")
# l1 = [10,20,30]
# a = l1.index(100)



#Type Error
# a = 1
# b = "2"
# c = a + b




#Indentation Error
# a = 10
# b = 20
# if a > b:
# print("Hello")




#Syntax Error
# print("Hello"