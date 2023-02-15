import re

from soupsieve import match

text = ''' Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.'''

pattern = "FY(.*)\was"

match = re.findall(pattern,text)
print(match)