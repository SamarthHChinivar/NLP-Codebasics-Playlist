#Customer service chatbot regex
import re

chat1 = 'here it is phone:(123)-456-7890 email:abc@gmail.com with my order #412889912'
chat2 = 'you ask lot of questions 1234567890, abc@gmail.com with my order  number 412889912'
chat3 = 'phone number is 1234567890 and email is abc@gmail.com and my order number is 412889912'

pattern_phone = '\d{10}|\(\d{3}\)-\d{3}-\d{4}'
pattern_email = "[a-z0-9_.]+@[a-z._]+[a-z.]+"
pattern_orderno = "order [^\d]+(\d+)"

match_phone = re.findall(pattern_phone,chat2)
match_email = re.findall(pattern_email,chat2)
match_orderno = re.findall(pattern_orderno,chat2)

print(match_phone[0],"    ", match_email[0], "   ", match_orderno[0])