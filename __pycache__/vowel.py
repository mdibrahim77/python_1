
def count_vowels(text):
    count = 0
    vowels = "aeiou"

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


# Test cases
print(count_vowels("Hello World"))  
"""
print(count_vowels("PYTHON"))       
print(count_vowels("Education"))   
print(count_vowels("rhythm"))    
"""   
