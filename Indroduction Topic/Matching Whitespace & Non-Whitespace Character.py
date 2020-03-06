Regex_Pattern = r"\S{2}\s\S{2}\s\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
