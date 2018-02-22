import re

line = "The ghost that says boo haunts the loo."

result = re.findall(".oo", line, re.IGNORECASE)
print(result)