
# Write a Python function to get a string made of the first three characters of a specified string. 
# If the length of the string is less than 3, return the original string.
def reduced_str(str_val): 
    if len(str_val) > 3:
        return str_val[:3]
    else:
        return str_val
    

print(reduced_str("Hidaya"))


# Write a Python program to create a Caesar encryption.
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha(): 
            start = ord('a') if char.islower() else ord('A')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            result += char 
    return result


print(caesar_encrypt("Word", 6))

# Write a Python program to remove duplicate characters from a given string.pass

def remove_duplicate(word):
    seen_characters = set()
    results = []

    for char in word :
        if char not in seen_characters:
            results.append(char)
            seen_characters.add(char)
    return results

print(remove_duplicate("Hello"))

# Write a Python program to delete all occurrences of
#  a specified character in a given string.

def deletes_letter(word, letter):
    new_word = word.replace(letter, "")
    return new_word

print(deletes_letter("Mariam" , "a"))

# Write a Python program that counts the number of leap years 
# within the range of years. Ranges of years should be accepted as strings.


def leap_years(year_range):
    start_year, end_year = map(int, year_range.split('-'))
    
    leaps = []
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leaps.append(year)
    return len(leaps)

print(leap_years("1981-1991"))

# Write a Python program to insert space before every capital letter appears in a given word.

def add_space_before_capital(text):
    result = []
    for i, char in enumerate(text):
        if char.isupper():  
            result.append(' ')
        result.append(char)
    return ''.join(result)

print(add_space_before_capital("HidAyA"))

