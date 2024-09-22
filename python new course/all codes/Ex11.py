import re
str = '''
Hlo my name is Rohan 
abc@gmail.com
this is first email
123@gamil.com
'''
a = re.compile(r'.com')
match = a.finditer(str)
for matches in match:
    print(matches)
    

