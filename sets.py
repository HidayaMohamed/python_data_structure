# Write a Python program to find the length of a set.
s = {1, 2, 3, 4, 5}

print(len(s))

# Write a Python program to add member(s) to a set.
s = {1, 2, 3}

# Add a single member
s.add(4)

# Add multiple members
s.update([5, 6, 7])

print(s)


# Write a Python program to remove item(s) from a given set.
s = {1, 2, 3, 4, 5}

# Remove an item (throws error if item not found)
s.remove(3)

# Discard an item (does NOT throw an error if not found)
s.discard(10)

# Remove and return an arbitrary element
removed = s.pop()

print(s)
print("Popped:", removed)

# Write a Python program to create an intersection of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)


# Write a Python program to create a union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)


# Write a Python program to create set difference.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

result = set1.difference(set2)

print(result)


# Write a Python program to find the maximum and minimum values in a set.
s = {10, 3, 25, 7, 1}

print("Max:", max(s))
print("Min:", min(s))

