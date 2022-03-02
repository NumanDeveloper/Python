import re

pattern = r"spam"
match = re.search(pattern, "sausagespam")
print(match)

# These methods include GROUP() which returns the string matched, 
# START() and END() which return the start and ending positions of the first match, 
# and SPAN() which returns the start and end positions of the first match as a tuple.

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
