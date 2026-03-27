#iterator
# lst = [10, 20, 30]
# for a in lst:
#     print(a)

# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))


# l1 = [1,2,3]
# a = iter(l1)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# class NewIterator:
#     def __init__(self, maxValue):
#         self.maxValue = maxValue
#         self.current = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= self.maxValue:
#             val = self.current
#             self.current += 1
#             return val
#         else:
#             raise StopIteration
# obj = NewIterator(5)
# for i in obj:
#     print(i)



# class NewRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         val = self.start
#         self.start += 1
#         return val

# obj = NewRange(2, 5)
# for a in obj:
#     print(a)



# class Revlist:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
# obj = Revlist([10, 20, 30])
# for i in obj:
#     print(i)



#Fibonacci iterator
# class fibonacci:
#     def __init__(self, n):
#         self.n = n
#         self.a = 0
#         self.b = 1
#         self.count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count >= self.n:
#             raise StopIteration
#         val = self.a
#         self.a, self.b = self.b, self.a + self.b
#         self.count += 1
#         return val
# obj = fibonacci(5)
# for i in obj:
#     print(i)




#Generator

# def mygen():
#     yield 1
#     yield 2
#     yield 3
# obj = mygen()
# print(next(obj))
# print(next(obj))
# print(next(obj))


#fibonacci Generator
# def fib(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         yield a
#         a, b = b, a+b

# print(list(fib(5)))




#Even number generator
# def evenNum(n):
#     for i in range(n):
#         if i%2 == 0:
#             yield i
            
# print(list(evenNum(10)))


#generator for square
def squareNum(n):
    for i in range(n+1):
        yield i*i
        
print(list(squareNum(5)))