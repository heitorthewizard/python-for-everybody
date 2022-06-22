file_name = input('Enter the file name: ')
try:
    read_file = open(file_name)
except:
    print('File cannot be opened: ', file_name)
    quit()

count = 0

for line in read_file:
    if line.startswith('Subject:'):
        count = count + 1

print(f'There were {count} subject lines in {file_name}')

