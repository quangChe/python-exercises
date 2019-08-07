import re

def find_all(patterns, string):
  for pat in patterns:
    print(re.findall(pat, string))


# # 0 or more letters (d)
# text_patterns = ['sd*']
# text = 'ssssssd sddddd sd ssss dsss'


# # 1 or more letters (d)
# text_patterns = ['sd+']
# text = 'ssssssd sddddd sd ssss dsss'


# # 0 or 1 letter (d)
# text_patterns = ['sd?']
# text = 'ssssssd sddddd sd ssss dsss'


# # Specific count of letter (d)
# text_patterns = ['sd{5}']
# text_patterns = ['sd{2,5}']
# text = 'ssssssd sddddd sdd ssss dsss'


# # Several letters wrapped in []
# text_patterns = ['s[sd]+']
# text = 'ssssssd sddddd sdd ssss dsss'

 
# # EXCLUDE all of characters using ^
# text_patterns = ['[^!.?\',]+']
# text = "Hello! What's up? I'm good, and you?"


# # All lowercase/uppercase letters
# text_patterns = ['[a-z]+']
# text_patterns = ['[A-Z]+']
# text = "Hello! What's up? I'm good, and you?"


# # All digits
# # The 'r' indicates Python string literal without having to escape antyhing
# # \d escapes the regular d and turns it into representation of 'digits'
# text_patterns = [r'\d+']
# text = "Hello! What's up? 388383 I'm good, and you? 3838"

# # All non-digits
# text_patterns = [r'\D+']
# text = "Hello! What's up? 388383 I'm good, and you? 3838"


# # All whitespace
# text_patterns = [r'\s+']
# text = "Hello! What's up? 388383 I'm good, and you? 3838"

# # All non-whitespace
# text_patterns = [r'\S+']
# text = "Hello! What's up? 388383 I'm good, and you? 3838"


# # All alphanumeric
# text_patterns = [r'\w+']
# text = "Hello! What's up? 388383 I'm good, and you? 3838"

# All non-alphanumeric (including whitespaces)
text_patterns = [r'\W+']
text = "Hello! What's up? 388383 I'm good, and you? 3838"

find_all(text_patterns, text)