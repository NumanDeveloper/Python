import re

# Character classes provide a way to match only one of a specific set of characters.A character class is created by putting the characters it matches inside square brackets.

pattern = r"[a,e,i,o,u]"
# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.
if re.search(pattern, "gray"):
    print("Match 1")

if re.search(pattern, "qwerty"):
    print("Match 2")

if re.search(pattern, "rhythm"):
    print("Match 3")
