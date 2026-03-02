print("Hello World")
print("\n")

# By default python have sep and end parameter
print("Hello")
print("World")
print("\n")

#By default python contain end = "\n"
print("Hello", end = "_")
print("World")
print("\n")

#By default python contain sep = " "
print("Welcome", "Everyone")
print('\n')

print("Placement", "2027", sep="_", end = "#")
print("\n")

#Variable
a = 10
print(a)
print(type(a))
print("\n")


a = "Balance"
print(a)
print(type(a))
print("\n")

a = 10.4
print(a)
print(type(a))
print("\n")

#Arithmetic operator
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print("\n")

#Comparision Operator
print(a >= b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a < b)
print("\n")

#Assignment Operator
# =, +=, *=, /=, %=, //=, **=


#Logical Operator
print(a > 8 and b > 4)
print(a < 8 or b > 4)
print(not(a))
print("\n")

#Bitwise operator
print(21 | 17)
print(21 & 17)
print(21 ^ 17)
print(~10)
print(7 << 2)
print(32 >> 2)
print("\n")

#Membership Operator (in, not in)
stmt = "Balance Yourself is important"
print("Balance" in stmt)
print("You" not in stmt)
print("\n")


# Identity Operator(is, is not)
s1 = [10,20,30,40]
s2 = [10,20,30,40]
s3 = s1
print(s1 is s2) #here check address both s1 and s2 have different address
print(s1 is not s2)
