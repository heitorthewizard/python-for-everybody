# fine-tuning string extraction
import re

x = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'

y = re.findall('\\S+@\\S+', x)
print(y)

