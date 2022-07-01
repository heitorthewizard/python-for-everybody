# Matching and Extracting Data
# re.search() returns boolean weather the string matches the regex
# re.findall() returns the value that matches the string
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
w = re.findall('[AEIOU]', x)
print(w)

