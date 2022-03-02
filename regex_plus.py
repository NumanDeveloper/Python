import re

pattern = r"g+$"
"""The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions"."""
if re.match(pattern, "g"):
    print("match 1")

if re.match(pattern, "gggggk"):
    print("match 2")

if re.match(pattern, "abc"):
    print("match 3")

"""To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression."""
