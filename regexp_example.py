import re

text = "Hello world, this is your capitan speaking"
pattern = r'[A-Za-z]+'
print(re.search(pattern, text))

# email_str = "example@gmail.com"
# pattern = r'([A-Za-z]+)@([A-Za-z]+).([A-Za-z]+)'
# email_match = re.match(pattern, email_str)
# print(email_match.groups())

# email_str = "example@gmail.com"
# pattern = r'(?P<username>\w+)@(?P<domain>\w+).(?P<top_level_domain>\w+)'
# email_match = re.match(pattern, email_str)
# print(email_match.groupdict())