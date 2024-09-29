def count_characters(s):
    lower_case = 0
    upper_case = 0
    digits = 0
    special_symbols = 0

    for char in s:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return lower_case, upper_case, digits, special_symbols

input_string = "Hello World"
lower, upper, digits, special = count_characters(input_string)
print(f"Lower case characters: {lower}")
print(f"Upper case characters: {upper}")
print(f"Digits: {digits}")
print(f"Special symbols: {special}")
