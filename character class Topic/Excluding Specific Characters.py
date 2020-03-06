Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s\r\n\t][^AEIOU][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
