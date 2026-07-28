import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

replaced = re.sub ('python|Python', 'Ruby', txt, re.I)
print(replaced)
