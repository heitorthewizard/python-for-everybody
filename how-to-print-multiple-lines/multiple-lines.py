text = '''
Hello, I'm Heitor
This is a line Wrapper
Text that I am  storing
inside a variable
'''

print(text)

print("""
I am also using 
it directly inside
the print function
""")

print('Let\'s play a game\n')
name = input('What\'s your name? ')
age = input('How old are you, {}? '.format(name))
answer = f"""
Hello, {name}!
wow...
you are {age} old!
That's awesome
"""

print(answer)

print(f"{name}, you're awesome")

