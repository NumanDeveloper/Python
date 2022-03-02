import re

str = "It's Numan here. Hi, Numan"
pattern = r"Numan"

# sub() method replaces all occurrences of the pattern in string with replace word, substituting all occurrences, unless count provided. This method returns the modified string.
# syntax : sub(pattern, repl, str, count)
new_str = re.sub(pattern, "Hasnain", str)
print(str)
print(new_str)
