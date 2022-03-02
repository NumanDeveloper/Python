import re

pattern = r"harry(porter)*"
"""The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses."""

if re.match(pattern, "harry"):
    print("match 1")

if re.search(pattern, "porterharry"):
    print("match 2")

if re.match(pattern, "porterharry"):
    print("match 3")
