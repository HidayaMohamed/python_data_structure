# Write a Python program to replace the last value of tuples in a list.
data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = [t[:-1] + (100,) for t in data]

print(result)


# Write a Python program to remove an empty tuple(s) from a list of tuples.
data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

result = [t for t in data if t]

print(result)


# Write a Python program to sort a tuple by its float element.
data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

result = sorted(data, key=lambda x: float(x[1]), reverse=True)

print(result)


# Write a Python program to convert a given tuple of positive integers into an integer.
def tuple_to_int(t):
    return int("".join(str(x) for x in t))

print(tuple_to_int((1, 2, 3)))
print(tuple_to_int((10, 20, 40, 5, 70)))


# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
data1 = [(1, 2), (2, 3), (3, 4)]
data2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

print([sum(t) for t in data1])
print([sum(t) for t in data2])


# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
def column_averages(tuples):
    return [sum(col) / len(col) for col in zip(*tuples)]

data1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
data2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

print(column_averages(data1))
print(column_averages(data2))
