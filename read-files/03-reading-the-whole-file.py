file_handler = open('random-file.txt')
intrerpeter = file_handler.read()

print(intrerpeter)
print('length:', len(intrerpeter))
print('printing 100 characters\n', intrerpeter[:100])

