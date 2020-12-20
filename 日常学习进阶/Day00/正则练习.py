import re

data = "asdasd(asdasd)asdasd"
print(re.search(r"\(.*\)", data).group(0).strip("()"))
print(type(r"a"))

