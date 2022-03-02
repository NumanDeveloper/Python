import re

"""dot . matches any character, other than a new line
The next two metacharacters are ^(start) and $(end).These match the start and end of a string, respectively."""

pattern = r"^gr..y$"
# The pattern "^gr.y$" means that the string should start with gr, then follow with any  two characters, except a newline, and end with y.

if re.match(pattern, "graey"):
    print("match 1")

if re.search(pattern, "graay"):
    print("match 2")

if re.match(pattern, "stingray"):
    print("match 3")
