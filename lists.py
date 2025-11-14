# Write a Python program to generate and print a list of the first and last 5 elements
#  where the values are square numbers between 1 and 30 (both included).
squares = [i*i for i in range(1, 31) if i*i <= 30]

first_five = squares[:5]
last_five = squares[-5:]

print( squares)

# Write a Python program to calculate the difference between the two lists.

difference = list(set(first_five) - set(last_five))
print( difference)

# Write a Python program to create a list by concatenating a given list with a range from 1 to n. 

lst = ['p', 'q']
n = 5

result = [x + str(i) for i in range(1, n+1) for x in lst]
print(result)

# Write a Python program to convert a list to a list of dictionaries.

color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = []"#000000", "#FF0000", "#800000", "#FFFF00"]

result = [{"color_name": name, "color_code": code}
          for name, code in zip(color_names, color_codes)]

print(result)

#  Write a Python program to move all zero digits to the end of a given list of numbers.

nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]


result = [x for x in nums if x != 0] + [0] * nums.count(0)

print(nums)
print(result)

# Write a Python program to round the numbers in a given list, print the minimum and maximum numbers 
# and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.

nums = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

rounded = [round(x) for x in nums]
print("Minimum value:", min(rounded))
print("Maximum value:", max(rounded))

multiplied = sorted({x * 5 for x in rounded})
print(*multiplied)


# Write a Python program to count the number of lists in a given list of lists.
lst1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
lst2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

print("Number of lists in lst1:", len(lst1))