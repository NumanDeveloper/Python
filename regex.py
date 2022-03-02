import re
pattern = r"email"
if re.match(pattern, "mailemailemail"):
    print("match")
else:
    print("no match")

if re.search(pattern, "mailemailmail"):
    print("match")
else:
    print("no match")

if re.finditer(pattern, "mailemailemail"):
    print("match")
else:
    print("no match")
