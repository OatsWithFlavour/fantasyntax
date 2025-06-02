import re

text = """liste:
- punkt1
- punkt2
- punkt3

"""

regex = r"^liste:\s*$([\s\S]*?)^\s*$"
match = re.search(regex, text, re.MULTILINE)
if match:
    print("Gefunden:", match.group(1))
else:
    print("Kein Treffer.")
