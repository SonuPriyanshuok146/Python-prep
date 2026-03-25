#input: "I love programming"
#output: "programming love I"
# s1 = "I love programming"
# a = s1.split()
# b = a[::-1]
# c = " ".join(b)
# print(c)


# s1 = "I love programming"
# def rev(s1):
#     c = " ".join(s1.split()[::-1])
#     return c
# x = rev("I love programming")
# print(x)

    




#print all substrings of a string
# s1 = "abc"
# for i in range(len(s1)):
#     for j in range(i+1, len(s1)+1):
#         print(s1[i:j])




#print the longest word in a string
# s1 = "I am preparing for placements"
# a = s1.split()
# largest = a[0]

# for item in a:
#     if len(item) > len(largest):
#         largest = item
# print(largest)






#Print the freq of each character
# s1 = "aabbcdafabx"
# freq = {}
# for ch in s1:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)





#check whether two strings are anagram or not?
# s1 = "listen"
# s2 = "tsilen"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not a anagram")






#Print first non repeating character
# s1 = "aaabbcced"
# for i in s1:
#     if s1.count(i) == 1:
#         print(i)
#         break





#Remove duplicate character
# s1 = "hello"
# s2 = ""
# for i in s1:
#     if i not in s2:
#         s2 += i
# print(s2)





#Count vowel and consonent
# a = "hello 2027"
# vowelCount = 0
# consonentCount = 0
# vowels = "aeiouAEIOU"
# for i in a:
#     if i.isalpha():
#         if i in vowels:
#             vowelCount += 1
#         else:
#             consonentCount += 1
# print(f"count of vowel = {vowelCount}")
# print(f"count of Consonent = {consonentCount}")




#Palindrome
# a = "abba"
# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome!")


def palindrome(a):
    if a == a[::-1]:
        return "Palindrome"
    return "Not Palindrome"
x = palindrome("abba")
print(x)




#Reverse string
# a = "hello"
# print(a[::-1])