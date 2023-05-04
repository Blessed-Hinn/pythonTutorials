# Lists
"""
first_Container = [34, 89, "Weeknd", 89, "Die for you", True]
print(first_Container)
first, *other, last = first_Container  # Swapping using asterisk
first_Container = [last, *other, first]  # Swapping using asterisk
print(first_Container)  # Print the swapped list
print(*other)
print(last)
print(first_Container)
first_Container.append("StarBoy")
print(first_Container)
first_Container[0], first_Container[-1] = first_Container[-1], first_Container[0]  # Swapping using indices
print(first_Container)
first_Container.append(["Kodak Black", "Zeze", 10])  # Adding data
print(first_Container)

first_Container.pop()
print(first_Container)
"""

"""
# Swapping content
temp = first_Container[0]
first_Container[0] = first_Container[3]
first_Container[3] = temp
print(first_Container)
first_Container[0], first_Container[3] = first_Container[3], first_Container[0]
print(first_Container)

zeros = [[0,1]] * 4
print(zeros)
"""

"""
numerals = list(range(20))
print(numerals)
print(numerals[3])
print(len(numerals))
print(numerals[::-1])
numerals.insert(2, 89)
print(numerals)
print(len(numerals))
numerals.append(89)
print(numerals)
numerals.remove(89)
print(numerals)
# alphabets = list("Hello World")
# print(alphabets)
# print(len(zeros))
"""

# numerals = list("Hello World")
# print(numerals)

# Tuples