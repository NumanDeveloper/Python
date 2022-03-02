import re

"""Place a ^(caret) at the start of a character class to invert it. 

This causes it to match any character other than the ones included. 

Other metacharacters such as $ and ., have no meaning within character classes. 

The metacharacter ^ has no meaning unless it is the first character in a class."""

pattern = r"[^A-Z]"
"""The pattern [^A-Z] excludes uppercase strings.

Note, that the ^ should be inside the brackets to invert the character class."""

if re.search(pattern, "this is caret"):
    print("Match 1")

if re.search(pattern, "AeIoU999"):
    print("Match 2")

if re.search(pattern, "UPPERCASE"):
    print("Match 3")
