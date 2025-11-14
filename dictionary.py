from collections import Counter

# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)

# Write a Python program to print all distinct values in a dictionary.
data = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = {v for d in data for v in d.values()}
print("Unique Values:", unique_values)


# Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = Counter(d1) + Counter(d2)
print(result)

# Write a Python program to get the top three items in a shop.
shop = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

top_three = sorted(shop.items(), key=lambda x: x[1], reverse=True)[:3]

for item, price in top_three:
    print(item, price)

# Write a Python program to filter a dictionary based on values.
marks = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}

filtered = {k: v for k, v in marks.items() if v > 170}
print(filtered)

# Write a Python program to extract a list of values from a given list of dictionaries.

data = [
    {'Math': 90, 'Science': 92},
    {'Math': 89, 'Science': 94},
    {'Math': 92, 'Science': 88}
]

science_values = [d['Science'] for d in data]
print(science_values)