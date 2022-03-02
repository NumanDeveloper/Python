import re

# dot . matches any character, other than a new line.
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("match 1")

if re.search(pattern, "ffgrty"):
    print("match 2")

if re.match(pattern, "blue"):
    print("match 3")
