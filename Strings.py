#  All about strings
# str is immutable 

str12 = "Rahul Bharadia"
str2 = "Hello"
fruits = "Apple"

print(type(str12)) #class str

# concatenation
print(str2 + " " + str12) # Hello Rahul Bharadia

# length of str
print(len(str12))  # 14

# indexing
# index number start from 0 ( L To R)
# index number start from -1 ( R To L)

print(str12[0]) # R accesing element from index number
#  str1[0] = R # cannot change the error and throws error

# print(str12[0:5]) # slicing 0 (start point) is included and 5 is excluded (end point)

# Negative indexing

print(fruits[  : :-1 ]) #reverse the str
print(fruits[  -5: -2 ]) # -5 is the starting point and -2 is the ending point
