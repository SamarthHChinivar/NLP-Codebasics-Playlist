#Information Extraction

import re
from unicodedata import name

text = '''Born	Pichai Sundararajan
June 10, 1972 (age 50)
Madurai, Tamil Nadu, India
Citizenship	United States[1]
Education	IIT Kharagpur (BTech)
Stanford University (MS)
University of Pennsylvania (MBA)
Title	CEO of Alphabet and Google'''

pattern_age = "age (\d+)"
pattern_name = "Born(.*)"
pattern_date = "Born.*\n(.*)\("
pattern_bp = "\(age.*\n(.*)"

def get_pattern_match(pattern,text):
    match = re.findall(pattern,text)
    if(match != []):
        return match[0]

def get_personal_info(text):
     name = get_pattern_match(pattern_name,text)
     date = get_pattern_match(pattern_date,text)
     age  = get_pattern_match(pattern_age,text)
     bp   = get_pattern_match(pattern_bp,text)
     
     return {
        'Name' : name.strip(),
        'Date' : date.strip(),
        'Age'  : int(age),
        'Birthplace'   : bp.strip()
    }

print(get_personal_info(text))