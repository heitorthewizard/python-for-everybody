file_handler = open('mbox-short.txt')

# Getting the word "Sat" from .txt file
for line in file_handler:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print(words[2])


# getting email
email = words[1]
print(email)

domain = email.split('@')[1]
print(domain)
