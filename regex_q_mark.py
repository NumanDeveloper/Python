import re

pattern = r"ice(-)?cream"
"""The metacharacter ? means "zero or one repetitions"."""
if re.match(pattern, "ice-cream"):
    print("match 1")

if re.search(pattern, "icecream"):
    print("match 2")

if re.match(pattern, "ice--cream"):
    print("match 3")
